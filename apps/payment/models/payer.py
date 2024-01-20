"""
the cards database model
"""
from django.utils.translation import gettext_lazy as _

from apps.payment.models import base


class Payer(base.BaseModel):
    """
    payer information.
    """
    class Meta:
        """
        meta fields
        """
        db_table = "card_payer"
        verbose_name = _('Payer')
        verbose_name_plural = _('Payers')

    full_name = base.models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_("Full Name"),
    )
    phone_number = base.models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_("Phone Number"),
    )
    # additional fields should be added
