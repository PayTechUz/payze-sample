"""
cards admin side.
"""
from django.contrib import admin

from unfold.admin import ModelAdmin

from apps.payment.models import cards


class CardsUnfoldAdmin(ModelAdmin):
    """
    cards unfold admin side.
    """
    list_display = [
        "number",
        "expire_date",
        "is_active",
        "entity_type",
        "brand_types"
    ]
    exclude = (
        "is_deleted",
    )


admin.site.register(cards.Cards, CardsUnfoldAdmin)
