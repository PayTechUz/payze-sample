"""
payer admin side.
"""
from django.contrib import admin

from unfold.admin import ModelAdmin

from apps.payment.models import payer


class PayerUnfolderAdmin(ModelAdmin):
    """
    payer unfolder admin side.
    """
    list_display = [
        "full_name",
        "phone_number",
    ]
    exclude = (
        "is_deleted",
    )


admin.site.register(payer.Payer, PayerUnfolderAdmin)
