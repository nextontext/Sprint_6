import allure
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import BASE_URL

class OrderPage:
    name = (By.XPATH, ".//input[@placeholder='* Имя']")
    last_name = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    address = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    phone = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[normalize-space()='Далее']")

    delivery_day = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rent_period = (By.XPATH, ".//div[contains(@class, 'Dropdown-control')]")
    comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    confirm_yes_button = (By.XPATH, ".//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    confirm_header = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")
    check_status_button = (By.XPATH, ".//div[contains(@class, 'Order_NextButton')]//button[text()='Посмотреть статус']")
    

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def metro_station_locator(metro):
        return By.XPATH, f"//div[text()='{metro}']"

    @staticmethod
    def rent_period_locator(rent_period):
        return By.XPATH, f".//div[contains(@class, 'Dropdown-option') and text()='{rent_period}']"

    @staticmethod
    def scooter_color_locator(color):
        return By.ID, color

    @allure.step("Заполняем поле 'Имя'")
    def send_keys_to_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    @allure.step("Заполняем поле 'Фамилия'")
    def send_keys_to_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    @allure.step("Заполняем поле 'Адрес'")
    def send_keys_to_address(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    @allure.step("Выбираем станцию метро")
    def send_keys_to_metro(self, metro_station):
        self.driver.find_element(*self.metro).send_keys(metro_station)
        self.driver.find_element(*self.metro_station_locator(metro_station)).click()

    @allure.step("Заполняем поле 'Телефон'")
    def send_keys_to_phone(self, phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    @allure.step("Нажимаем кнопку 'Далее'")
    def press_next_button(self):
        self.driver.find_element(*self.next_button).click()

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
        date_input = self.driver.find_element(*self.delivery_day)
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбираем срок аренды")
    def select_rent_period(self, rent_period):
        self.driver.find_element(*self.rent_period).click()
        self.driver.find_element(*self.rent_period_locator(rent_period)).click()

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, color):
        self.driver.find_element(*self.scooter_color_locator(color)).click()

    @allure.step("Оставляем комментарий для курьера")
    def send_keys_to_comment(self, comment):
        self.driver.find_element(*self.comment).send_keys(comment)

    @allure.step("Заполняем форму 'Про аренду'")
    def fill_rent_form(self, delivery_date, rent_period, scooter_color, comment):
        self.send_keys_to_delivery_day(delivery_date)
        self.select_rent_period(rent_period)
        self.choose_scooter_color(scooter_color)
        self.send_keys_to_comment(comment)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def press_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step("Подтверждаем заказ")
    def press_yes_button(self):
        self.driver.find_element(*self.confirm_yes_button).click()

    @allure.step("Получаем текст окна успешного заказа")
    def get_order_confirm_text(self):
        return self.driver.find_element(*self.confirm_header).text

    @allure.step("Переходим в статус заказа")
    def press_check_order_status_button(self):
        self.driver.find_element(*self.check_status_button).click()

    @allure.step("Оформляем заказ")
    def create_order(self, order, station, delivery_date, rent_period, scooter_color):
        self.fill_customer_form(order, station)
        self.fill_rent_form(delivery_date, rent_period, scooter_color, order["comment"])
        self.press_order_button()
        self.press_yes_button()

    @allure.step("Проходим по ссылкам в логотипах")
    def click_logo_links(self):
        main_page = MainPage(self.driver)

        main_page.click_scooter_logo()
        assert self.driver.current_url.rstrip("/") == BASE_URL.rstrip("/")

        old_window = self.driver.current_window_handle

        main_page.click_yandex_logo()

        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(2)
        )

        for window in self.driver.window_handles:
            if window != old_window:
                self.driver.switch_to.window(window)
                break
        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("ya.ru")
        )

        assert "ya" in self.driver.current_url
