"""
the card processor implementation.
"""
import logging
from typing import Any

from django.db import transaction

from apps.abc import storage
from apps.abc.params.payment import Payment
from apps.payment.enums import pt
from apps.payment.enums import ps
from apps.abc.params import cards
from apps.payment.enums import reason
from apps.payment.models import Cards
from apps.payment.models import Payer
from apps.payment.models import Payments

from apps.payment.providers.payze.enums import ps as payze_ps


logger = logging.getLogger(__name__)


class PayzeCardProcessor(storage.CardProcessorABC):
    """
    card processor implementation with payze.
    """
    def create_card(self, cards: cards.CardInfo):
        try:
            with transaction.atomic():
                card = Cards.objects.create(
                    payment_id=cards.payment.payment_id,
                    token=cards.token,
                    is_active=False
                )
                Payments.objects.create(
                    card_id=card.id,
                    order_id=0,
                    commission=cards.payment.commission,
                    invoice=card.payment_id,
                    amount=cards.payment.amount,
                    final_amount=cards.payment.final_amount,
                    debit=cards.payment.amount,
                    credit=0,
                    reason=reason.PaymentReason.CARD_VERIFY.value,
                    currency=cards.payment.currency,
                    provider_type=pt.ProviderTypes.PAYZE.value,
                    status=ps.Status.PENDING.value,
                    idempotency_key=cards.payment.idempotency_key
                )

        except Exception as exc:
            logger.error("error creating card - %s", exc)

    def update_card(self, card_params: cards.CardInfo) -> Any:
        payment_status = card_params.payment.payment_status
        payment_id = card_params.payment.payment_id
        idempotency_key = card_params.payment.idempotency_key

        if payment_status == "Captured":
            status = ps.Status.SUCCESS.value
        elif payment_status == "Rejected":
            status = ps.Status.REJECTED.value
        elif payment_status == "Draft":
            status = ps.Status.PENDING.value

        try:
            with transaction.atomic():
                card_object, _ = Cards.objects.update_or_create(
                    payment_id=payment_id,
                    token=card_params.token,
                    defaults={
                        'is_active': False,
                        'number': card_params.number,
                        'expire_date': card_params.expire_date,
                        'entity_type': card_params.card_entity_type,
                        'brand_types': card_params.card_brand,
                    }
                )

                if not card_params.payment.amount:
                    debit = 0.0

                if not card_params.payment.commission:
                    commission = 0.0

                payment, _ = Payments.objects.update_or_create(
                    invoice=payment_id,
                    defaults={
                        'card_id': card_object.id,
                        'order_id': 0,
                        'commission': commission,
                        'amount': card_params.payment.amount,
                        'final_amount': card_params.payment.final_amount,
                        'debit': debit,
                        'credit': 0,
                        'reason': reason.PaymentReason.CARD_VERIFY.value,
                        'currency': card_params.payment.currency,
                        'provider_type': pt.ProviderTypes.PAYZE.value,
                        'status': status,
                        'idempotency_key': idempotency_key,
                    }
                )

                if not card_object.payer \
                    and card_params.payer.phone \
                        and card_params.payer.full_name:
                    card_object.payer = Payer.objects.create(
                        phone_number=card_params.payer.phone,
                        full_name=card_params.payer.full_name
                    )

                payment_fields = {
                    'status': status,
                    'commission': card_params.payment.commission,
                    'amount': card_params.payment.amount,
                    'final_amount': card_params.payment.final_amount,
                    'debit': card_params.payment.amount,
                }

                Payments.objects.filter(pk=payment.pk).update(**payment_fields)

                if card_object.payer:
                    Payer.objects.filter(pk=card_object.payer.pk).update(
                        phone_number=card_params.payer.phone,
                        full_name=card_params.payer.full_name
                    )

                is_active = card_params.payment.payment_status \
                    == payze_ps.PaymentStatus.CAPTURED.value

                card_fields = {
                    'is_active': is_active,
                    'entity_type': card_params.card_entity_type,
                    'brand_types': card_params.card_brand,
                    'payer': card_object.payer
                }

                Cards.objects.filter(pk=card_object.pk).update(**card_fields)

        except Exception as exc:
            logger.error("Error updating card object - %s", exc)

    def deactivate_card(self, card_params: cards.CardInfo) -> Any:
        try:
            with transaction.atomic():
                Payments.objects.filter(
                    invoice=card_params.payment.payment_id
                ).delete()

                cards = Cards.objects.filter(
                    payment_id=card_params.payment.payment_id
                )
                for card in cards:
                    card.payer.delete()

                cards.delete()

        except Exception as exc:
            logger.error("Error deleting card object - %s", exc)

    def create_payment(self, _: Payment) -> None:
        raise NotImplementedError(
            "create payment does not support in card processor"
        )


card_processor = PayzeCardProcessor()
