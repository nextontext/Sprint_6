from selenium.webdriver.common.by import By


class BasePageLocators:
    scooter_logo = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    yandex_logo = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
