from django.db import DatabaseError

from rest_framework import views
from rest_framework import response

from apps.utility.logger import logger
from apps.order.models.order import Order
from apps.payment.libs.payze import payze
from apps.payment.serializers import PaySerializer
from apps.utility.exceptions import ServiceAPIException
from apps.utility.exceptions import ServiceAPIException500


class PayAPIView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = PaySerializer(
            data=request.data
        )
        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data
        order_id = data.get("order_id")

        try:
            order = Order.objects.get(
                id=order_id,
            )

        except Order.DoesNotExist as error:
            logger.error("error was occurred while getting order: %s", error)
            raise ServiceAPIException(
                type="not_found",
                message=f"order not found - {order_id}",
                status_code=404
            )

        except DatabaseError as error:
            logger.error("error was occurred while getting order: %s", error)
            raise ServiceAPIException500()
        
        payze.pay_with_card(
            amount=order.amount,
            order=order,
            card_token=order.card.card_token,
            hook_refound=True
        )

        return response.Response({
            "status": "success",
        })
