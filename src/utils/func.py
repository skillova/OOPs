import pathlib
import json
from src.Classes.category import Category
from src.Classes.product import Product

path = pathlib.Path.cwd().parent / 'data' / 'products.json'


def get_data_from_json(file):
    """Возвращает словарь из файла .json"""
    with open(file, mode='r', encoding='UTF-8') as file:
        return json.load(fp=file)


def get_category_products(data):
    """Создает список объектов класса <Category> со списком объектов класса<Product>"""
    category_list = []
    for ctg in data:
        ctg_name: str = ctg.get('name')
        ctg_description: str = ctg.get('description')
        products_list = []
        for product in ctg.get('products'):
            prod_name: str = product.get('name')
            prod_description: str = product.get('description')
            prod_price: float = product.get('price')
            quantity: int = product.get('quantity')
            products_list.append(Product(prod_name, prod_description, prod_price, quantity))
        category_list.append(Category(ctg_name, ctg_description, products_list))
    return category_list
