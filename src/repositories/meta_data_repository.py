from sqlalchemy.orm import Session

from src.models.category import Category
from src.models.order_type import OrderType
from src.models.payment_method import PaymentMethod
from src.models.status import Status


class MetaDataRepository:

    @staticmethod
    def get_category(db: Session):
        return db.query(Category).all()

    @staticmethod
    def get_status(db: Session):
        return db.query(Status).all()

    @staticmethod
    def get_order_type(db: Session):
        return db.query(OrderType).all()

    @staticmethod
    def get_payment_method(db: Session):
        return db.query(PaymentMethod).all()
