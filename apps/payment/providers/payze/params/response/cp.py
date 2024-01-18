"""
create payment response models.
"""
import pydantic


class CardPayment(pydantic.BaseModel):
    """
    card payment model.
    """
    token: str


class Payment(pydantic.BaseModel):
    """
    payment model.
    """
    source: str
    type: str
    status: str
    amount: int
    idempotency_key: str = pydantic.Field(
        alias="idempotencyKey",
    )
    transaction_id: str = pydantic.Field(
        alias="transactionId",
    )
    card_payment: CardPayment = pydantic.Field(
        alias="cardPayment"
    )


class Data(pydantic.BaseModel):
    """
    response data model.
    """
    payment: Payment


class CreatePayment(pydantic.BaseModel):
    """
    create payment response model.
    """
    data: Data
