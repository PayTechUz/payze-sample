from django.db import models

from apps.card.models.card import PayzeCardModel


class Order(models.Model):
    card = models.ForeignKey(PayzeCardModel, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Order - ID {self.id}"
