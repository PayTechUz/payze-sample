"""
the application of interface.
"""
from typing import Any

from apps.abc import IApp
from apps.abc.params import cp
from apps.abc.params import cards
from apps.abc.params.payment import Payment
from apps.payment.enums import pt
from apps.payment.providers import init_provider

from apps.payment.providers.payze.processors.card import card_processor
from apps.payment.providers.payze.processors.payment import payment_processor


class App(IApp):
    """
    implementation of interfaces.
    """
    def __init__(self):
        self.provider = init_provider(
            provider_type=pt.ProviderTypes.PAYZE.value
        )

    def get_token(self, _: cards.GetToken = None) -> Any:
        return self.provider.get_token()

    def create_payment(self, req_params: cp.CreatePayment) -> Any:
        self.provider.create_payment(
            req_params=req_params
        )

    def check_status(self, req_params: Any) -> Any:
        return super().check_status(req_params)

    def create_card(self, cards: cards.CardInfo) -> None:
        card_processor.create_card(
            cards=cards
        )

    def update_card(self, card_params: Any) -> Any:
        card_processor.update_card(
            card_params=card_params
        )

    def deactivate_card(self, card_params: Any) -> Any:
        card_processor.deactivate_card(
            card_params=card_params
        )

    def store_payment(self, payment: Payment) -> None:
        payment_processor.store_payment(
            payment=payment
        )


app_context = App()
