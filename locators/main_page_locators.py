from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button_header = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    order_status_button = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Статус заказа']")
    order_status_input = (By.XPATH, ".//div[contains(@class, 'Header_SearchInput')]//input")
    go_to_search_button = (By.XPATH, ".//div[contains(@class, 'Header_SearchInput')]//button")
    order_button_footer = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    cookie_button = (By.XPATH, "//button[normalize-space()='да все привыкли']")
    

    @staticmethod
    def accordion_question_locator(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def accordion_answer_locator(index):
        return By.ID, f"accordion__panel-{index}"
    
    @staticmethod
    def order_button_locator(entry_point):
        return {
            "header": MainPageLocators.order_button_header,
            "footer": MainPageLocators.order_button_footer,
        }[entry_point]
