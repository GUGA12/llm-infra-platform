from fastapi.testclient import TestClient
import sys; sys.path.insert(0, "src")
from main import app

def test_healthz():
    assert TestClient(app).get("/healthz").json()["ok"] is True
