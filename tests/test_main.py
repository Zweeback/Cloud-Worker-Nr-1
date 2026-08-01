from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_get_subworkers():
    response = client.get("/api/subworkers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_chats():
    response = client.get("/api/chats")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_drive_search():
    response = client.get("/api/drive-search")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
