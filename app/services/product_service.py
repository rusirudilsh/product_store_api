from ..utility.file_helper import read_csv
from ..models.product import Product


async def get_products(category: str, stock_count: int) -> list[Product]:
        products = await ProductProcessor.get_product_list()
        if category is not None or stock_count is not None:
            return []
        return products

async def get_product_by_id(id: int) -> Product:
    try:
        products = await ProductProcessor.get_product_list()
        result = next(filter(lambda product: int(product["product_id"]) == id, products), None)         
        return result
    except Exception as error:
        return Product



class ProductProcessor():
    @staticmethod
    async def get_product_list() -> list[Product]:
        return await read_csv("../schema/products.csv")