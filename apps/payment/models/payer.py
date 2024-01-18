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

    full_name = base.models.CharField(
        max_length=30,
        verbose_name=_("Full Name"),
    )
    phone_number = base.models.CharField(
        max_length=30,
        verbose_name=_("Phone Number"),
    )
    # additional fields should be added
