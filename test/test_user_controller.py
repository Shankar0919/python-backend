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
