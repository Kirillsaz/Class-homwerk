from abc import ABC, abstractmethod

class Clothing(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_required(self):
        pass

class Coat(Clothing):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cloth_required(self):
        return self.size / 6.5 + 0.5

class Suit(Clothing):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cloth_required(self):
        return 2 * self.height + 0.3

class ClothingFactory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def cloth_required(self):
        total_cloth = 0
        for product in self.products:
            total_cloth += product.cloth_required
        return total_cloth
