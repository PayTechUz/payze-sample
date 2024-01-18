"""
payze types enumeration
"""
from enum import Enum


class Type(Enum):
    """
    the payment types of payze
    """
    ADD_CARD = "AddCard"
    PAY_WITH_CARD = "PayWithCard"
