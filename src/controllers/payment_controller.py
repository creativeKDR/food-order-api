from typing import List, Any

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from src.core.db import get_db
from src.schemas.payment_schema import PaymentCreate, PaymentUpdate, PaymentResponse
from src.services.payment_service import PaymentService, getPaymentInstance

router = APIRouter(tags=["payment-endpoints"])


@router.get(include_in_schema=True, path="/payment", status_code=200, response_model=List[PaymentResponse])
def get_payment(payment_service: PaymentService = Depends(getPaymentInstance), db: Session = Depends(get_db)) -> Any:
    response = payment_service.get_payment(db=db)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.post(include_in_schema=True, path="/payment", status_code=200, response_model=PaymentResponse)
def create_payment(payment_obj: PaymentCreate, payment_service: PaymentService = Depends(getPaymentInstance),
                   db: Session = Depends(get_db)) -> Any:
    response = payment_service.create_payment(db=db, payment_obj=payment_obj)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Payment not created')

    return response


@router.get(include_in_schema=True, path="/payment/order/{order_id}", status_code=200, response_model=PaymentResponse)
def get_payment_by_order_id(order_id: str, payment_service: PaymentService = Depends(getPaymentInstance),
                            db: Session = Depends(get_db)) -> Any:
    response = payment_service.get_payment_by_order_id(db=db, order_id=order_id)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.put(include_in_schema=True, path="/payment/{payment_id}", status_code=200, response_model=PaymentResponse)
def update_payment(payment_id: str, payment_obj: PaymentUpdate,
                   payment_service: PaymentService = Depends(getPaymentInstance), db: Session = Depends(get_db)) -> Any:
    response = payment_service.update_payment(db=db, payment_obj=payment_obj, payment_id=payment_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Payment not updated')

    return response


@router.delete(include_in_schema=True, path="/payment/{payment_id}", status_code=200)
def delete_payment(payment_id: str, payment_service: PaymentService = Depends(getPaymentInstance),
                   db: Session = Depends(get_db)) -> Any:
    response = payment_service.delete_payment(db=db, payment_id=payment_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Payment not updated')

    return Response(status_code=status.HTTP_204_NO_CONTENT, content='Payment deleted successfully')
