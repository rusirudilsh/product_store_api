from fastapi import APIRouter, HTTPException
from ..models.product_order import ProductOrder
from ..services.product_order_service import make_purchase


order_router = APIRouter()

@order_router.post("/")
async def purchase_product(order_item: ProductOrder):
    result = await make_purchase(order_item)
    if result[1] == "":
        raise HTTPException(status_code = 404, 
                            detail = "Order Item not found", 
                            headers = {"X-Error" : "404 error"})
    elif result[1] == "500":
        raise HTTPException(status_code = 500, 
                            detail = "Something went wrong", 
                            headers = {"X-Error" : "500 server error"}) 
    return {"isSuccess": result[0],  "message": result[1]}