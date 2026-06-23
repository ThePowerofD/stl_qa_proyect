# test_posts.py
import pytest

@pytest.mark.api
@pytest.mark.parametrize("post_id", [1,2,3,4,5])
def test_get_post(api, post_id):

    session, base_url = api
    response = session.get(f"{base_url}/posts/{post_id}")
    
    assert response.status_code == 200
    assert response.json()["id"] == post_id

@pytest.mark.api
def test_post(api):
    session, base_url = api
    response = session.post(f"{base_url}/posts", json={"title": "test", "body": "this is an example for post"})

    assert response.status_code == 201
    
def test_put(api):
    session, base_url = api 
    response = session.put(f"{base_url}/posts/1", json= { "title": "The New Order", "body": "Wolfenstein"})

    assert response.status_code == 200

def test_patch(api):
    session, base_url = api

    response = session.patch(f"{base_url}/posts/1", json={
    "title": "New Title"})
    

def test_delete(api):
    session, base_url = api
    response = session.delete(f"{base_url}/posts/1")
    assert response.status_code == 200 # more correct should be 204 no content but not this time


