from fastapi import FastAPI
from .routes import main_api_router

description = """ 
Product Store API serves your Online Store
"""

product_store_api = FastAPI(
    title = "Product Store API",
    description = description,
    version = "1.0"
)



product_store_api.include_router(main_api_router)