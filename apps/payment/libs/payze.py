import json

import requests

from django.conf import settings
from django.db import DatabaseError

from apps.utility.logger import logger
from apps.order.models.order import Order
from apps.payment.models.transactions import Transactions
from apps.utility.exceptions import ServiceAPIException500


class Payze:
    def __init__(
        self,
        api_url: str,
        api_key: str,
        api_secret: str,
        call_back_url: str = None
    ) -> "Payze":
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.call_back_url = call_back_url
        self.headers = {
            "Content-Type": "application/json"
        }
        self.methods: dict = {
            "pay_with_card": "payWithCard"
        }

    def pay_with_card(
        self,
        amount: float,
        order: Order,
        card_token: str,
        hook_refound=True,
        currency = "USD"
    ) -> None:
        payload = json.dumps({
            "method": self.methods.get("pay_with_card"),
            "apiKey": self.api_key,
            "apiSecret": self.api_secret,
            "data": {
                "amount": amount,
                "currency": currency,
                "cardToken": card_token,
                "hookUrl": self.call_back_url,
                "hookRefund": hook_refound
            }
        })
        resp = requests.post(
            url=self.api_url,
            data=payload,
            headers=self.headers
        ).json()
        
        error = resp.get("response").get("error")
        transaction = resp.get("response").get("transactionInfo")

        if error != None:
            logger.error("error was occured while paying the order - {order} error - {error}".format(
                order=Order.id,
                error=error
            ))
            raise ServiceAPIException500()


        try:
            Transactions.objects.create(
                order=order,
                amount=amount,
                transaction_id=transaction.get("transactionId"),
                status=transaction.get("status"),
                transaction_info=transaction
            )
        
        except DatabaseError as error:
            logger.error("error was occurred while creating transaction in database: %s", error)
            raise ServiceAPIException500()

        return resp


payze = Payze(**settings.PAYZE)
