from django.db import models

from apps.order.models.order import Order
from apps.card.models.card import PayzeCardModel


class Transactions(models.Model):
    """
    Transaction models that's
    help for saving transactions information.
    """
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.FloatField(null=False, blank=False)
    transaction_id = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(max_length=10, null=False, blank=False)
    transaction_info = models.JSONField(null=False, blank=True)


    def __str__(self):
        return f"Order ID - {self.order_id} - Transaction ID - {self.transaction_id}"
