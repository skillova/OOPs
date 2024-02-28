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
