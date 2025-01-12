from typing import List, Any

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.core.db import get_db
from src.schemas.metadata_schema import MetaDataResponse
from src.services.meta_data_service import MetaDataService, getMetaDataInstance

router = APIRouter(prefix='/metadata', tags=["metadata-endpoints"])


@router.get(include_in_schema=True, path="/category", status_code=200, response_model=List[MetaDataResponse])
def get_category(metadata_service: MetaDataService = Depends(getMetaDataInstance), db: Session = Depends(get_db)) -> Any:
    response = metadata_service.get_category(db=db)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.get(include_in_schema=True, path="/status", status_code=200, response_model=List[MetaDataResponse])
def get_status(metadata_service: MetaDataService = Depends(getMetaDataInstance), db: Session = Depends(get_db)) -> Any:
    response = metadata_service.get_status(db=db)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.get(include_in_schema=True, path="/payment-method", status_code=200, response_model=List[MetaDataResponse])
def get_payment_method(metadata_service: MetaDataService = Depends(getMetaDataInstance),
                       db: Session = Depends(get_db)) -> Any:
    response = metadata_service.get_payment_method(db=db)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response


@router.get(include_in_schema=True, path="/order-type", status_code=200, response_model=List[MetaDataResponse])
def get_order_type(metadata_service: MetaDataService = Depends(getMetaDataInstance), db: Session = Depends(get_db)) -> Any:
    response = metadata_service.get_order_type(db=db)
    if not response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return response
