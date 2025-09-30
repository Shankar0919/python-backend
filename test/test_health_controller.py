import pytest
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_healthcheck(client):
    response = client.get("/healthcheck")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {
        "message": "Shankar Python Backend Application is Up and Running successfully"
    }
