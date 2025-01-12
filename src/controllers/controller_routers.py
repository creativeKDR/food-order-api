from fastapi import APIRouter

from src.controllers import user_controller, user_order_controller, payment_controller, product_controller, meta_data_controller

api_router = APIRouter(prefix="/food-app/v1/api")

api_router.include_router(user_controller.router)
api_router.include_router(user_order_controller.router)
api_router.include_router(payment_controller.router)
api_router.include_router(product_controller.router)
api_router.include_router(meta_data_controller.router)
