from fastapi import Path, Query
from pydantic import BaseModel


class ProductUpdate(BaseModel):
    product_id: int = Path(ge=0)
    name: str | None = Query(default=None, min_length=1, max_length=50)
    price: float | None = Query(default=None, gt=0.0)