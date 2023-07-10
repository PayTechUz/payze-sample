from rest_framework import serializers


class CardAccceptSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()
    card_token = serializers.CharField()
