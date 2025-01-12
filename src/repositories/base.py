from typing import Any, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.models.base_model import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def getAll(self, db: Session) -> List[Optional[ModelType]]:
        return db.query(self.model).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def multi_create(self, db: Session, *, obj_in: List[CreateSchemaType]) -> ModelType:
        create_data = []
        for obj_in_data in obj_in:
            db_obj = self.model(**(jsonable_encoder(obj_in_data)))
            create_data.append(db_obj)
        db.bulk_save_objects(create_data)
        db.commit()
        return create_data

    def update(self, db: Session, id: any, *, obj_in: Union[UpdateSchemaType]) -> ModelType:
        update_data = jsonable_encoder(obj_in)
        db.query(self.model).filter(self.model.id == id).update(update_data)
        db.commit()
        return db.query(self.model).filter(self.model.id == id).first()

    def remove(self, db: Session, *, id: str) -> ModelType:
        db_obj = db.query(self.model).filter(self.model.id == id).first()
        if db_obj is not None:
            db.delete(db_obj)
            db.commit()
        return db_obj
