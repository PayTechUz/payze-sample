"""
initialize payze views.
"""
from .hooks.card import CardsWebHooksAPIView # noqa
from .hooks.cp import CreatePaymentAPIView # noqa
from .cards.token import TokenAPIView # noqa
