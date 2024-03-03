import json
import pathlib

from src.Classes.category import Category
from src.Classes.lawn_grass import LawnGrass
from src.Classes.smartphone import SmartPhone

path = pathlib.Path.cwd().parent.parent / 'data' / 'products.json'


def get_data_from_json(file):
    """Возвращает словарь из файла .json"""
    with open(file, mode='r', encoding='UTF-8') as file:
        return json.load(fp=file)


def get_category_list(data):
    """Создает список объектов класса <Category> со списком объектов класса <Product>"""
    category_list = []
    for ctg in data:
        product_object_list = []
        ctg_name: str = ctg.get('name')
        ctg_description: str = ctg.get('description')
        for product in ctg.get('products'):
            data = list(product.values())
            if ctg_name == "Смартфоны":
                product_object = SmartPhone(*data)
                product_object_list.append(product_object)
            if ctg_name == "Трава газонная":
                product_object = LawnGrass(*data)
                product_object_list.append(product_object)
        category_list.append(Category(ctg_name, ctg_description, product_object_list))
    return category_list

ctg_prod = get_data_from_json(path)
object_list = get_category_list(ctg_prod)
