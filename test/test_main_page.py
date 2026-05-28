import allure
import pytest

from pages.main_page import MainPage
from data import BASE_URL

@allure.feature("Главная страница")
class TestMainPage:
    @pytest.mark.parametrize(
        "index, accordion_tab_text",
        [
            pytest.param(0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой.", id="accordion_0"),
            pytest.param(1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.", id="accordion_1"),
            pytest.param(2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.", id="accordion_2"),
            pytest.param(3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее.", id="accordion_3"),
            pytest.param(4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.", id="accordion_4"),
            pytest.param(5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.", id="accordion_5"),
            pytest.param(6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.", id="accordion_6"),
            pytest.param(7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.", id="accordion_7"),
        ]
    )
    @allure.story("Аккордеон FAQ")
    @allure.tag("regression", "main page", "positive")
    def test_accordion_text(self, driver, index, accordion_tab_text):
        main_page = MainPage(driver)
        driver.get(BASE_URL)

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
        driver.get(BASE_URL)
        main_page.close_cookie_banner_if_visible()

        main_page.click_order_button_by_entry_point(entry_point)

        assert "/order" in driver.current_url
