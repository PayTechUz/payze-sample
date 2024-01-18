"""
initialize providers.
"""
from apps.abc import provider
from apps.payment.enums import pt

from apps.payment.providers.payze.client import payze as payze_client


def init_provider(provider_type: pt.ProviderTypes) -> provider.Provider:
    """
    init providers with using factory design pattern.
    """
    if provider_type == pt.ProviderTypes.PAYZE.value:
        return payze_client

    raise NotImplementedError("provider type not supported")
