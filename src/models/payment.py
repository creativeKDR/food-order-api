import datetime

from sqlalchemy import Column, VARCHAR, TIMESTAMP, DECIMAL, INTEGER, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.models.base_model import Base


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(VARCHAR(200), primary_key=True, nullable=False, index=True)
    order_id = Column(VARCHAR(200), ForeignKey('user_order.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    amount = Column(DECIMAL(9, 2), nullable=False, default=0.0)
    payment_method = Column(INTEGER, ForeignKey('payment_method.id'), nullable=False)
    status = Column(INTEGER, ForeignKey('status.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())

    payment_payment_method = relationship('PaymentMethod')
    payment_status = relationship('Status')
