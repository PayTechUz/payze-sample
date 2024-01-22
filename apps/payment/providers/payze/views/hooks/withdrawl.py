"""
create payment web hook http message listener.
"""
import logging

from rest_framework import views
from rest_framework import response

from apps.app import app_context
from apps.abc.params import payment
from apps.utility.exceptions import ServiceAPIException
from apps.payment.providers.payze.serializers import webhook


logger = logging.getLogger(__name__)


class CreatePaymentAPIView(views.APIView):
    """
    create payment api view.
    """
    def post(self, request):
        """
        the post method is called
        when the payment web hook is come
        """
        try:
            data = webhook.WithDrawlWebHookSerializer(**request.data)
        except Exception as exc:
            msg = f"error serializing: {exc}"
            logger.error(msg)
            raise ServiceAPIException(
                type="bad_request",
                message=msg,
                status_code=400
            ) from exc

        app_context.store_payment(
            payment=payment.Payment(
                payment_id=data.payment_id,
                token=data.token,
                amount=data.amount,
                currency=data.currency,
                commission=data.commission,
                payment_status=data.payment_status,
                final_amount=data.final_amount,
                idempotency_key=data.idempotency_key,
                order_id=data.metadata.extra_attribute[2].value
            )
        )
        return response.Response()
