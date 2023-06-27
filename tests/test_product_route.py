from tests import client

def test_list_products():
    response = client.get("/product/list")
    assert response.status_code == 200
    assert len(response.json()['products']) > 1

def test_get_by_id():
    response = client.get("/product/2")
    assert response.status_code == 200
    assert response.json() == {
        "product" : {"product_id":2,"name":"Seasalt white shirt","category":"tops","price":15.0}
    }

def test_get_by_id_404():
    response = client.get("/product/200")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}
       