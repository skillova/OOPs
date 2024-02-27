import pathlib
import pytest

from src.utils.func import get_data_from_json, get_category_products


@pytest.fixture
def category_data():
    path = pathlib.Path.cwd() / 'data' / 'products.json'
    data = get_data_from_json(path)
    return get_category_products(data)


# проверка последних объектов в списках

def test_category(category_data):
    assert (category_data[0]
            .name == "Смартфоны")
    assert (category_data[0]
            .description == ("Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                             "функций для удобства жизни"))
    assert isinstance(category_data[0].products, list) == 1
    assert category_data[-1].instance_counter == 2
    assert category_data[-1].product_counter == 4


def test_product(category_data):
    product = category_data
    assert product[-1].products[-1].name == '55" QLED 4K'
    assert product[-1].products[-1].description == 'Фоновая подсветка'
    assert product[-1].products[-1].price == 123000.0
    assert product[-1].products[-1].quantity == 7
