from sqlalchemy.orm import Session

from src.models.user_order_item import UserOrderItem
from src.repositories.base import CRUDBase


class UserOrderItemRepository(CRUDBase):

    def __init__(self):
        super().__init__(UserOrderItem)

    def get_user_order_item(self, db: Session, order_id: str):
        return db.query(UserOrderItem).filter(UserOrderItem.order_id == order_id).all()
