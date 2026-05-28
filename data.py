import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("ru_RU")

BASE_URL = "https://qa-scooter.education-services.ru/"

def generate_phone_number():
    return f"+7{random.randint(800,999)}{random.randint(100,500)}{random.randint(1000, 5000)}"

def generate_order_data():
    return {
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_name(),
        "phone": generate_phone_number(),
        "comment": fake.text(max_nb_chars=20),
    }

def generate_delivery_date(day):
    return (datetime.now() + timedelta(days=day)).strftime("%d.%m.%Y")
