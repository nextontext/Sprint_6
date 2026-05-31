import allure
import pytest

from pages.main_page import MainPage
from data import Urls, AccordionTexts

@allure.feature("Главная страница")
class TestMainPage:
    @pytest.mark.parametrize(
        "index, accordion_tab_text",
        [
            pytest.param(index, text, id=f"accordion_{index}")
            for index, text in AccordionTexts.ANSWERS.items()
        ]
    )
    @allure.story("Аккордеон FAQ")
    @allure.tag("regression", "main page", "positive")
    def test_accordion_text(self, driver, index, accordion_tab_text):
        main_page = MainPage(driver)
        main_page.open_main_page()

        assert main_page.get_accordion_text_after_open(index) == accordion_tab_text

    @pytest.mark.parametrize(
        "entry_point",
        [
            pytest.param("header", id="header_order_button"),
            pytest.param("footer", id="footer_order_button"),
        ],
    )
    @allure.story("Точки входа в заказ")
    @allure.tag("regression", "main page", "positive")
    def test_order_buttons_open_order_page(self, driver, entry_point):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.close_cookie_banner_if_visible()

        main_page.click_order_button_by_entry_point(entry_point)

        assert main_page.is_order_page_opened()

    @allure.story("Переход по логотипу Самоката")
    @allure.tag("regression", "main page", "positive")
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_order_button_header()
        main_page.click_scooter_logo()

        assert main_page.get_current_url().rstrip("/") == Urls.BASE_URL.rstrip("/")
    
    @allure.story("Переход по логотипу Яндекса")
    @allure.tag("regression", "main page", "positive")
    def test_yandex_logo_opens_ya_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()

        old_window = main_page.get_current_window()
        main_page.click_yandex_logo()
        main_page.wait_number_of_windows_to_be(2)
        main_page.switch_to_new_window(old_window)

        assert main_page.is_url_contains("ya.ru")
