from rest_framework import views
from rest_framework import response

from drf_yasg.utils import swagger_auto_schema

from apps.utility.logger import logger
from apps.callback.serializer import PaymentSerializer
from apps.card.libs.card_processor import card_processor


class CallBackURLAPIView(views.APIView):
    DRAFT = "Draft"
    CAPTURED = "Captured"
    COMMITED = "Commited"
    ACTIVATED = "CardAdded"
    PAYWITHCARD = "PayWithCard"

    @swagger_auto_schema(
        request_body=PaymentSerializer,
        responses={200: "{'status': str}"}
    )

    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        if data.get("PaymentStatus") == self.DRAFT:
            card_processor.add_payment(
                payment_id=data.get("PaymentId")
            )

        if data.get("PaymentStatus") == self.CAPTURED:
            card_processor.set_captured(
                payment_id=data.get("PaymentId"),
                card_mask=data.get("CardMask"),
                card_holder=data.get("CardHolder"),
                expire_date=data.get("ExpirationDate"),
                card_brand=data.get("CardBrand")
            )

        if data.get("status") == self.ACTIVATED:
            card_processor.set_to_activated(
                payment_id=data.get("transactionId"),
            )

        if data.get("type") == self.PAYWITHCARD and self.COMMITED:
            logger.info("Payment has been successfully processed %s", data.get("transactionId"))

        return response.Response({
            "status": "success",
        })
