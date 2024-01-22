"""
initialize payze views.
"""
from .hooks.card import CardsWebHooksAPIView # noqa
from .hooks.withdrawl import CreatePaymentAPIView # noqa
from .cards.token import TokenAPIView # noqa
