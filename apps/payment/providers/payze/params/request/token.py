"""
the token requests params
"""
import uuid
import pydantic

from apps.abc.params import cards
from apps.payment.providers.payze.params.request import base


class CardPayment(pydantic.BaseModel):
    """
    card payment model.
    """
    tokenize_card: bool = True

    def to_dict(self):
        """
        the dict representation.
        """
        return {
            "tokenizeCard": self.tokenize_card,
        }


class GetToken(cards.GetToken):
    """
    get token request model.
    """
    amount: int = 0
    currency: str = "UZS"
    language: str = "UZ"
    source: str = "Card"
    hooks: base.Hooks = None
    card_payment: CardPayment = CardPayment()
    idempotency_key: str = None

    def to_dict(self):
        """
        the dict representation.
        """
        if self.idempotency_key is None:
            self.idempotency_key = str(uuid.uuid4())

        return {
            "amount": self.amount,
            "currency": self.currency,
            "hooks": self.hooks.to_dict(),
            "idempotencyKey": self.idempotency_key,
            "source": self.source,
            "cardPayment": self.card_payment.to_dict(),
        }
