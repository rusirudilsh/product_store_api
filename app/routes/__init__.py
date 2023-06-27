from fastapi import APIRouter
from .product_route import product_router
from .category_route import category_router


main_api_router = APIRouter()


main_api_router.include_router(product_router, prefix="/product", tags=["product"])
main_api_router.include_router(category_router, prefix="/category", tags=["category"])


@main_api_router.get("/")
async def root():
    return {"message": "Hello World!"}