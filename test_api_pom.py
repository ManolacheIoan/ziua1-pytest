import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()


def test_get_user(api_session):
    response = api_session.get(f"{BASE_URL}/users/1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data
    assert "@" in data["email"]


@pytest.mark.parametrize("post_id, expected_status", [
    (1, 200),
    (100, 200),
    (999, 404),
])
def test_multiple_post_ids(api_session, post_id, expected_status):
    response = api_session.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == expected_status


def test_response_time_is_reasonable(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2


def test_response_headers(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
