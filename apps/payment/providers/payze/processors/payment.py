"""
the payment processor implementation.
"""
import logging

from django.db import transaction

from apps.abc import storage
from apps.abc.params.payment import Payment


from apps.payment.enums import pt
from apps.payment.enums import ps
from apps.payment.enums import reason
from apps.payment.models import Cards
from apps.payment.models import Payments


logger = logging.getLogger(__name__)


class PaymentProcessor(storage.PaymentProcessorABC):
    """
    payment processor implementation
    """
    def store_payment(self, payment: Payment) -> None:
        if payment.payment_status == "Captured":
            status = ps.Status.SUCCESS.value

        if payment.payment_status == "Rejected":
            status = ps.Status.REJECTED.value

        if payment.payment_status == "Draft":
            status = ps.Status.PENDING.value

        # TODO: if unknown status come, need notification

        try:
            with transaction.atomic():
                card = Cards.objects.get(
                    token=payment.token,
                    is_active=True
                )
            Payments.objects.update_or_create(
                invoice=payment.payment_id,
                credit=0,
                idempotency_key=payment.idempotency_key,
                defaults={
                    "card_id": card.id,
                    "order_id": payment.order_id,
                    "commission": payment.commission,
                    "amount": payment.amount,
                    "final_amount": payment.final_amount,
                    "debit": payment.final_amount,
                    "reason": reason.PaymentReason.ORDER.value,
                    "currency": payment.currency,
                    "provider_type": pt.ProviderTypes.PAYZE.value,
                    "status": status,
                }
            )

        except Exception as exc:
            logger.error("error storing payment - %s", exc)


payment_processor = PaymentProcessor()
