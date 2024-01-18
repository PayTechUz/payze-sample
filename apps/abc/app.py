"""
applications of interfaces.
"""
from apps.abc import storage
from apps.abc import provider


class IApp(
    provider.Provider,
    storage.CardProcessorABC,
):
    """
    whole interfaces of target application.
    """
