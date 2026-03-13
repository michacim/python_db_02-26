from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_expense():

    response = client.post(
        "/expenses/",
        json={
            "category":"food",
            "amount":10,
            "date":"2026-03-08"
        }
    )

    assert response.status_code == 200