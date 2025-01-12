from sqlalchemy.orm import Session

from src.repositories.product_repository import ProductRepository
from src.schemas.product_schema import ProductCreate, ProductUpdate
from src.utils.utilities import Utilities


def getProductInstance():
    return ProductService(repository=ProductRepository())


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_product(self, db: Session):
        return self.repository.getAll(db=db)

    def get_product_by_id(self, db: Session, product_id: str):
        return self.repository.get(db=db, id=product_id)

    def create_product(self, db: Session, product_obj: ProductCreate):
        product_obj = self.prepare_save_object(product_obj)
        return self.repository.create(db=db, obj_in=product_obj)

    def update_product(self, db: Session, product_obj: ProductUpdate, product_id: str):
        return self.repository.update(db=db, obj_in=product_obj, id=product_id)

    def delete_product(self, db: Session, product_id: str):
        return self.repository.remove(db=db, id=product_id)

    @classmethod
    def prepare_save_object(cls, obj):
        obj.id = Utilities.generateUUID()
        return obj
