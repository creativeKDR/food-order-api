from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def create_db_and_tables():
#     Base.metadata.create_all(engine)
#
#
# def destroy_db_and_tables():
#     Base.metadata.drop_all(bind=engine, tables=[User.__table__, Blog.__table__])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
