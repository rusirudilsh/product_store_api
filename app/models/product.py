from pydantic import BaseModel


class Product(BaseModel):
    product_id: int = -1
    name: str
    category: str
    price: float
    stock_count: int = 0
