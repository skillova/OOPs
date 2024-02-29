from src.Classes.product import Product


class SmartPhone(Product):
    """Новый класс на основе уже существующего (родительского) <Product>"""
    def __init__(self, name: str, model: str, efficiency: str, memory: str, color: str, description: str,
                 price: float, quantity: int):
        super().__init__(name, description, color, price, quantity)
        self.name = name
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __del__(self):
        pass
