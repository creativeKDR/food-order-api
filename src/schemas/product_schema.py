from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field


class ProductResponse(BaseModel):
    id: Union[str, UUID] = Field(None, alias='id')
    name: str = Field(None, alias='name')
    description: str = Field(None, alias='description')
    price: float = Field(None, alias='price')
    discount_price: float = Field(None, alias='discount_price')
    quantity: int = Field(None, alias='quantity')
    category: int = Field(None, alias='category')
    image_url: str = Field(None, alias='image_url')
    is_available: bool = Field(None, alias='is_available')

    class Config:
        orm_mode = True


class ProductCreate(ProductResponse):
    pass


class ProductUpdate(ProductResponse):
    class Config:
        fields = {
            "id": {"exclude": True},
        }
