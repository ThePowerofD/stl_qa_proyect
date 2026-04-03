import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_stl_title(page_driver):
    assert "STLGears.com | The Free Gear" in page_driver.title

#def test_google_search_box(google_driver):
 #   search_box = google_driver.find_element(By.NAME, "q")
  #  assert search_box.is_displayed()