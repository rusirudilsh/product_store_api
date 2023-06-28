from fastapi import APIRouter, HTTPException, status
from ..models.product_update import ProductUpdate
from ..services.product_service import delete_product, get_products, get_product_by_id, update_product
from ..models.product import Product
from typing import List


product_router = APIRouter()


@product_router.get("/list", status_code = status.HTTP_200_OK)
async def list_products(
    category: str | None = None,
    stock_availability: bool | None = None,
    first: int = 0,
    products_per_page: int = 5
):
    result = await get_products(category, stock_availability, first, products_per_page)
    return {"products": result[0], "product_count": result[1]}


@product_router.get("/{product_id}", status_code = status.HTTP_200_OK)
async def get_by_id(product_id: int) -> dict[str, Product]:
    result = await get_product_by_id(product_id)
    if result is None:
        raise HTTPException(status_code = 404, 
                            detail = "Product not found", 
                            headers = {"X-Error" : "404 error"})
    return {"product": result}


@product_router.put("/{product_id}", status_code = status.HTTP_200_OK)
async def update(product_id: int, product: ProductUpdate) -> dict[str, Product]:
    result = await update_product(product_id, product)
    if result is None:
        raise HTTPException(status_code = 404, 
                            detail = "Product not found to update", 
                            headers = {"X-Error" : "404 error"})
    elif result is not None and result["product_id"] == -1:
        raise HTTPException(status_code = 500, 
                            detail = "Something went wrong", 
                            headers = {"X-Error" : "500 server error"})
    return {"updatedProduct" : result} 


@product_router.delete("/{product_id}", status_code = status.HTTP_200_OK)
async def delete(product_id: int):
    result = await delete_product(product_id)
    if result is None:
        raise HTTPException(status_code = 404, 
                            detail = "Product not found to delete", 
                            headers = {"X-Error" : "404 error"})
    if result is False:
        raise HTTPException(status_code = 500, 
                            detail = "Something went wrong", 
                            headers = {"X-Error" : "500 server error"})
    return {"isDeleted": result}