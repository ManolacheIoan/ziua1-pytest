import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    
    posts = response.json()
    assert len(posts) == 100
    assert isinstance(posts, list)


def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/99999")
    
    assert response.status_code == 404


def test_create_post():
    new_post = {
        "title": "Test post",
        "body": "This is a test",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == "Test post"
    assert "id" in data
