from ..utility.file_helper import FileHelper


class CategoryService:

    async def get_product_categories() -> list[str]:
        products = await FileHelper.read_csv("../schema/products.csv")
        if products is not None:
            categories = list(set(map(lambda prod: prod["category"].title(), products)))
            return categories
        return []