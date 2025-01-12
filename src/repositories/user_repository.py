from src.models.user import User
from src.repositories.base import CRUDBase


class UserRepository(CRUDBase):
    def __init__(self):
        super().__init__(User)

    pass
