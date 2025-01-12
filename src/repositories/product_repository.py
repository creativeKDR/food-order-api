from src.models.product import Product
from src.repositories.base import CRUDBase


class ProductRepository(CRUDBase):

    def __init__(self):
        super().__init__(Product)

    pass
