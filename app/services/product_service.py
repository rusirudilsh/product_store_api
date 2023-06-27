from ..models.product_update import ProductUpdate
from ..utility.file_helper import read_csv, remove_from_csv
from ..models.product import Product
import pandas as pd
import os


async def get_products(category: str, stock_count: int) -> list[Product]:
        products = await ProductProcessor.get_product_list()
        if category is not None or stock_count is not None:
            return []
        return products


async def get_product_by_id(id: int) -> Product:
    try:
        products = await ProductProcessor.get_product_list()
        result = next(filter(lambda product: int(product["product_id"]) == id, products), None)
        if result is not None:
            await ProductProcessor.set_product_stock(result)  
        return result
    except Exception as error:
        return Product

    
async def update_product(product_id: int, update_model: ProductUpdate) -> Product:
    products = await ProductProcessor.get_product_list()
    product = next(filter(lambda prod: int(prod["product_id"]) == product_id, products), None)   
    if product is None:
        return None  
    if update_model != None:
        update_model.product_id = product_id
        result = ProductProcessor.update_product_row(update_model, product)
        if result is True:
            await ProductProcessor.set_product_stock(product)         
        return product if result is True else Product

    
async def delete_product(product_id: int) -> bool:
    product = next(filter(lambda prod: int(prod["product_id"]) == product_id, 
                          await ProductProcessor.get_product_list()), None)
    if product is None:
        return None  
    result = remove_from_csv("../schema/products.csv", "product_id", product_id)
    if result is True:
        ProductProcessor.remove_product_stock(product_id)
    return result
    


class ProductProcessor():
    @staticmethod
    async def get_product_list() -> list[Product]:
        return await read_csv("../schema/products.csv")
    

    @staticmethod
    async def set_product_stock(product: Product):
        product_stoks = await read_csv("../schema/stocks.csv")
        product_stock = next(filter(lambda prod: int(prod["product_id"]) == int(product["product_id"]), product_stoks), None)
        if product_stock is not None:
            stock_count = int(product_stock["stock_count"])
            if stock_count > 0:
                product["stock_count"] = stock_count
        return product  
    

    @staticmethod
    def remove_product_stock(product_id: int) -> bool:
        return remove_from_csv("../schema/stocks.csv", "product_id", product_id)
    

    @staticmethod
    def update_product_row(data: ProductUpdate, product: Product) -> bool:
        try:
            data_frame = pd.read_csv(os.path.join(os.path.dirname(__file__), "../schema/products.csv"), index_col='product_id')
            if data.name is not None:           
                data_frame.loc[data.product_id, "name"] = data.name
                product["name"] = data.name
            if data.price is not None:
                data_frame.loc[data.product_id, "price"] = data.price
                product["price"] = data.price
            data_frame.to_csv(os.path.join(os.path.dirname(__file__), "../schema/products.csv"))
            return True 
        except Exception as error:
            return False
