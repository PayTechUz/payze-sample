"""
payze webhooks for card actions.
"""
import logging

from rest_framework import views
from rest_framework import response

from apps.abc.app import IApp
from apps.app import app_context
from apps.abc.params import cards
from apps.payment.providers.payze.enums import ps
from apps.payment.providers.payze.enums import types
from apps.payment.providers.payze.enums import source
from apps.utility.exceptions import ServiceAPIException
from apps.payment.providers.payze.serializers import webhook


logger = logging.getLogger(__name__)


class CardsWebHooksAPIView(views.APIView):
    """
    cards webhooks for card actions
    """
    def post(self, request, app_context: IApp = app_context):
        """
        the post method for getting card updates
        """
        try:
            data = webhook.CardsWebHookSerializers(**request.data)
        except Exception as exc:
            msg = f"error serializing: {exc}"
            logger.error(msg)
            raise ServiceAPIException(
                type="bad_request",
                message=msg,
                status_code=400
            ) from exc

        if data.type == types.Type.ADD_CARD.value \
            and data.source == source.Sources.CARD.value \
                and data.payment_status == ps.PaymentStatus.DRAFT.value:

            app_context.create_card(
                cards=cards.CardInfo(
                    token=data.token,
                    verify_payments=cards.CardVeryPayments(
                        payment_id=data.payment_id,
                        idempotency_key=data.idempotency_key,
                        currency=data.currency,
                        amount=data.amount,
                        final_amount=data.final_amount,
                        payment_status=data.payment_status
                    )
                )
            )

        if data.type == types.Type.ADD_CARD.value \
            and data.source == source.Sources.CARD.value\
                and data.payment_status != ps.PaymentStatus.DRAFT.value:

            verify_payments = cards.CardVeryPayments(
                payment_id=data.payment_id,
                idempotency_key=data.idempotency_key,
                currency=data.currency,
                amount=data.amount,
                payment_status=data.payment_status,
                final_amount=data.final_amount,
            )
            payer = cards.Payer(
                phone=data.payer.phone,
                full_name=data.payer.full_name
            )

            app_context.update_card(
                card_params=cards.CardInfo(
                    token=data.token,
                    number=data.card_musk,
                    expire_date=data.expire_date,
                    card_brand=data.card_brand,
                    card_entity_type=data.card_owner_entity_type,
                    verify_payments=verify_payments,
                    payer=payer
                )
            )

        return response.Response({
            "data": data.model_dump(),
        })