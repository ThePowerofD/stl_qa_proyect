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
def page_driver(driver):
    driver.get("https://www.stlgears.com/")
    yield driver

