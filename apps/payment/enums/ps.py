"""
payment statuses enumeration.
"""
from enum import Enum


class Status(Enum):
    """
    payment status
    """
    PENDING = 'Pending'
    SUCCESS = 'Succeeded'
    REJECTED = 'Rejected'
