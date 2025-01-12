import datetime

from sqlalchemy import Column, VARCHAR, INTEGER, TIMESTAMP, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship

from src.models.base_model import Base


class UserOrder(Base):
    __tablename__ = 'user_order'

    id = Column(VARCHAR(200), primary_key=True, nullable=False, index=True)
    user_id = Column(VARCHAR(200), ForeignKey('user.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total_price = Column(DECIMAL(9, 2), nullable=False, default=0.0)
    discount_price = Column(DECIMAL(9, 2), nullable=True, default=0.0)
    status = Column(INTEGER, ForeignKey('status.id'), nullable=False)
    order_type = Column(INTEGER, ForeignKey('order_type.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())

    user_order = relationship("User")
    status_order = relationship("Status")
    order_type_order = relationship("OrderType")
