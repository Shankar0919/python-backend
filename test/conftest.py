import pytest
from src.app import create_app
from src.controllers import user_controller


@pytest.fixture(autouse=True)
def clear_users():
    """
    Automatically clear the in-memory users dictionary
    before each individual test.
    """
    user_controller.users.clear()
    yield


@pytest.fixture
def client():
    """
    Provides a fresh Flask test client for each test.
    """
    app = create_app()
    app.testing = True  # Enable Flask testing mode
    with app.test_client() as client:
        yield client
