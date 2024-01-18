"""
cards admin side.
"""
from django.contrib import admin

from apps.payment.models import cards


admin.site.register(cards.Cards)
admin.site.register(cards.CardVerifyPayment)
