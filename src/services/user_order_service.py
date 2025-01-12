from sqlalchemy.orm import Session

from src.repositories.user_order_item_repository import UserOrderItemRepository
from src.repositories.user_order_repository import UserOrderRepository
from src.schemas.user_order_schema import UserOrderCreate, UserOrderUpdate, UserOrderItemCreate
from src.utils.utilities import Utilities


def getUserOrderInstance():
    return UserOrderService(repository=UserOrderRepository(), itemRepository=UserOrderItemRepository())


class UserOrderService:

    def __init__(self, repository: UserOrderRepository, itemRepository: UserOrderItemRepository):
        self.repository = repository
        self.itemRepository = itemRepository

    def get_order_by_user_id(self, db: Session, user_id: str):
        return self.repository.get_user_order(db=db, user_id=user_id)

    def get_order_by_id(self, db: Session, order_id: str):
        return self.repository.get(db=db, id=order_id)

    def create_user_order(self, db: Session, order_obj: UserOrderCreate):
        order_obj, item_obj_list = self.prepare_save_object(order_obj)
        order_data = self.repository.create(db=db, obj_in=order_obj)
        if order_data:
            self.itemRepository.multi_create(db=db,obj_in=item_obj_list)
        return order_data

    def update_user_order(self, db: Session, order_obj: UserOrderUpdate, order_id: str):
        return self.repository.update(db=db, obj_in=order_obj, id=order_id)

    def delete_user_order(self, db: Session, order_id: str):
        return self.repository.remove(db=db, id=order_id)

    @classmethod
    def prepare_save_object(cls, obj):
        order_items = obj.items
        del obj.items
        obj.id = Utilities.generateUUID()
        obj.status = ''  # need to add status enum

        order_item_list = []
        for items in order_items:
            item_obj = UserOrderItemCreate(
                id=Utilities.generateUUID(), order_id=obj.id, product_id=items.product_id, price=items.price,
                quantity=items.quantity
            )
            order_item_list.append(item_obj)
        return obj, order_item_list
