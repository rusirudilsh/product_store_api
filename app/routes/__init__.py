from fastapi import APIRouter
from .product_route import product_router
from .category_route import category_router
from .product_order_route import order_router


main_api_router = APIRouter()


main_api_router.include_router(product_router, prefix="/products", tags=["products"])
main_api_router.include_router(category_router, prefix="/categories", tags=["categories"])
main_api_router.include_router(order_router, prefix="/orders", tags=["orders"])


@main_api_router.get("/")
async def root():
    return {"message": "Welcome to Product Store API"}