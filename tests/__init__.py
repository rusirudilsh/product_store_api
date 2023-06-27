from fastapi.testclient import TestClient
from app import product_store_api

client = TestClient(product_store_api)

__all__ = ["client"]