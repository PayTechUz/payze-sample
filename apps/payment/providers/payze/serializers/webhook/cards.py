"""
cards web hook serializers.
"""
import typing
import pydantic


class Payer(pydantic.BaseModel):
    """
    payer information.
    """
    phone: typing.Optional[str] = pydantic.Field(
        alias="Phone",
    )
    full_name: typing.Optional[str] = pydantic.Field(
        alias="FullName"
    )


class CardsWebHookSerializers(pydantic.BaseModel):
    """
    the cards serializer.
    """
    type: str = \
        pydantic.Field(alias="Type")
    token: str = \
        pydantic.Field(alias="Token")
    source: str = \
        pydantic.Field(alias="Source")
    amount: float = \
        pydantic.Field(alias="Amount")
    currency: str = \
        pydantic.Field(alias="Currency")
    payment_id: str = \
        pydantic.Field(alias="PaymentId")
    payment_status: str = \
        pydantic.Field(alias="PaymentStatus")
    idempotency_key: str = \
        pydantic.Field(alias="IdempotencyKey")
    final_amount: typing.Optional[float] \
        = pydantic.Field(alias="FinalAmount")
    card_musk: typing.Optional[str] = \
        pydantic.Field(alias="CardMask")
    card_owner_entity_type: typing.Optional[str] = \
        pydantic.Field(alias="CardOwnerEntityType")
    card_brand: typing.Optional[str] = \
        pydantic.Field(alias="CardBrand")
    expire_date: typing.Optional[str] = \
        pydantic.Field(alias="ExpirationDate")
    payer: typing.Optional[Payer] = pydantic.Field(
        alias="Payer"
    )
