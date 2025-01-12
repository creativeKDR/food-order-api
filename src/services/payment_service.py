from sqlalchemy.orm import Session

from src.repositories.payment_repository import PaymentRepository
from src.schemas.payment_schema import PaymentCreate, PaymentUpdate
from src.utils.utilities import Utilities


def getPaymentInstance():
    return PaymentService(repository=PaymentRepository())


class PaymentService:

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def get_payment(self, db: Session):
        return self.repository.getAll(db=db)

    def get_payment_by_order_id(self, db: Session, order_id: str):
        return self.repository.get_payment_by_order_id(db=db, order_id=order_id)

    def create_payment(self, db: Session, payment_obj: PaymentCreate):
        payment_obj = self.prepare_save_object(payment_obj)
        return self.repository.create(db=db, obj_in=payment_obj)

    def update_payment(self, db: Session, payment_obj: PaymentUpdate, payment_id: str):
        return self.repository.update(db=db, obj_in=payment_obj, id=payment_id)

    def delete_payment(self, db: Session, payment_id: str):
        return self.repository.remove(db=db, id=payment_id)

    @classmethod
    def prepare_save_object(cls, obj):
        obj.id = Utilities.generateUUID()
        return obj
