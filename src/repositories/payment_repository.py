from sqlalchemy.orm import Session

from src.models.payment import Payment
from src.repositories.base import CRUDBase


class PaymentRepository(CRUDBase):

    def __init__(self):
        super().__init__(Payment)

    def get_payment_by_order_id(self, db: Session, order_id: str):
        return db.query(Payment).filter(Payment.order_id == order_id).all()
