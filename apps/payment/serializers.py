from rest_framework import serializers


class PaySerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
