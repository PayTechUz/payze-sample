"""
cards params abstractions
"""
import typing
import pydantic

from apps.abc.params.payment import Payment


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


class CardInfo(pydantic.BaseModel):
    """
    create cards abstract class
    """
    token: str
    holder: str = None
    card_entity_type: str = None
    number: typing.Optional[str] = None
    payer: typing.Optional[Payer] = None
    expire_date: typing.Optional[str] = None
    card_brand: typing.Optional[str] = None
    payment: typing.Optional[Payment] = None
