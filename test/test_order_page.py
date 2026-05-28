import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage

from data import (
    BASE_URL,
    generate_order_data,
    generate_delivery_date,
)

@allure.feature("Страница заказа")
class TestOrderPage:
    @pytest.mark.parametrize(
        "order, station, delivery_date, rent_period, scooter_color",
        [
            pytest.param(generate_order_data(), "Савёловская", 1, "сутки", "black", id="black_scooter"),
            pytest.param(generate_order_data(), "Сокольники", 2, "двое суток", "grey", id="grey_scooter"),
        ],
    )
    @allure.story("Заказ самоката")
    @allure.tag("positive")
    def test_order(self, driver, order, station, delivery_date, rent_period, scooter_color):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)        
        driver.get(BASE_URL)

        main_page.click_order_button_header()
        order_page.create_order(
            order,
            station,
            generate_delivery_date(delivery_date),
            rent_period,
            scooter_color,
        )
        assert "Заказ оформлен" in order_page.get_order_confirm_text()

        order_page.press_check_order_status_button()
        order_page.click_logo_links()
