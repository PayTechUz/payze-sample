"""
the payment reasons.
"""
from enum import Enum


class PaymentMethods(Enum):
    """
    payment methods.
    p2p: per-to-per
    a2c: account-to-card
    c2a: card-to-account
    """
    P2P = 1
    A2C = 2
    C2A = 3


class PaymentReason(Enum):
    """
    the payment reasons
    """
    ORDER = 1
    DEBT = 2
    TIP = 3
    CARD_VERIFY = 4
