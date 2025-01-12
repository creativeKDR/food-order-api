from typing import List, Any

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from src.core.db import get_db
from src.schemas.user_order_schema import UserOrderResponse, UserOrderCreate, UserOrderUpdate
from src.services.user_order_service import UserOrderService, getUserOrderInstance

router = APIRouter(tags=["user-order-endpoints"])


@router.get(include_in_schema=True, path="/order/user/{user_id}", status_code=200,
            response_model=List[UserOrderResponse])
def get_user_order(user_id: str, order_service: UserOrderService = Depends(getUserOrderInstance),
                   db: Session = Depends(get_db)) -> Any:
    response = order_service.get_order_by_user_id(db=db, user_id=user_id)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.post(include_in_schema=True, path="/order", status_code=200, response_model=UserOrderResponse)
def create_user_order(order_obj: UserOrderCreate, order_service: UserOrderService = Depends(getUserOrderInstance),
                      db: Session = Depends(get_db)) -> Any:
    response = order_service.create_user_order(db=db, order_obj=order_obj)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Order not created')

    return response


@router.get(include_in_schema=True, path="/order/{order_id}", status_code=200, response_model=UserOrderResponse)
def get_order_by_order_id(order_id: str, order_service: UserOrderService = Depends(getUserOrderInstance),
                          db: Session = Depends(get_db)) -> Any:
    response = order_service.get_order_by_id(db=db, order_id=order_id)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.put(include_in_schema=True, path="/order/{order_id}", status_code=200, response_model=UserOrderResponse)
def update_user_order(order_id: str, order_obj: UserOrderUpdate,
                      order_service: UserOrderService = Depends(getUserOrderInstance),
                      db: Session = Depends(get_db)) -> Any:
    response = order_service.update_user_order(db=db, order_obj=order_obj, order_id=order_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Order not updated')

    return response


@router.delete(include_in_schema=True, path="/order/{order_id}", status_code=200)
def delete_user_order(order_id: str, order_service: UserOrderService = Depends(getUserOrderInstance),
                      db: Session = Depends(get_db)) -> Any:
    response = order_service.delete_user_order(db=db, order_id=order_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Order not updated')

    return Response(status_code=status.HTTP_204_NO_CONTENT, content='Order deleted successfully')
