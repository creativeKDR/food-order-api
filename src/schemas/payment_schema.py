from datetime import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field


class PaymentResponse(BaseModel):
    id: Union[str, UUID] = Field(None, alias='id')
    order_id: Union[str, UUID] = Field(None, alias='order_id')
    order_date: datetime = Field(None, alias='order_date')
    amount: float = Field(None, alias='amount')
    payment_method: int = Field(None, alias='payment_method')
    status: int = Field(None, alias='status')

    class Config:
        orm_mode = True


class PaymentCreate(PaymentResponse):
    pass


class PaymentUpdate(PaymentResponse):
    class Config:
        fields = {
            "id": {"exclude": True},
        }
