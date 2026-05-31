import random
from faker import Faker
from datetime import datetime, timedelta

class Urls:
    BASE_URL = "https://qa-scooter.education-services.ru/"


class AccordionTexts:
    ANSWERS = {
        0: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        1: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        2: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        3: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        4: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        5: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        6: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        7: "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    }


class OrderData:
    fake = Faker("ru_RU")

    @staticmethod
    def generate_phone_number():
        return f"+7{random.randint(800,999)}{random.randint(100,500)}{random.randint(1000, 5000)}"

    @classmethod
    def generate_order_data(cls):
        return {
            "name": cls.fake.first_name(),
            "last_name": cls.fake.last_name(),
            "address": cls.fake.street_name(),
            "phone": cls.generate_phone_number(),
            "comment": cls.fake.text(max_nb_chars=20),
        }

    @staticmethod
    def generate_delivery_date(day):
        return (datetime.now() + timedelta(days=day)).strftime("%d.%m.%Y")
