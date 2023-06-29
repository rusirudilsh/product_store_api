from fastapi import FastAPI

from app.config import Settings
from .routes import main_api_router
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings

description = """ 
Product Store API serves your Online Store
"""

product_store_api = FastAPI(
    title = get_settings().app_name,
    description = description,
    version = get_settings().app_version
)

product_store_api.add_middleware(
    CORSMiddleware,
    allow_origins= get_settings().origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

product_store_api.include_router(main_api_router)