"""
payze withdrawl serializers.
"""
import typing
import pydantic


class ExtraAttribute(pydantic.BaseModel):
    """
    extra attributes.
    """
    key: str = pydantic.Field(alias="Key")
    value: str = pydantic.Field(alias="Value")
    description: str = pydantic.Field(
        alias="Description"
    )


class Metadata(pydantic.BaseModel):
    """
    meta data attributes.
    """
    extra_attribute: typing.List[ExtraAttribute] = pydantic.Field(
        alias="ExtraAttributes"
    )


class WithDrawlWebHookSerializer(pydantic.BaseModel):
    """
    withdraw serializer.
    """
    source: str = pydantic.Field(alias="Source")
    idempotency_key: str = pydantic.Field(alias="IdempotencyKey")
    payment_id: str = pydantic.Field(alias="PaymentId")
    type: str = pydantic.Field(alias="Type")
    payment_status: str = pydantic.Field(alias="PaymentStatus")
    amount: float = pydantic.Field(alias="Amount")
    currency: str = pydantic.Field(alias="Currency")
    final_amount: typing.Optional[float] = pydantic.Field(alias="FinalAmount")
    commission: typing.Optional[float] = pydantic.Field(alias="Commission")
    token: str = pydantic.Field(alias="Token")
    metadata: Metadata = pydantic.Field(alias="Metadata")
