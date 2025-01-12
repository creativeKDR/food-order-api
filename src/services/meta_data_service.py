from sqlalchemy.orm import Session

from src.repositories.meta_data_repository import MetaDataRepository


def getMetaDataInstance():
    return MetaDataService(repository=MetaDataRepository())


class MetaDataService:

    def __init__(self, repository: MetaDataRepository):
        self.repository = repository

    def get_category(self, db: Session):
        return self.repository.get_category(db=db)

    def get_status(self, db: Session):
        return self.repository.get_status(db=db)

    def get_order_type(self, db: Session):
        return self.repository.get_order_type(db=db)

    def get_payment_method(self, db: Session):
        return self.repository.get_payment_method(db=db)
