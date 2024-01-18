"""
payer admin side.
"""
from django.contrib import admin

from apps.payment.models import payer


admin.site.register(payer.Payer)
