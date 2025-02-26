from fastapi import Response
from fastapi.testclient import TestClient


class TestHealthCheck:
    def test_health_check(self, client: TestClient) -> None:
        response: Response = client.get("/health_check")
        assert response.status_code == 200
        assert response.json() == dict(status="Server is up")
