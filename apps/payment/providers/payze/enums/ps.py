"""
the payment status enumeration
"""
from enum import Enum


class PaymentStatus(Enum):
    """
    the payment status enumeration.
    """
    DRAFT = "Draft"
    CAPTURED = "Captured"
    REJECTED = "Rejected"
    REFUNDED = "Refunded"
    PARTIALLYREFUNDED = "PartiallyRefunded"
