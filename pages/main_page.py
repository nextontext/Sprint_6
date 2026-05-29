import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import BASE_URL


class MainPage(BasePage):
    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.open_url(BASE_URL)
    
    @allure.step("Проверяем, что открылась страница заказа")
    def is_order_page_opened(self):
        return "/order" in self.get_current_url()

    @allure.step("Переходим к заказу через точку входа: {entry_point}")
    def click_order_button_by_entry_point(self, entry_point):
        self.click_element(MainPageLocators.order_button_locator(entry_point))

    @allure.step("Нажимаем кнопку 'Заказать' в хедере")
    def click_order_button_header(self):
        self.click_element(MainPageLocators.order_button_header)

    @allure.step("Нажимаем кнопку 'Статус заказа' в хедере")
    def click_order_status_button(self):
        self.click_element(MainPageLocators.order_status_button)

    @allure.step("Отправляем номер заказа: {order_number}")
    def set_order_number(self, order_number):
        self.send_keys_to_element(MainPageLocators.order_status_input, order_number)

    @allure.step("Нажимаем кнопку 'Go'")
    def click_go_to_search_button(self):
        self.click_element(MainPageLocators.go_to_search_button)

    @allure.step("Нажимаем кнопку 'Заказать' в футере")
    def click_order_button_footer(self):
        self.click_element(MainPageLocators.order_button_footer)

    @allure.step("Нажимаем кнопку согласия на использование cookie")
    def click_cookie_button(self):
        self.click_element(MainPageLocators.cookie_button)

    @allure.step("Закрываем cookie-баннер, если он отображается")
    def close_cookie_banner_if_visible(self):
        cookie_buttons = self.find_elements(MainPageLocators.cookie_button)
        if cookie_buttons:
            cookie_buttons[0].click()

    @allure.step("Нажимаем вкладку номер '{index}' в аккордеоне")
    def click_accordion_question(self, index):
        self.click_element(MainPageLocators.accordion_question_locator(index))

    @allure.step("Получаем текст вкладки номер '{index}' в аккордеоне")
    def get_accordion_answer_text(self, index):
        return self.get_text_from_element(MainPageLocators.accordion_answer_locator(index))

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
