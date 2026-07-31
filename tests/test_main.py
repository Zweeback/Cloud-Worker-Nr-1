from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "agent": "Alice", "message": "Gatekeeper ist aktiv."}

def test_get_agent_status():
    response = client.get("/agent/status")
    assert response.status_code == 200
    assert response.json() == {"llm_initialized": True, "model": "gpt-4o"}
