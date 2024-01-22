"""
applications of interfaces.
"""
from apps.abc import storage
from apps.abc import provider


class IApp(
    provider.Provider,
    storage.CardProcessorABC,
    storage.PaymentProcessorABC,
):
    """
    whole interfaces of target application.
    """
