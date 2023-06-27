from ..utility.file_helper import read_csv


async def get_product_categories() -> list[str]:
    products = await read_csv("../schema/products.csv")
    if products is not None:
        categories = list(set(map(lambda prod: prod["category"], products)))
        return categories
    return []