from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from src.models.base_model import Base


class UserOrderItem(Base):
    __tablename__ = 'user_order_item'

    id = Column(VARCHAR(200), primary_key=True, nullable=False, index=True)
    order_id = Column(VARCHAR(200), ForeignKey('user_order.id'), nullable=False)
    product_id = Column(VARCHAR(200), ForeignKey('product.id'), nullable=False)
    quantity = Column(INTEGER, default=0, nullable=False)
    price = Column(DECIMAL(9, 2), nullable=False, default=0.0)

    order_id_item = relationship("UserOrder")
    product_item = relationship("Product")
