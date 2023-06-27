from tests import client


def test_purchase_product():
    response = client.post("/order/",
                          json = {"items": [
                                {
                                "product_id": 3,
                                "quantity": 1
                                }],
                            "total":100 })
    assert response.status_code == 200
    assert response.json() == {"isSuccess": True, 
                               "message": "Product 3 (Vintage crop tee) was purchased"}


def test_purchase_product_invalid_product_id():
    response = client.post("/order/",
                          json = {"items": [
                                {
                                "product_id": 300,
                                "quantity": 1
                                }],
                            "total":100 })
    assert response.status_code == 404
    assert response.json() == {"detail": "Order Item not found"}


def test_purchase_product_invalid_quantity():
    response = client.post("/order/",
                          json = {"items": [
                                {
                                "product_id": 3,
                                "quantity": 100
                                }],
                            "total":100 })
    assert response.status_code == 200
    assert response.json() == {"isSuccess": False, 
                               "message": "Quantity exceeded for Product 3 (Vintage crop tee)"}