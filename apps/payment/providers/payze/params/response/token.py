import pydantic


class CardPayment(pydantic.BaseModel):
    """
    card payment response model.
    """
    token: str


class Payment(pydantic.BaseModel):
    """
    the payment response model.
    """
    type: str
    source: str
    amount: int
    status: str
    transaction_id: str = pydantic.Field(alias="transactionId")
    card_payment: CardPayment = pydantic.Field(alias="cardPayment")
    payment_url: pydantic.HttpUrl = pydantic.Field(alias="paymentUrl")


class RespData(pydantic.BaseModel):
    """
    the get token response model.
    """
    payment: Payment


class GetToken(pydantic.BaseModel):
    """
    the get token response model.
    """
    data: RespData
