from django.contrib import admin

from apps.card.models.payment import PaymentID
from apps.card.models.card import PayzeCardModel


admin.site.register(PaymentID)
admin.site.register(PayzeCardModel)
