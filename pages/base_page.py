import allure
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def wait_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    def wait_number_of_windows_to_be(self, number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(number)
        )

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self, old_window):
        for window in self.driver.window_handles:
            if window != old_window:
                self.driver.switch_to.window(window)
                break
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)
    
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    @allure.step("Нажимаем на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.scooter_logo)

    @allure.step("Нажимаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.yandex_logo)
