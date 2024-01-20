"""
the cards database model
"""
from django.utils.translation import gettext_lazy as _

from apps.payment.models import base
from apps.payment.models import payer


class Cards(base.BaseModel):
    """
    the cards database model.
    """
    class Meta:
        """
        meta fields
        """
        db_table = "cards"
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')

    payment_id = base.models.CharField(
        verbose_name=_("Payment ID"),
    )
    number = base.models.CharField(
        max_length=18,
        null=True,
        blank=True,
        verbose_name=_("Number"),
    )
    expire_date = base.models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name=_("Expire Date"),
    )
    token = base.models.CharField(
        max_length=100,
        blank=True,
        unique=True,
        verbose_name=_("Token"),
    )
    is_active = base.models.BooleanField(
        default=False,
        verbose_name=_("Active"),
    )
    entity_type = base.models.CharField(
        max_length=100,
        default="Unknown",
        verbose_name=_("Entity Type"),
    )
    brand_types = base.models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Brand Types"),
    )
    payer = base.models.ForeignKey(
        payer.Payer,
        on_delete=base.models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Payer")
    )
