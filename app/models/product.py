from fastapi import Path, Query
from pydantic import BaseModel


class Product(BaseModel):
    product_id: int = Path(ge=0)
    name: str | None = Query(default=None, min_length=1, max_length=50)
    category: str | None = Query(default=None, min_length=1, max_length=20)
    price: float | None = Query(default=None, gt=0.0)
    stock_count: int = Path(ge=0)
