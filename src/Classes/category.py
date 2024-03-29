import statistics

from src.Classes.product import Product


class Category:
    """Класс для категорий товара"""

    instance_counter = 0
    product_counter = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.instance_counter += 1
        Category.product_counter += 1

    @property
    def set_products(self):
        """Геттер приватного атрибута класса <self.__products>"""
        return self.__products

    @set_products.setter
    def set_products(self, new_product):
        """Сеттер приватного атрибута класса <self.__products>"""
        if new_product.quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        if isinstance(new_product, Product) or issubclass(new_product, Product):
            for product in self.__products:
                if product.name == new_product.name:
                    product.quantity += new_product.quantity
                    if new_product.price >= 0:
                        product.price = new_product.price
                        return
                else:
                    self.__products.append(new_product)
                    return
            raise TypeError('Добавляемый объект не относится к классу <Product>')

    @property
    def get_format_products(self):
        """Возвращает список продуктов в формате (<name>, <price> руб. Остаток: <quantity> шт.)"""
        product_list = []
        for product in self.__products:
            product_list.append(product.__str__())
        return product_list

    def get_average_price(self):
        """Возвращает средний ценник продуктов"""
        try:
            price_list = (prc.price for prc in self.__products)
            average = round(statistics.mean(price_list), 2)
        except statistics.StatisticsError:
            average = 0
        return average


    def __str__(self):
        """Строковое отображение объекта класса в формате (<name>, количество продуктов: <XXX> шт.)"""
        return f'{self.name}, количество продуктов: {len(self.set_products)} шт.'

    def __repr__(self):
        """Отображение информации об объекте класса в режиме отладки (для разработчиков)"""
        return f'{self.__class__.__name__} -> "{self.name}, {self.description}, {self.__products}"'

    def __del__(self):
        pass
