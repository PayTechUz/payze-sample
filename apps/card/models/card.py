from django.db import models

from apps.card.models.payment import PaymentID


class PayzeCardModel(models.Model):
    payment_id = models.OneToOneField(PaymentID, on_delete=models.SET_NULL, null=True)
    card_mask = models.CharField(max_length=20, null=True, blank=True)
    card_brand = models.CharField(max_length=20, null=True, blank=True)
    card_holder = models.CharField(max_length=30, null=True, blank=True)
    expire_date = models.CharField(max_length=5, null=True, blank=True)
    card_token = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "ID — {id} Card Mask — {card_mask} Status — {status}".format(
            id=self.id,
            card_mask=self.card_mask,
            status=self.status
        )
