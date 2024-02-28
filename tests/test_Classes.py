import pathlib

import pytest

from src.Classes.product import Product
from src.utils.func import get_data_from_json, get_category_products


@pytest.fixture
def category_data() -> list:
    path = pathlib.Path.cwd() / 'data' / 'products.json'
    data = get_data_from_json(path)
    return get_category_products(data)


def test_category_init(category_data):
    """Тест прохождения инициализации класса <Category>"""
    category = category_data[-1]
    assert category.name == "Телевизоры"
    assert category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")
    assert isinstance(category.set_products, list) == 1
    assert category.instance_counter == 2
    assert category.product_counter == 4


def test_product_init(category_data):
    """Тест прохождения инициализации класса <Product>"""
    product = category_data[-1].set_products[-1]
    assert product.name == '55" QLED 4K'
    assert product.description == 'Фоновая подсветка'
    assert product.price == 123000.0
    assert product.quantity == 7


def test_category_get_format_products(category_data):
    """Тест списка продуктов в формате (<name>, <price> руб. Остаток: <quantity> шт.)"""
    category = category_data[-1]
    assert category.get_format_products[0] == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_product_new_product_object():
    """Тест @classmethod Product"""
    data_products = ('Dildo', 'vibrato', 50000.0, 13)
    new_product_obj = Product.new_product_object(*data_products)
    assert new_product_obj.name == 'Dildo'
    assert new_product_obj.description == 'vibrato'
    assert new_product_obj.price == 50000.0
    assert new_product_obj.quantity == 13


def test_category_add_product(category_data):
    """Тест установки цены и изменения цены с условием через декоратор @property"""
    category = category_data[-1]
    assert category.set_products[-1].name == '55" QLED 4K'
    assert category.set_products[-1].quantity == 7

    data_products = ('55" QLED 4K', 'vibrato', 200.0, 10)
    from src.Classes.product import Product
    new_product = Product.new_product_object(*data_products)
    category.set_products = new_product
    assert category.set_products[-1].name == '55" QLED 4K'
    assert category.set_products[-1].price == 200.0
    assert category.set_products[-1].quantity == 17

    data_products = ('Dildo', 'vibrato', 60000.0, 100)
    new_product = Product.new_product_object(*data_products)
    category.set_products = new_product
    assert category.set_products[-1].name == 'Dildo'
    assert category.set_products[-1].price == 60000.0
    assert category.set_products[-1].quantity == 100
