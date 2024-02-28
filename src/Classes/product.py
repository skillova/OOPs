class Product:
    """Класс для описания товара в магазине"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product_object(cls, name: str, description: str, price: float, quantity: int):
        """Создание экземпляра класса Product"""
        return cls(name, description, price, quantity)

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
        """Сложение продуктов, умноженных на количество на складе"""
        return self.quantity * self.__price + other

    def __radd__(self, other):
        """Сложение пользовательского значения <int> и стоимости, умноженного на количество на складе"""
        return other + self.quantity * self.__price

    def __str__(self):
        """Строковое отображение объекта класса в формате (<name>, <price> руб. Остаток: <quantity> шт.)"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __repr__(self):
        """Отображение информации об объекте класса в режиме отладки (для разработчиков)"""
        return f'{self.__class__.__name__} -> ({self.name}, {self.description}, {self.__price}, {self.quantity}'
