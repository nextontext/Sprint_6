import allure
from selenium.webdriver.common.by import By


class MainPage:
    order_button_header = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    order_status_button = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Статус заказа']")
    order_status_input = (By.XPATH, ".//div[contains(@class, 'Header_SearchInput')]//input")
    go_to_search_button = (By.XPATH, ".//div[contains(@class, 'Header_SearchInput')]//button")
    order_button_footer = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    cookie_button = (By.XPATH, "//button[normalize-space()='да все привыкли']")
    scooter_logo = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    yandex_logo = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def accordion_question_locator(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def accordion_answer_locator(index):
        return By.ID, f"accordion__panel-{index}"
    
    @staticmethod
    def order_button_locator(entry_point):
        return {
            "header": MainPage.order_button_header,
            "footer": MainPage.order_button_footer,
        }[entry_point]

    @allure.step("Переходим к заказу через точку входа: {entry_point}")
    def click_order_button_by_entry_point(self, entry_point):
        self.driver.find_element(*self.order_button_locator(entry_point)).click()

    @allure.step("Нажимаем кнопку 'Заказать' в хедере")
    def click_order_button_header(self):
        self.driver.find_element(*self.order_button_header).click()

    @allure.step("Нажимаем кнопку 'Статус заказа' в хедере")
    def click_order_status_button(self):
        self.driver.find_element(*self.order_status_button).click()

    @allure.step("Отправляем номер заказа: {order_number}")
    def set_order_number(self, order_number):
        self.driver.find_element(*self.order_status_input).send_keys(order_number)

    @allure.step("Нажимаем кнопку 'Go'")
    def click_go_to_search_button(self):
        self.driver.find_element(*self.go_to_search_button).click()

    @allure.step("Нажимаем кнопку 'Заказать' в футере")
    def click_order_button_footer(self):
        self.driver.find_element(*self.order_button_footer).click()

    @allure.step("Нажимаем кнопку согласия на использование cookie")
    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()

    @allure.step("Закрываем cookie-баннер, если он отображается")
    def close_cookie_banner_if_visible(self):
        cookie_buttons = self.driver.find_elements(*self.cookie_button)
        if cookie_buttons:
            cookie_buttons[0].click()

    @allure.step("Нажимаем вкладку номер '{index}' в аккордеоне")
    def click_accordion_question(self, index):
        self.driver.find_element(*self.accordion_question_locator(index)).click()

    @allure.step("Получаем текст вкладки номер '{index}' в аккордеоне")
    def get_accordion_answer_text(self, index):
        return self.driver.find_element(*self.accordion_answer_locator(index)).text

    @allure.step("Нажимаем на логотип Самоката")
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step("Нажимаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step("Открываем вопрос номер '{index}' в блоке 'Вопросы о важном'")
    def open_accordion_question(self, index):
        self.close_cookie_banner_if_visible()
        self.click_accordion_question(index)

    @allure.step("Получаем ответ на вопрос номер '{index}'")
    def get_accordion_text_after_open(self, index):
        self.open_accordion_question(index)
        return self.get_accordion_answer_text(index)

    @allure.step("Переходим к поиску заказа по номеру")
    def search_order_by_number(self, order_number):
        self.click_order_status_button()
        self.set_order_number(order_number)
        self.click_go_to_search_button()
