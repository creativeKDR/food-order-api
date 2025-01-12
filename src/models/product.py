import datetime

from sqlalchemy import Column, VARCHAR, String, BOOLEAN, TIMESTAMP, TEXT, DECIMAL, INTEGER, ForeignKey
from sqlalchemy.orm import relationship

from src.models.base_model import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(VARCHAR(200), primary_key=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    description = Column(TEXT, nullable=True)
    price = Column(DECIMAL(9, 2), nullable=False, default=0.0)
    discount_price = Column(DECIMAL(9, 2), nullable=True, default=0.0)
    quantity = Column(INTEGER, default=0, nullable=False)
    category = Column(INTEGER, ForeignKey('category.id'), nullable=False)
    image_url = Column(String(200), nullable=False)
    is_available = Column(BOOLEAN, default=None)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())

    category_product = relationship('Category')
