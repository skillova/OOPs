from src.Classes.product import Product


class LawnGrass(Product):
    """Новый класс на основе уже существующего (родительского) <Product>"""
    def __init__(self, name: str, description: str, color: str, germination: str, made_country: str, price: float,
                 quantity: int):
        super().__init__(name, description, color, price, quantity)
        self.made_country = made_country
        self.germination = germination

    def __del__(self):
        pass
