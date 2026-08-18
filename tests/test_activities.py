def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert len(payload) == expected_count
    assert "Chess Club" in payload

    for details in payload.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)


def test_get_activities_includes_baseline_participants(client):
    # Arrange
    activity_name = "Chess Club"
    baseline_participants = {"michael@mergington.edu", "daniel@mergington.edu"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert set(payload[activity_name]["participants"]) == baseline_participants
