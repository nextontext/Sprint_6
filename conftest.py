import pytest
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    browser =  webdriver.Firefox
    browser.maximize_window()
    yield browser
    browser.quit()

