from sqlalchemy import Column, String, INTEGER

from src.models.base_model import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(INTEGER, autoincrement=True, primary_key=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    display_name = Column(String(100), nullable=False)
