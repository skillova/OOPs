import pathlib
import pytest

from src.Classes.product import Product
from src.Classes.smartphone import SmartPhone
from src.utils.func import get_data_from_json, get_category_list


@pytest.fixture
def category_data() -> list:
    path = pathlib.Path.cwd() / 'data' / 'products.json'
    data = get_data_from_json(path)
    return get_category_list(data)


def test_category_init(category_data):
    """Тест прохождения инициализации класса <Category>"""
    category = category_data[0]
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни")
    assert isinstance(category.set_products, list) == 1
    assert category.instance_counter == 2
    assert category.product_counter == 6


def test_product_init(category_data):
    """Тест прохождения инициализации класса <Product>"""
    product = category_data[0].set_products[0]
    assert product.name == "ASUS"
    assert product.description == "ASUS ROG Phone 7 Ultimate 16/512 ГБ, Dual nano SIM, белый"
    assert product.price == 210000.0
    assert product.quantity == 5

def test_smartphone_init(category_data):
    """Тест прохождения инициализации класса <SmartPhone>"""
    product = category_data[0].set_products[0]
    assert product.name == 'ASUS'
    assert product.model == 'ROG Phone 7 Ultimate'
    assert product.efficiency == '3.2 Ghz'
    assert product.memory == '16/512 ГБ'
    assert product.color == 'White'
    assert product.description == 'ASUS ROG Phone 7 Ultimate 16/512 ГБ, Dual nano SIM, белый'
    assert product.price == 210000.0
    assert product.quantity == 5

def test_lawn_grass_init(category_data):
    """Тест прохождения инициализации класса <LawnGrass>"""
    product = category_data[-1].set_products[0]
    assert product.name == 'Канада Грин'
    assert product.description == 'Быстро всходит, неприхотлив в уходе. Морозоустойчив, быстро восстанавливается.'
    assert product.color == 'Green'
    assert product.germination == '10-14 day'
    assert product.made_country == 'Russia'
    assert product.price == 2500.0
    assert product.quantity == 20

def test_category_get_format_products(category_data):
    """Тест списка продуктов в формате (<name>, <price> руб. Остаток: <quantity> шт.)"""
    format_product = category_data[0].set_products[0]
    assert format_product.__str__() == 'ASUS, 210000.0 руб. Остаток: 5 шт.'


def test_product_new_product_object():
    """Тест @classmethod Product"""
    data_products = ('Dildo', 'vibrato', 'Negro', 50000.0, 13)
    new_product_obj = Product.new_product_object(*data_products)
    assert new_product_obj.name == 'Dildo'
    assert new_product_obj.description == 'vibrato'
    assert new_product_obj.price == 50000.0
    assert new_product_obj.quantity == 13


def test_category_add_product(category_data):
    """Тест установки цены и изменения цены с условием через декоратор @property"""
    category = category_data[0]
    assert category.set_products[0].name == "ASUS"
    assert category.set_products[0].price == 210000.0
    assert category.set_products[0].quantity == 5

    data_products = ("ASUS",
                     "ROG Phone 7 Ultimate",
                     "3.2 Ghz",
                     "16/512 ГБ",
                     "White",
                     "ASUS ROG Phone 7 Ultimate 16/512 ГБ, Dual nano SIM, белый",
                     100.0,
                     5)
    new_product = SmartPhone(*data_products)
    category.set_products = new_product
    assert category.set_products[0].name == "ASUS"
    assert category.set_products[0].price == 100.0
    assert category.set_products[0].quantity == 10

    data_products = ('Dildo', 'vibrato', 'Negro', 60000.0, 100)
    new_product = Product.new_product_object(*data_products)
    category.set_products = new_product
    assert category.set_products[-1].name == 'Dildo'
    assert category.set_products[-1].price == 60000.0
    assert category.set_products[-1].quantity == 100


def test_category_str_(category_data):
    """Тест отображения объекта класса <Category> в формате (<name>, количество продуктов: <XXX> шт."""
    assert category_data[0].__str__() == 'Смартфоны, количество продуктов: 3 шт.'
    assert category_data[-1].__str__() == 'Трава газонная, количество продуктов: 3 шт.'


def test_product_add_(category_data):
    """Тест сложения продуктов <quantity * price> + <other(quantity * price)>"""
    asus = category_data[0].set_products[0]
    samsung = category_data[0].set_products[1]
    canada_green = category_data[1].set_products[0]
    assert (asus + samsung) == 2750000.0
    with pytest.raises(ValueError) as val_err:
        error = asus + canada_green
    assert 'Сложение возможно только двух одинаковых категорий' in str(val_err.value)

