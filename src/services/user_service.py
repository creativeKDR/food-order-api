from sqlalchemy.orm import Session

from src.repositories.user_repository import UserRepository
from src.schemas.user_schema import UserCreate, UserUpdate
from src.utils.utilities import Utilities


def getUserInstance():
    return UserService(repository=UserRepository())


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user(self, db: Session):
        return self.repository.getAll(db=db)

    def get_user_by_id(self, db: Session, user_id: str):
        return self.repository.get(db=db, id=user_id)

    def create_user(self, db: Session, user_obj: UserCreate):
        user_obj = self.prepare_save_object(user_obj)
        return self.repository.create(db=db, obj_in=user_obj)

    def update_user(self, db: Session, user_obj: UserUpdate, user_id: str):
        return self.repository.update(db=db, obj_in=user_obj, id=user_id)

    def delete_user(self, db: Session, user_id: str):
        return self.repository.remove(db=db, id=user_id)

    @classmethod
    def prepare_save_object(cls, obj):
        obj.id = Utilities.generateUUID()
        obj.password = ''  # need to add password encryption
        obj.is_admin = False
        return obj
