from tests import client


def test_list_categories():
    response = client.get("/category/list")
    assert response.status_code == 200
    assert len(response.json()['productCategories']) > 1