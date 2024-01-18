"""
the cards database model
"""
from django.utils.translation import gettext_lazy as _

from apps.payment.models import base
from apps.payment.models import payer


class CardVerifyPayment(base.BaseModel):
    """
    card verify payments.
    """
    class Meta:
        """
        meta fields
        """
        db_table = "card_verify_payments"

    payment_id = base.models.CharField(
        max_length=255,
        null=False,
        blank=False,
        primary_key=True,
        verbose_name=_("Payment ID"),
    )
    amount = base.models.FloatField(
        verbose_name=_("Amount"),
        default=0
    )
    currency = base.models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name=_("Currency"),
    )
    payment_status = base.models.CharField(
        max_length=16,
        verbose_name=_("Payment Status"),
    )
    idempotency_key = base.models.CharField(
        max_length=50,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_("Idempotency Key"),
    )
    final_amount = base.models.FloatField(
        verbose_name=_("Final Amount"),
        default=0,
        null=True,
        blank=True,
    )


class Cards(base.BaseModel):
    """
    the cards database model.
    """
    class Meta:
        """
        meta fields
        """
        db_table = "cards"
    verify_payment = base.models.ForeignKey(
        CardVerifyPayment,
        on_delete=base.models.CASCADE,
        verbose_name=_("Very Payment"),
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
