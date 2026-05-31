from selenium.webdriver.common.by import By


class OrderPageLocators:
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
    order_success_header = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
    check_status_button = (By.XPATH, ".//div[contains(@class, 'Order_NextButton')]//button[text()='Посмотреть статус']")
    
    @staticmethod
    def metro_station_locator(metro):
        return By.XPATH, f"//div[text()='{metro}']"

    @staticmethod
    def rent_period_locator(rent_period):
        return By.XPATH, f".//div[contains(@class, 'Dropdown-option') and text()='{rent_period}']"

    @staticmethod
    def scooter_color_locator(color):
        return By.ID, color
