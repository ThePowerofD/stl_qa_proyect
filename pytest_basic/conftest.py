import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield d
    d.quit()

@pytest.fixture
def google_driver(driver):
    driver.get("https://www.google.com")
    yield driver