from chalice.test import Client
from app import app
import json


def test_post_offline():
    with Client(app) as client:
        response = client.http.post(
            "/sales/offline",
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_put_offline():
    with Client(app) as client:
        response = client.http.put(
            "/sales/offline",
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_delete_offline():
    with Client(app) as client:
        response = client.http.delete(
            "/sales/offline",
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_offline():
    with Client(app) as client:
        response = client.http.get("/sales/offline")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_getid_offline():
    with Client(app) as client:
        response = client.http.get("/sales/offline/1")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


########################################## ONLINE ##########################################


def test_post_online():
    with Client(app) as client:
        response = client.http.post(
            "/sales/online",
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_put_online():
    with Client(app) as client:
        response = client.http.put(
            "/sales/online",
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_delete_online():
    with Client(app) as client:
        response = client.http.delete(
            "/sales/online",
            body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
            headers={"Content-Type": "application/json"},
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_online():
    with Client(app) as client:
        response = client.http.get("/sales/online")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_getid_online():
    with Client(app) as client:
        response = client.http.get("/sales/online/1")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
