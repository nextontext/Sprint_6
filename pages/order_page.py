import allure
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from data import BASE_URL
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполняем поле 'Имя'")
    def send_keys_to_name(self, name):
        self.send_keys_to_element(OrderPageLocators.name, name)

    @allure.step("Заполняем поле 'Фамилия'")
    def send_keys_to_last_name(self, last_name):
        self.send_keys_to_element(OrderPageLocators.last_name, last_name)

    @allure.step("Заполняем поле 'Адрес'")
    def send_keys_to_address(self, address):
        self.send_keys_to_element(OrderPageLocators.address, address)

    @allure.step("Выбираем станцию метро")
    def send_keys_to_metro(self, metro_station):
        self.send_keys_to_element(OrderPageLocators.metro, metro_station)
        self.click_element(OrderPageLocators.metro_station_locator(metro_station))

    @allure.step("Заполняем поле 'Телефон'")
    def send_keys_to_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.phone, phone)

    @allure.step("Нажимаем кнопку 'Далее'")
    def press_next_button(self):
        self.click_element(OrderPageLocators.next_button)

    @allure.step("Заполняем форму 'Для кого самокат'")
    def fill_customer_form(self, order, station):
        self.send_keys_to_name(order["name"])
        self.send_keys_to_last_name(order["last_name"])
        self.send_keys_to_address(order["address"])
        self.send_keys_to_metro(station)
        self.send_keys_to_phone(order["phone"])
        self.press_next_button()

    @allure.step("Заполняем поле 'Когда привезти самокат'")
    def send_keys_to_delivery_day(self, delivery_date):
        date_input = self.find_element(OrderPageLocators.delivery_day)
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбираем срок аренды")
    def select_rent_period(self, rent_period):
        self.click_element(OrderPageLocators.rent_period)
        self.click_element(OrderPageLocators.rent_period_locator(rent_period))

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, color):
        self.click_element(OrderPageLocators.scooter_color_locator(color))

    @allure.step("Оставляем комментарий для курьера")
    def send_keys_to_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.comment, comment)

    @allure.step("Заполняем форму 'Про аренду'")
    def fill_rent_form(self, delivery_date, rent_period, scooter_color, comment):
        self.send_keys_to_delivery_day(delivery_date)
        self.select_rent_period(rent_period)
        self.choose_scooter_color(scooter_color)
        self.send_keys_to_comment(comment)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def press_order_button(self):
        self.click_element(OrderPageLocators.order_button)

    @allure.step("Подтверждаем заказ")
    def press_yes_button(self):
        self.click_element(OrderPageLocators.confirm_yes_button)

    @allure.step("Проверяем, что отображается окно успешного заказа")
    def is_order_success_header_displayed(self):
        return self.is_element_displayed(OrderPageLocators.order_success_header)

    @allure.step("Переходим в статус заказа")
    def press_check_order_status_button(self):
        self.click_element(OrderPageLocators.check_status_button)

    @allure.step("Оформляем заказ")
    def create_order(self, order, station, delivery_date, rent_period, scooter_color):
        self.fill_customer_form(order, station)
        self.fill_rent_form(delivery_date, rent_period, scooter_color, order["comment"])
        self.press_order_button()
        self.press_yes_button()

    @allure.step("Проходим по ссылкам в логотипах")
    def click_logo_links(self):
        self.click_scooter_logo()
        assert self.get_current_url().rstrip("/") == BASE_URL.rstrip("/")

        old_window = self.get_current_window()

        self.click_yandex_logo()

        self.wait_number_of_windows_to_be(2)
        self.switch_to_new_window(old_window)
        self.wait_url_contains("ya.ru")

        assert "ya" in self.get_current_url()
