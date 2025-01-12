from typing import List, Any

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from src.core.db import get_db
from src.schemas.product_schema import ProductResponse, ProductCreate, ProductUpdate
from src.services.product_service import ProductService, getProductInstance

router = APIRouter(tags=["product-endpoints"])


@router.get(include_in_schema=True, path="/product", status_code=200, response_model=List[ProductResponse])
def get_product(product_service: ProductService = Depends(getProductInstance), db: Session = Depends(get_db)) -> Any:
    response = product_service.get_product(db=db)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.post(include_in_schema=True, path="/product", status_code=200, response_model=ProductResponse)
def create_product(product_obj: ProductCreate, product_service: ProductService = Depends(getProductInstance),
                   db: Session = Depends(get_db)) -> Any:
    response = product_service.create_product(db=db, product_obj=product_obj)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Product not created')

    return response


@router.get(include_in_schema=True, path="/product/{product_id}", status_code=200, response_model=ProductResponse)
def get_product_by_product_id(product_id: str, product_service: ProductService = Depends(getProductInstance),
                              db: Session = Depends(get_db)) -> Any:
    response = product_service.get_product_by_id(db=db, product_id=product_id)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.put(include_in_schema=True, path="/product/{product_id}", status_code=200, response_model=ProductResponse)
def update_product(product_id: str, product_obj: ProductUpdate,
                   product_service: ProductService = Depends(getProductInstance),
                   db: Session = Depends(get_db)) -> Any:
    response = product_service.update_product(db=db, product_obj=product_obj, product_id=product_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Product not updated')

    return response


@router.delete(include_in_schema=True, path="/product/{product_id}", status_code=200)
def delete_product(product_id: str, product_service: ProductService = Depends(getProductInstance),
                   db: Session = Depends(get_db)) -> Any:
    response = product_service.delete_product(db=db, product_id=product_id)
    if not response:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Product not updated')

    return Response(status_code=status.HTTP_204_NO_CONTENT, content='Product deleted successfully')
