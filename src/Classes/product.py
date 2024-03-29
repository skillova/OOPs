from src.Classes.abstract_class import AbstractProduct
from src.Classes.mixin_product import MixinClassInfo


class Product(AbstractProduct, MixinClassInfo):
    """Класс для описания товара в магазине"""

    def __init__(self, name: str, description: str, color: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        MixinClassInfo.__init__(self)

    @classmethod
    def new_product_object(cls, name: str, description: str, color: str, price: float, quantity: int):
        """Создание экземпляра класса Product"""
        return cls(name, description, color, price, quantity)

    @property
    def price(self):
        """Вернуть значение приватного атрибута <self.__price>"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Установка цены объекта класса Product, если товар в списке продуктов то проверяется условие веса стоимости"""
        if 0 <= new_price > self.__price:
            self.__price = new_price
        elif 0 <= new_price < self.__price:
            confirm: str = input("Подтверждение понижения цены ( y / n ): ").lower()
            if confirm == 'y':
                self.__price = new_price
            else:
                print('Новая цена не установлена')
        else:
            print('Цена введена некорректная')

    def __add__(self, other):
        """Сложение продуктов с проверкой принадлежности к одному классу, умноженных на количество на складе"""
        if isinstance(self, type(other)) and isinstance(other, type(self)):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise ValueError('Сложение возможно только двух одинаковых категорий')

    def __str__(self):
        """Строковое отображение объекта класса в формате (<name>, <price> руб. Остаток: <quantity> шт.)"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __del__(self):
        pass
