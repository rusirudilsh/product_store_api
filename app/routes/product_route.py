from fastapi import APIRouter, status
from ..services.product_service import get_products
from ..models.product import Product
from typing import List


product_router = APIRouter()


@product_router.get("/list", status_code = status.HTTP_200_OK)
async def lis_products(
    category: str | None = None,
    stock_availability: int | None = None
) -> dict[str, List[Product]]:
    return {"products": await get_products(category, stock_availability)}