from fastapi.testclient import TestClient

from src.app import app as fastapi_app


def test_unregister_participant_removes_their_signup():
    client = TestClient(fastapi_app)

    response = client.delete(
        "/activities/Chess%20Club/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    assert "michael@mergington.edu" in response.json()["message"]

    activities_response = client.get("/activities")
    assert "michael@mergington.edu" not in activities_response.json()["Chess Club"]["participants"]
