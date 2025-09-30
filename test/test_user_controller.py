import pytest
from src.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client


def test_get_users_empty(client):
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_user_success(client):
    payload = {"name": "John", "active": "true", "dob": "2000-01-01"}
    response = client.post("/api/users/create", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "User created"
    assert "data" in data
    assert data["data"]["name"] == "John"


def test_create_user_missing_name(client):
    payload = {"active": "true", "dob": "2000-01-01"}
    response = client.post("/api/users/create", json=payload)
    assert response.status_code == 400
    assert response.get_json()["error"] == "Name is required"


def test_update_user_success(client):
    # create user first
    payload = {"name": "Jane", "active": "true", "dob": "1995-01-01"}
    create_res = client.post("/api/users/create", json=payload)
    user_id = create_res.get_json()["data"]["id"]

    # update user
    update_payload = {"name": "Jane Doe"}
    response = client.put(f"/api/users/update/{user_id}", json=update_payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "User updated"
    assert data["data"]["name"] == "Jane Doe"


def test_update_user_not_found(client):
    response = client.put("/api/users/update/999", json={"name": "Ghost"})
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"


def test_delete_user_success(client):
    # create user first
    payload = {"name": "Alex", "active": "true", "dob": "1990-01-01"}
    create_res = client.post("/api/users/create", json=payload)
    user_id = create_res.get_json()["data"]["id"]

    # delete user
    response = client.delete(f"/api/users/delete/{user_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "User deleted"
    assert "data" in data


def test_delete_user_not_found(client):
    response = client.delete("/api/users/delete/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"
