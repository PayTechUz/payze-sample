"""
storing abstraction.
"""
import abc
import typing

from apps.abc.params import cards


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
    def update_card(self, card_params: cards.CardInfo) -> typing.Any:
        """"
        update card information in database.
        """
        raise NotImplementedError("method should have implement in subclass")

    @abc.abstractmethod
    def deactivate_card(self, card_params: typing.Any) -> typing.Any:
        """
        deactivate the card
        """
        raise NotImplementedError("method should have implement in subclass")
