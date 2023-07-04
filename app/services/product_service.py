from ..utility.file_helper import read_csv, remove_from_csv
from ..models.product import Product
import pandas as pd
import os


async def get_products(category: str, stock_availability: bool, current_products_count: int, products_per_page: int) -> tuple[list[Product], int]:
    products = await ProductProcessor.get_product_list()
    products_count = len(products)
    if products_count > 0 :
        for product in products:
            product = await ProductProcessor.set_product_props(product)
        if category is not None and len(category) > 0 and category != "All" or stock_availability is True:
            products = [prod for prod in products if ProductProcessor.filter_product(prod, category, stock_availability)]

            #to set the product count after the filtering
            #this will helps to adjust the paginator after filtering the list
            #paginotor will be adjusted automatically with all the products as well as filtered products
            products_count = len(products)
        slice_start = current_products_count
        slice_stop = products_per_page + current_products_count
        products = products[slice_start:slice_stop]
        
    return (products, products_count)


async def get_product_by_id(id: int) -> Product:
    try:
        products = await ProductProcessor.get_product_list()
        result = next(filter(lambda product: int(product["product_id"]) == id, products), None)
        if result is not None:
            await ProductProcessor.set_product_props(result)  
        return result
    except Exception as error:
        return Product

    
async def update_product(product_id: int, update_product: Product) -> Product:
    products = await ProductProcessor.get_product_list()
    product = next(filter(lambda prod: int(prod["product_id"]) == product_id, products), None)  
    if product is None:
        return None  
    else:
        update_product.product_id = product_id
        productProcessor = ProductProcessor(product)
        result = productProcessor.update_product_row()        
        return update_product if result is True else Product

    
async def delete_product(product_id: int) -> bool:
    product = next(filter(lambda prod: int(prod["product_id"]) == product_id, 
                          await ProductProcessor.get_product_list()), None)
    if product is None:
        return None  
    result = remove_from_csv("../schema/products.csv", "product_id", product_id)
    if result is True:
        ProductProcessor.remove_product_stock(product_id)
    return result
    


class ProductProcessor:
    def __init__(self, product: Product):
        self.product = product

    @staticmethod
    async def get_product_list() -> list[Product]:
        return await read_csv("../schema/products.csv")
    

    @staticmethod
    async def set_product_props(product: Product) -> Product:
        product_stoks = await read_csv("../schema/stocks.csv")
        product_stock = next(filter(lambda prod: int(prod["product_id"]) == int(product["product_id"]), product_stoks), None)
        if product_stock is not None:
            product["category"] = product["category"].title()
            stock_count = int(product_stock["stock_count"])
            if stock_count >= 0:
                product["stock_count"] = stock_count
        return product 
    

    @staticmethod
    def remove_product_stock(product_id: int) -> bool:
        return remove_from_csv("../schema/stocks.csv", "product_id", product_id)
    

    def update_product_row(self) -> bool:
        try:
            data_frame = pd.read_csv(os.path.join(os.path.dirname(__file__), "../schema/products.csv"), index_col='product_id')
            if self.product["name"] is not None:           
                data_frame.loc[self.product["product_id"], "name"] = self.product["name"]
            if self.product["price"] is not None:
                data_frame.loc[self.product["product_id"], "price"] = self.product["price"]
            data_frame.to_csv(os.path.join(os.path.dirname(__file__), "../schema/products.csv"))
            return True 
        except Exception as error:
            return False
    

    @staticmethod
    def filter_product(product: Product, category: str, isAvailability: bool) -> bool:
        return all(
            (
                product["category"].lower() == category.lower() if category is not None and category != "All" else 1 == 1,
                product["stock_count"] > 0 if isAvailability == True else isAvailability == False            
            )
        )