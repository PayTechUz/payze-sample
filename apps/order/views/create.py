from django.db import DatabaseError

from rest_framework import views
from rest_framework import response

from apps.utility.logger import logger
from apps.order.serializers import CreateOrderSerializer
from apps.utility.exceptions import ServiceAPIException500


class CreateOrderAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data
        )
        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        try:
            Order.objects.create(
                card_id=data.get("card_id"),
                amount=data.get("amount"),
            )
        
        except DatabaseError as error:
            logger.error("error was occurred while creating new order: %s", error)
            raise ServiceAPIException500()

        return response.Response({
            "status": "success",
        })
