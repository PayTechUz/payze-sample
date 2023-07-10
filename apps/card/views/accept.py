from rest_framework import views
from rest_framework import response

from apps.card.serializer import CardAccceptSerializer
from apps.card.libs.card_processor import card_processor


class CardAccceptAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CardAccceptSerializer(
            data=request.data
        )
        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        card_processor.set_token(
            payment_id=data.get("transaction_id"),
            card_token=data.get("card_token")
        )

        return response.Response({
            "status": "success",
        })

