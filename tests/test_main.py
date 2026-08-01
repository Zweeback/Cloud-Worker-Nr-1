from fastapi.testclient import TestClient
from app.main import app

def test_read_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]

def test_get_subworkers():
    with TestClient(app) as client:
        response = client.get("/api/subworkers")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

def test_get_chats():
    with TestClient(app) as client:
        response = client.get("/api/chats")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

def test_drive_search():
    with TestClient(app) as client:
        response = client.get("/api/drive-search")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
