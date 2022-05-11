from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_microservices():
    response = client.get("/get_all_microservice_data")
    assert response.status_code == 200
    assert len(response.json().keys()) == 3