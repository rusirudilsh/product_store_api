from fastapi import APIRouter
from .product_route import product_router
from .category_route import category_router
from .product_order_route import order_router


main_api_router = APIRouter()


main_api_router.include_router(product_router, prefix="/product", tags=["product"])
main_api_router.include_router(category_router, prefix="/category", tags=["category"])
main_api_router.include_router(order_router, prefix="/order", tags=["order"])


@main_api_router.get("/")
async def root():
    return {"message": "Welcome to Product Store API"}