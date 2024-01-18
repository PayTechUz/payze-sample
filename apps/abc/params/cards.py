"""
cards params abstractions
"""
import typing
import pydantic


class GetToken(pydantic.BaseModel):
    """
    get token abstraction fields.
    """


class Payer(pydantic.BaseModel):
    """
    payer information.
    """
    phone: typing.Optional[str]
    full_name: typing.Optional[str]


class CardVeryPayments(pydantic.BaseModel):
    """
    card very payments
    """
    payment_id: str
    idempotency_key: str
    currency: str
    amount: float
    payment_status: str
    final_amount: typing.Optional[float]


class CardInfo(pydantic.BaseModel):
    """
    create cards abstract class
    """
    token: str
    number: str = None
    expire_date: str = None
    holder: str = None
    card_brand: str = None
    card_entity_type: str = None
    verify_payments: typing.Optional[CardVeryPayments] = None
    payer: typing.Optional[Payer] = None
