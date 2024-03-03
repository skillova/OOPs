from src.Classes.mixin_product import MixinClassInfo
from src.Classes.product import Product


class SmartPhone(Product, MixinClassInfo):
    """Новый класс на основе уже существующего (родительского) <Product>"""
    def __init__(self, name: str, model: str, efficiency: str, memory: str, color: str, description: str,
                 price: float, quantity: int):
        super().__init__(name, description, color, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        MixinClassInfo.__init__(self)

    def __del__(self):
        pass
