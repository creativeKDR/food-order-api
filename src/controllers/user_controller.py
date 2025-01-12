from typing import List, Any

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from src.core.db import get_db
from src.schemas.user_schema import UserResponse, UserCreate, UserUpdate
from src.services.user_service import UserService, getUserInstance

router = APIRouter(tags=["user-endpoints"])


@router.get(include_in_schema=True, path="/user", status_code=200, response_model=List[UserResponse])
def get_user(user_service: UserService = Depends(getUserInstance), db: Session = Depends(get_db)) -> Any:
    response = user_service.get_user(db=db)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.post(include_in_schema=True, path="/user", status_code=200, response_model=UserResponse)
def create_user(user_obj: UserCreate, user_service: UserService = Depends(getUserInstance),
                db: Session = Depends(get_db)) -> Any:
    response = user_service.create_user(db=db, user_obj=user_obj)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User not created')

    return response


@router.get(include_in_schema=True, path="/user/{user_id}", status_code=200, response_model=UserResponse)
def get_user_by_user_id(user_id: str, user_service: UserService = Depends(getUserInstance),
                        db: Session = Depends(get_db)) -> Any:
    response = user_service.get_user_by_id(db=db, user_id=user_id)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.put(include_in_schema=True, path="/user/{user_id}", status_code=200, response_model=UserResponse)
def update_user(user_id: str, user_obj: UserUpdate, user_service: UserService = Depends(getUserInstance),
                db: Session = Depends(get_db)) -> Any:
    response = user_service.update_user(db=db, user_obj=user_obj, user_id=user_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User not updated')

    return response


@router.delete(include_in_schema=True, path="/user/{user_id}", status_code=200)
def delete_user(user_id: str, user_service: UserService = Depends(getUserInstance),
                db: Session = Depends(get_db)) -> Any:
    response = user_service.delete_user(db=db, user_id=user_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User not updated')

    return Response(status_code=status.HTTP_204_NO_CONTENT)
