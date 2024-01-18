"""
create payment params abstractions
"""
import pydantic


class CreatePayment(pydantic.BaseModel):
    """
    get token abstraction fields.
    """
    token: str
    amount: int
