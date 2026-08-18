import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

PRISTINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities before every test for isolation."""
    activities.clear()
    activities.update(copy.deepcopy(PRISTINE_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app)
