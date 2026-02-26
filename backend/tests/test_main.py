from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.post("/analyze", json={
        "resume_text": "Python backend developer with Django and REST APIs experience",
        "job_description": "Looking for AI Software Developer with Python experience"
    })

    assert response.status_code == 200
    assert "match_percentage" in response.json()