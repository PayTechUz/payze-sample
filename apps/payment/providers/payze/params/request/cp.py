"""
the create payment models.
"""
import uuid

from apps.abc.params import cp
from apps.payment.providers.payze.params.request import base


class CreatePayment(cp.CreatePayment):
    """
    get token request model.
    """
    language: str = "UZ"
    source: str = "Card"
    currency: str = "UZS"
    hooks: base.Hooks = None
    idempotency_key: str = str(uuid.uuid4())

    def to_dict(self):
        """
        the dict representation.
        """
        return {
            "amount": self.amount,
            "currency": self.currency,
            "hooks": self.hooks.to_dict(),
            "idempotencyKey": self.idempotency_key,
            "source": self.source,
            "token": self.token
        }
