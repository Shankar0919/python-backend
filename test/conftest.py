import pytest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

try:
    from app import create_app
except ImportError:
    from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = False
    with app.test_client() as client:
        yield client
