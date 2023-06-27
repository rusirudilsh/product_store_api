from fastapi import APIRouter, HTTPException, status
from ..services.product_service import get_products, get_product_by_id
from ..models.product import Product
from typing import List


product_router = APIRouter()


@product_router.get("/list", status_code = status.HTTP_200_OK)
async def lis_products(
    category: str | None = None,
    stock_availability: int | None = None
) -> dict[str, List[Product]]:
    return {"products": await get_products(category, stock_availability)}


@product_router.get("/{product_id}", status_code = status.HTTP_200_OK)
async def get_by_id(product_id: int) -> dict[str, Product]:
    result = await get_product_by_id(product_id)
    if result is None:
        raise HTTPException(status_code = 404, 
                            detail = "Product not found", 
                            headers = {"X-Error" : "404 error"})
    return {"product": result}