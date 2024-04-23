from chalice.test import Client
from app import app
import json


def test_post_products():
    with Client(app) as client:
        response = client.http.post(
            "/product",
            body=json.dumps({"product": "arroz", "amount": "2"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_put_products():
    with Client(app) as client:
        response = client.http.put(
            "/product",
            body=json.dumps({"product": "arroz", "amount": "2"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_delete_products():
    with Client(app) as client:
        response = client.http.delete(
            "/product",
            body=json.dumps({"product": "arroz", "amount": "2"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_products():
    with Client(app) as client:
        response = client.http.get("/product")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_getid_offline():
    with Client(app) as client:
        response = client.http.get("/product/1")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
