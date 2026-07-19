from urllib.parse import quote

from fastapi.testclient import TestClient

from src.app import app as fastapi_app


def test_unregister_participant_removes_their_signup():
    # Arrange
    client = TestClient(fastapi_app)
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{quote(activity_name)}/participants/{participant_email}"
    )

    # Assert
    assert response.status_code == 200
    assert participant_email in response.json()["message"]

    activities_response = client.get("/activities")
    assert participant_email not in activities_response.json()[activity_name]["participants"]
