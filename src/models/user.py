import datetime

from sqlalchemy import Column, VARCHAR, String, Unicode, BOOLEAN, TIMESTAMP

from src.models.base_model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(VARCHAR(200), primary_key=True, nullable=False, index=True)
    user_name = Column(String(100), nullable=False)
    email = Column(Unicode(100), nullable=False, unique=True)
    password = Column(Unicode(100), nullable=False)
    phone_number = Column(String(100), nullable=False)
    is_admin = Column(BOOLEAN, default=None)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())

