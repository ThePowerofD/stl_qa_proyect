import pytest

@pytest.mark.api
@pytest.mark.rainyday
def test_rainyd_post_notfound(api):
    session, base_url = api
    response = session.get(f"{base_url}/posts/99999")
    assert response.status_code == 404

@pytest.mark.api
@pytest.mark.rainyday
def test_rainyd_post_badrequest(api_auth):
    base_url, session = api_auth
    
    response = session.get("https://httpbin.org/status/400")
    assert response.status_code == 400


@pytest.mark.api
@pytest.mark.rainyday
def test_rainy_post_unauthorized(api_auth):
    base_url, session = api_auth #created for another api resource but it is not working

    response = session.get("https://httpbin.org/status/401")

    assert response.status_code == 401

@pytest.mark.api
@pytest.mark.rainyday
def test_rainy_day_get_internalServerError(api):
    session,  _ = api #need to unpack the tuple
    response = session.get("https://httpbin.org/status/500")
    assert response.status_code == 500