"""
payments model.
"""
from django.utils.translation import gettext_lazy as _

from apps.payment.enums import ps
from apps.payment.enums import pt
from apps.payment.models import base
from apps.payment.enums import reason
from apps.payment.enums import currency


class Payments(base.BaseModel):
    """
    payments model.
    """
    class Meta:
        """
        meta fields
        """
        db_table = "payments"
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    card_id = base.models.IntegerField(verbose_name=_("Card ID"),)
    order_id = base.models.IntegerField(verbose_name=_("Order ID"), null=True)

    commission = base.models.IntegerField(
        verbose_name=_("Commission"),
        default=0,
        null=True
    )
    invoice = base.models.CharField(
        verbose_name=_("Invoice"),
        max_length=255,
        null=False
    )
    amount = base.models.FloatField(
        verbose_name=_("Amount"),
        default=0,
        null=False
    )
    final_amount = base.models.FloatField(
        verbose_name=_("Final Amount"),
        default=0,
        null=True,
        blank=True
    )
    debt = base.models.FloatField(
        verbose_name=_("Debt"),
        default=0,
        null=False
    )
    credit = base.models.FloatField(
        verbose_name=_("Credit"),
        default=0,
        null=False
    )
    reason = base.models.IntegerField(
        verbose_name=_("Reason"),
        choices=[
            (member.value, member.name) for member in reason.PaymentReason
        ],
    )
    currency = base.models.CharField(
        verbose_name=_("Currency"),
        max_length=40,
        choices=[
            (member.value, member.name) for member in currency.Currency
        ],
    )
    provider_type = base.models.CharField(
        verbose_name=_("Provider Type"),
        max_length=40,
        choices=[
            (member.value, member.name) for member in pt.ProviderTypes
        ],
    )
    status = base.models.CharField(
        verbose_name=_("Status"),
        max_length=40,
        choices=[
            (member.value, member.name) for member in ps.Status
        ],
        default=ps.Status.PENDING.value
    )
    idempotency_key = base.models.CharField(
        max_length=50,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_("Idempotency Key"),
    )
