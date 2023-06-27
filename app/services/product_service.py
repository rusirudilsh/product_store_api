from ..utility.file_helper import read_csv
from ..models.product import Product


async def get_products(category: str, stock_count: int) -> list[Product]:
        products = await ProductProcessor.get_product_list()
        if category is not None or stock_count is not None:
            return []
        return products



class ProductProcessor():
    async def get_product_list() -> list[Product]:
        return await read_csv("../schema/products.csv")