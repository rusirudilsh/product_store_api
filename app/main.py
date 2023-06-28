from fastapi import FastAPI
from .routes import main_api_router
from fastapi.middleware.cors import CORSMiddleware

description = """ 
Product Store API serves your Online Store
"""

product_store_api = FastAPI(
    title = "Product Store API",
    description = description,
    version = "1.0"
)

origins = [
    "http://localhost",
    "http://localhost:5173",
]

product_store_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

product_store_api.include_router(main_api_router)