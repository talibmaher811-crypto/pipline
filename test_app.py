"""Unit test untuk aplikasi."""
from app import app


def test_index():
    """Endpoint / mengembalikan pesan."""
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello, pipeline!"


def test_health():
    """Endpoint /health mengembalikan ok."""
    client = app.test_client()
    res = client.get("/health")
    assert res.get_json()["status"] == "ok"
