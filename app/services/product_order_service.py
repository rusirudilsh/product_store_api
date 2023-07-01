import os
from ..services.product_service import ProductProcessor
from ..models.product_order import ProductOrder
import pandas as pd


async def make_purchase(order: ProductOrder):
    orderProcessor = OrderProcessor(order)
    result = await orderProcessor.update_stock_count()
    return result



# this function returns success status and success message. if error, then error code.
class OrderProcessor:
    def __init__(self, order: ProductOrder):
        self.order = order

    async def update_stock_count(self) -> tuple[bool, str]:
        try:
            if len(self.order.items) > 0:
                item = self.order.items[0]
                data_frame = pd.read_csv(os.path.join(os.path.dirname(__file__), "../schema/stocks.csv"), index_col='product_id')
                product = next(filter(lambda prod: int(prod["product_id"]) ==  item.product_id, 
                            await ProductProcessor.get_product_list()), None)
                if product is None:
                        return (False, "404")
                if item.quantity > 0:
                    stock_data = data_frame.loc[[item.product_id]]
                    if stock_data["stock_count"].values[0] < item.quantity:
                        return (False, "Quantity exceeded for Product {} ({})".format(product["product_id"], product["name"]))
                    
                    data_frame.loc[item.product_id, "stock_count"] = stock_data["stock_count"].values[0] - item.quantity
                    data_frame.to_csv(os.path.join(os.path.dirname(__file__), "../schema/stocks.csv"))
                    return (True, "Product {} ({}) was purchased".format(product["product_id"], product["name"]))
             
        except Exception as error:
            return (False, "500") 