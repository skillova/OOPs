class Category:
    """Класс для категорий товара"""

    instance_counter = 0
    product_counter = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.instance_counter += 1
        Category.product_counter += len(self.products)
