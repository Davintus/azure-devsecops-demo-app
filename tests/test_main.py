import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.main import app


def test_index():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "azure-devsecops-demo-app"
    assert data["status"] == "running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_readiness():
    client = app.test_client()

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ready"
