"""
storing abstraction.
"""
import abc

from apps.abc.params import cards
from apps.abc.params import payment


class CardProcessorABC(abc.ABC):
    """
    card processing abstraction.
    """
    @abc.abstractmethod
    def create_card(self, cards: cards.CardInfo) -> None:
        """
        create a new card with draft status.
        """
        raise NotImplementedError("method should have implement in subclass")

    @abc.abstractmethod
    def update_card(self, card_params: cards.CardInfo) -> None:
        """"
        update card information in database.
        """
        raise NotImplementedError("method should have implement in subclass")

    @abc.abstractmethod
    def deactivate_card(self, card_params: cards.CardInfo) -> None:
        """
        deactivate the card
        """
        raise NotImplementedError("method should have implement in subclass")


class PaymentProcessorABC(abc.ABC):
    """
    payment processor abstraction.
    """
    @abc.abstractmethod
    def store_payment(self, payment: payment.Payment) -> None:
        """
        create a new payment in database.
        """
        raise NotImplementedError("method should have implement in subclass")
