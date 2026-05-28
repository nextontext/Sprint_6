import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    service = Service("/snap/bin/geckodriver")

    browser = webdriver.Firefox(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()
