from typing import List
from fastapi import APIRouter
from ..services.category_service import CategoryService


category_router = APIRouter()

@category_router.get("/list")
async def list_categories() -> dict[str, List[str]]:
    result = await CategoryService.get_product_categories()
    return {"productCategories": result}