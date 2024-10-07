from fastapi.testclient import TestClient
from api.src.main import app

test_client = TestClient(app)

class TestHealthCheckRoute:
    """Tests for the /v1/healthcheck route"""

    def test_healthcheck(self):
        """Test for the healthcheck route"""
        response = test_client.get("/v1/healthcheck")

        # Check if the response status code is 200 (OK)
        assert response.status_code == 200

        # Check if the response JSON contains the expected message
        assert response.json() == {"status": "Healthy!"}
