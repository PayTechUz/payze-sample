from rest_framework import serializers


class CreateOrderSerializer(serializers.Serializer):
    card_id = serializers.IntegerField()
    amount = serializers.IntegerField()
