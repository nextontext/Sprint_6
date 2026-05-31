import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage

from data import OrderData

@allure.feature("Страница заказа")
class TestOrderPage:
    @pytest.mark.parametrize(
        "order, station, delivery_date, rent_period, scooter_color",
        [
            pytest.param(OrderData.generate_order_data(), "Савёловская", 1, "сутки", "black", id="black_scooter"),
            pytest.param(OrderData.generate_order_data(), "Сокольники", 2, "двое суток", "grey", id="grey_scooter"),
        ],
    )
    @allure.story("Заказ самоката")
    @allure.tag("positive")
    def test_order(self, driver, order, station, delivery_date, rent_period, scooter_color):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)        

        main_page.open_main_page()

        main_page.click_order_button_header()
        order_page.create_order(
            order,
            station,
            OrderData.generate_delivery_date(delivery_date),
            rent_period,
            scooter_color,
        )
        
        assert order_page.is_order_success_header_displayed()
