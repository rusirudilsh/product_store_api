from tests import client


def test_list_products():
    response = client.get("/product/list")
    assert response.status_code == 200
    assert len(response.json()['products']) > 1

def test_list_products_with_filter_params():
    response = client.get("/product/list?category=tops&stock_availability=true")
    assert response.status_code == 200
    assert len(response.json()['products']) == 6


def test_get_by_id():
    response = client.get("/product/2")
    assert response.status_code == 200
    assert response.json() == {
        "product" : {"product_id":2, 
                     "name":"Seasalt white shirt", 
                     "category":"Tops", 
                     "price":15.0, "stock_count": 10}
    }


def test_get_by_id_404():
    response = client.get("/product/200")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}
       

def test_update():
    response = client.put("/product/5",
                          json = {"product_id":5,
                                  "name":"Ivo blue",
                                   "price":15.0})
    assert response.status_code == 200
    assert response.json() == {
        "updatedProduct" : {"product_id":5,
                             "name":"Ivo blue",
                             "category":"Tops", 
                             "price":15.0, "stock_count": 0}
    }


def test_update_404():
    response = client.put("/product/500",
                          json = {"product_id":500,
                                  "name":"Ivo blue",
                                  "price":15.0})
    assert response.status_code == 404


def test_delete():
     response = client.delete("product/11")
     assert response.status_code == 200
     assert response.json() == {"isDeleted": True}


def test_delete_404():
    response = client.delete("product/100")
    assert response.status_code == 404