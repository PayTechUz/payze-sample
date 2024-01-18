"""
the payze client.
"""
import json
import logging

from typing import Any
from requests import Session, Response

from payze.settings import payze

from apps.abc import provider
from apps.abc.params import cp
from apps.abc.params import cards
from apps.payment.providers.payze.params import ops
from apps.payment.providers.payze.params import request as payze_req
from apps.payment.providers.payze.params import response as payze_res
from apps.payment.providers.payze.decorators.error_catcher import error_catcher


logger = logging.getLogger(__name__)


class Payze(provider.Provider):
    """
    payze client implementation.
    """
    def __init__(self, ops: ops.PayzeOPS):
        self.url = ops.url
        self.hooks = ops.hooks
        self.timeout = ops.timeout
        self.session = Session()
        self.session.headers.update({
            "Authorization": ops.auth_token,
            "Content-Type": "application/json"
        })

    @error_catcher
    def __send_request(self, url: str, req_data: str, method: str) -> Any:
        resp_data: Response = self.session.request(
            method=method,
            url=url,
            timeout=self.timeout,
            data=req_data,
        )
        resp_data.raise_for_status()
        return resp_data.json()

    def _handle_response(
        self,
        resp_data: dict,
        resp_class: Any
    ) -> Any:
        return resp_class(**resp_data)

    def get_token(
        self,
        req_params: cards.GetToken = None
    ) -> payze_res.GetToken:
        url = f"{self.url}/v2/api/payment"

        req_params = payze_req.GetToken()
        req_params.hooks = self.hooks

        req_data = json.dumps(req_params.to_dict())
        resp_data = self.__send_request(url, req_data, "PUT")

        return self._handle_response(resp_data, payze_res.GetToken)

    def create_payment(
        self,
        req_params: cp.CreatePayment
    ) -> payze_res.CreatePayment:

        url = f"{self.url}/v2/api/payment"
        req_params = payze_req.CreatePayment(
            token=req_params.token,
            amount=req_params.amount
        )
        req_params.hooks = self.hooks

        req_data = json.dumps(req_params.to_dict())
        resp_data = self.__send_request(url, req_data, "PUT")

        return self._handle_response(resp_data, payze_res.CreatePayment)

    def check_status(self, req_params: Any) -> Any:
        return super().check_status(req_params)


payze = Payze(
    ops=ops.PayzeOPS(
        url=payze.PAYZE.get("url"),
        auth_token=payze.PAYZE.get("auth_token"),
        hooks=payze_req.Hooks(
            **payze.PAYZE.get("hooks")
        )
    )
)
