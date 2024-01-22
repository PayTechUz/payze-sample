"""
payment abstract params
"""
import typing
import pydantic


class Payment(pydantic.BaseModel):
    """
    card very payments
    """
    payment_id: str
    order_id: str
    token: typing.Optional[str] = None
    amount: typing.Optional[float] = None
    currency: typing.Optional[str] = None
    commission: typing.Optional[float] = None
    payment_status: typing.Optional[str] = None
    final_amount: typing.Optional[float] = None
    idempotency_key: typing.Optional[str] = None
