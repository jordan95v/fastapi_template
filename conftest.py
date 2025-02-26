import pytest
from fastapi.testclient import TestClient
from core.main import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI app.

    Returns:
        A test client for the FastAPI app.
    """

    return TestClient(app)
