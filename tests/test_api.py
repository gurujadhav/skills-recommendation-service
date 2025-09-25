import json
from app import app

def test_add_user():
    client = app.test_client()
    response = client.post("/user", 
        data=json.dumps({"name": "Alice", "skills": ["Python", "Java"]}),
        content_type="application/json"
    )
    assert response.status_code == 201

def test_recommend():
    client = app.test_client()
    response = client.get("/recommend/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "recommendations" in data
