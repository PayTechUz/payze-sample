"""
the card processor implementation.
"""
import logging
from typing import Any

from django.db import transaction

from apps.abc import storage
from apps.abc.params import cards

from apps.payment.models import Cards
from apps.payment.models import Payer
from apps.payment.models import CardVerifyPayment
from apps.payment.providers.payze.enums import ps


logger = logging.getLogger(__name__)


class PayzeCardProcessor(storage.CardProcessorABC):
    """
    card processor implementation with payze.
    """
    def create_card(self, cards: cards.CardInfo):
        try:
            with transaction.atomic():
                verify_payment = CardVerifyPayment.objects.create(
                    payment_id=cards.verify_payments.payment_id,
                    currency=cards.verify_payments.currency,
                    amount=cards.verify_payments.amount,
                    final_amount=cards.verify_payments.final_amount,
                    payment_status=cards.verify_payments.payment_status,
                    idempotency_key=cards.verify_payments.idempotency_key,
                )
                Cards.objects.create(
                    verify_payment_id=verify_payment.payment_id,
                    token=cards.token,
                    is_active=False
                )

        except Exception as exc:
            logger.error("error creating card - %s", exc)

    def update_card(self, card_params: cards.CardInfo) -> Any:
        is_active = card_params.verify_payments.payment_status \
            == ps.PaymentStatus.CAPTURED.value

        token = card_params.token
        phone_number = card_params.payer.phone
        full_name = card_params.payer.full_name
        amount = card_params.verify_payments.amount
        currency = card_params.verify_payments.currency
        payment_id = card_params.verify_payments.payment_id
        final_amount = card_params.verify_payments.final_amount
        payment_status = card_params.verify_payments.payment_status
        idempotency_key = card_params.verify_payments.idempotency_key

        try:
            with transaction.atomic():
                card_object, created = Cards.objects.get_or_create(
                    verify_payment_id=payment_id,
                    token=token,
                    defaults={
                        'is_active': False
                    }
                )

                if created:
                    verify_payment = CardVerifyPayment.objects.create(
                        payment_id=payment_id,
                        currency=currency,
                        amount=amount,
                        final_amount=final_amount,
                        payment_status=payment_status,
                        idempotency_key=idempotency_key
                    )
                    card_object.verify_payment_id = verify_payment.payment_id

                if not card_object.payer:
                    card_object.payer = Payer.objects.create(
                        phone_number=phone_number,
                        full_name=full_name
                    )

                if card_object.payer:
                    card_object.payer.phone_number = phone_number
                    card_object.payer.full_name = full_name
                    card_object.payer.save()

                card_object.number = card_params.number
                card_object.expire_date = card_params.expire_date
                card_object.is_active = is_active
                card_object.entity_type = card_params.card_entity_type
                card_object.brand_types = card_params.card_brand
                card_object.save()

        except Exception as exc:
            logger.error("Error updating card object - %s", exc)

    def deactivate_card(self, card_params: Any) -> Any:
        return super().deactivate_card(card_params)


card_processor = PayzeCardProcessor()
