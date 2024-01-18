"""
provider abstractions
"""
import abc
import typing

from apps.abc.params import cp
from apps.abc.params import cards


class Provider(abc.ABC):
    """
    provider abstractions.
    """
    @abc.abstractmethod
    def get_token(self, req_params: cards.GetToken = None) -> typing.Any:
        """
        get token from provider side, that returns the token and payment url
            for activate the given token.
        """
        raise NotImplementedError("method should have implement in subclass")

    @abc.abstractmethod
    def create_payment(self, req_params: cp.CreatePayment) -> typing.Any:
        """
        create payment with draft status, with using activated token,
        """
        raise NotImplementedError("method should have implement in subclass")

    @abc.abstractmethod
    def check_status(self, req_params: typing.Any) -> typing.Any:
        """
        check the status of the payment method.
        """
        raise NotImplementedError("method should have implement in subclass")
