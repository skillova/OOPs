from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @abstractmethod
    def __init__(self,):
        pass

    @classmethod
    @abstractmethod
    def new_product_object(cls, *args):
        """Создание экземпляра класса Product"""

    @abstractmethod
    def __str__(self):
        """Строковое отображение объекта класса в формате (<name>, <price> руб. Остаток: <quantity> шт.)"""

    @abstractmethod
    def __repr__(self):
        """Отображение информации об объекте класса в режиме отладки (для разработчиков)"""

    @abstractmethod
    def __del__(self):
        """Делитер"""
