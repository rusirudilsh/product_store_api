from tests import client

def test_list_products():
    response = client.get("/product/list")
    assert response.status_code == 200
    assert len(response.json()['products']) > 1
       