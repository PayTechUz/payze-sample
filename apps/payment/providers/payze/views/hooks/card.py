"""
payze webhooks for card actions.
"""
import logging

from rest_framework import views
from rest_framework import response

from apps.app import app_context
from apps.abc.params import cards
from apps.abc.params import payment
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
    def post(self, request):
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

        payment_param = payment.Payment(
            payment_id=data.payment_id,
            token=data.token,
            idempotency_key=data.idempotency_key,
            currency=data.currency,
            amount=data.amount,
            commission=data.commission,
            final_amount=data.final_amount,
            payment_status=data.payment_status
        )

        if data.type == types.Type.ADD_CARD.value \
            and data.source == source.Sources.CARD.value \
                and data.payment_status == ps.PaymentStatus.DRAFT.value:

            app_context.create_card(
                cards=cards.CardInfo(
                    token=data.token,
                    payment=payment_param
                )
            )

        if data.type == types.Type.ADD_CARD.value \
            and data.source == source.Sources.CARD.value\
            and data.payment_status == ps.PaymentStatus.REJECTED.value\
                and data.rejected_reason == "Timeout":

            app_context.deactivate_card(
                card_params=cards.CardInfo(
                    token=data.token,
                    payment=payment.Payment(
                        payment_id=data.payment_id
                    )
                )
            )

            return response.Response()

        if data.type == types.Type.ADD_CARD.value \
            and data.source == source.Sources.CARD.value\
                and data.payment_status not in [
                     ps.PaymentStatus.DRAFT.value,
                ]:

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
                    payment=payment_param,
                    payer=payer
                )
            )

        return response.Response()
