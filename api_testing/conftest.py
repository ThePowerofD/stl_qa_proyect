# conftest.py
import pytest
import requests

@pytest.fixture(scope="session")
def api():
    base_url = "https://jsonplaceholder.typicode.com"
    headers = {"Content-Type": "application/json"}
    
    session = requests.Session()
    session.headers.update(headers)
    
    yield session, base_url         # hand both to the test
    
    session.close()

@pytest.fixture(scope="session")
def api_auth():
    base_url = "https://reqres.in"
    headers = {"Content-Type": "application/json"}

    session = requests.Session()
    session.headers.update(headers)
    yield base_url, session

    session.close()