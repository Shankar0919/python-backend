def test_create_user_success(client):
    response = client.post("/api/users/create", json={
        "name": "shankar",
        "active": "true",
        "dob": "2000-01-01"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["data"]["name"] == "Shankar"

def test_create_user_invalid_date(client):
    response = client.post("/api/users/create", json={
        "name": "test",
        "active": "true",
        "dob": "not-a-date"
    })
    assert response.status_code == 400

def test_update_user_not_found(client):
    response = client.put("/api/users/update/999", json={"name": "updated"})
    assert response.status_code == 404

def test_delete_user(client):
    response = client.post("/api/users/create", json={
        "name": "to-delete",
        "active": "true",
        "dob": "2000-01-01"
    })
    user_id = response.get_json()["data"]["id"]
    response = client.delete(f"/api/users/delete/{user_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "User deleted"
