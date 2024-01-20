"""
payments admin.
"""
from django.contrib import admin

from unfold.admin import ModelAdmin

from apps.payment.models import payment


class PaymentsAdmin(ModelAdmin):
    """
    the payments admin
    """
    list_display = [
        "card_id",
        "order_id",
        "invoice",
        "amount",
        "debt",
        "credit",
        "reason",
        "provider_type",
        "status",
        "commission",

    ]
    exclude = (
        "is_deleted",
    )


admin.site.register(payment.Payments, PaymentsAdmin)
