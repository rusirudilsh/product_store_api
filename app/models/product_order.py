from fastapi import Query
from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product_id: int
    quantity: int = Query(gt=0)


class ProductOrder(BaseModel):
    items: List[OrderItem]
    total: float