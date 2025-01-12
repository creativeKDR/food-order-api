from sqlalchemy.orm import Session

from src.models.user_order import UserOrder
from src.repositories.base import CRUDBase


class UserOrderRepository(CRUDBase):

    def __init__(self):
        super().__init__(UserOrder)

    def get_user_order(self, db: Session, user_id: str):
        return db.query(UserOrder).filter(UserOrder.user_id == user_id).all()
