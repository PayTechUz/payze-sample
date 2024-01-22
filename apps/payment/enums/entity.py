"""
the card entity types
"""
from enum import Enum


class CardOwnerEntityType(Enum):
    """
    card owner entity types.
    """
    PRIVATE = "Private"
    CORPORATE = "Corporate"
    UNKNOWN = "Unknown"
