from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    PaymentId = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    PaymentStatus = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    CardMask = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    CardBrand = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    CardHolder = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    ExpirationDate = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    status = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    type = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    transactionId = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    card_token = serializers.CharField(required=False, allow_blank=True, allow_null=True)
