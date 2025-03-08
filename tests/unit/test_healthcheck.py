from fastapi import Response
from fastapi.testclient import TestClient

__all__: list[str] = ["TestHealthcheck"]


class TestHealthcheck:
    def test_healtcheck(self, client: TestClient) -> None:
        response: Response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json() == dict(status="Server is up")
