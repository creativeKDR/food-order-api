from datetime import datetime
from typing import Union, List
from uuid import UUID

from pydantic import BaseModel, Field


class UserOrderItemResponse(BaseModel):
    id: Union[str, UUID] = Field(None, alias='id')
    order_id: Union[str, UUID] = Field(None, alias='order_id')
    product_id: Union[str, UUID] = Field(None, alias='product_id')
    quantity: int = Field(None, alias='quantity')
    price: float = Field(None, alias='price')

    class Config:
        orm_mode = True


class UserOrderItemCreate(BaseModel):
    id: Union[str, UUID] = Field(None)
    order_id: Union[str, UUID] = Field(None)
    product_id: int = Field(None)
    quantity: int = Field(None)
    price: float = Field(None)

    class Config:
        orm_mode = True


class UserOrderItemUpdate(UserOrderItemResponse):
    class Config:
        fields = {
            "id": {"exclude": True},
        }


class UserOrderResponse(BaseModel):
    id: Union[str, UUID] = Field(None, alias='id')
    user_id: Union[str, UUID] = Field(None, alias='user_id')
    order_date: datetime = Field(None, alias='order_date')
    total_price: float = Field(None, alias='total_price')
    discount_price: float = Field(None, alias='discount_price')
    status: int = Field(None, alias='status')
    order_type: int = Field(None, alias='order_type')

    class Config:
        orm_mode = True


class UserOrderCreate(BaseModel):
    id: Union[str, UUID] = Field(None, alias='id')
    user_id: Union[str, UUID] = Field(None, alias='user_id')
    order_date: datetime = Field(None, alias='order_date')
    total_price: float = Field(None, alias='total_price')
    discount_price: float = Field(None, alias='discount_price')
    status: int = Field(None, alias='status')
    order_type: int = Field(None, alias='order_type')
    items: List[UserOrderItemCreate]

    class Config:
        orm_mode = True


class UserOrderUpdate(UserOrderResponse):
    class Config:
        fields = {
            "id": {"exclude": True},
        }
