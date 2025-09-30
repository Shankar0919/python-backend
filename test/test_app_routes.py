def test_healthcheck_route(client):
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Shankar Python Backend Application is Up and Running successfully"
    }


def test_get_users_empty(client):
    response = client.get("/users")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["statusCode"] == 200
    assert "users" in json_data
    assert json_data["users"] == []


def test_create_user_route(client):
    payload = {"name": "Alice", "active": "true", "dob": "1999-12-31"}
    response = client.post("/users/create", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "User created"
    assert "data" in data
    assert data["data"]["name"] == "Alice"


def test_update_user_route(client):
    # Create first
    payload = {"name": "Bob", "active": "true", "dob": "1995-05-05"}
    res = client.post("/users/create", json=payload)
    user_id = res.get_json()["data"]["id"]

    # Update
    update_payload = {"name": "Bob Marley"}
    response = client.put(f"/users/update/{user_id}", json=update_payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "User updated"
    assert data["data"]["name"] == "Bob Marley"


def test_update_user_not_found(client):
    response = client.put("/users/update/999", json={"name": "Ghost"})
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"


def test_delete_user_route(client):
    # Create first
    payload = {"name": "Charlie", "active": "true", "dob": "1990-10-10"}
    res = client.post("/users/create", json=payload)
    user_id = res.get_json()["data"]["id"]

    # Delete
    response = client.delete(f"/users/delete/{user_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "User deleted"
    assert "data" in data


def test_delete_user_not_found(client):
    response = client.delete("/users/delete/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"
