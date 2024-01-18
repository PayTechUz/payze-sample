from dataclasses import dataclass

from apps.payment.providers.payze.params import request as payze_request


@dataclass
class PayzeOPS:
    """
    payze options.
    url: string -> the payze api endpoint url
    auth_token: string -> the payze auth token
    hooks: list of payze hooks.
    timeout: int -> timeout in seconds
    """
    url: str
    auth_token: str
    hooks: payze_request.Hooks
    timeout: str = 10
