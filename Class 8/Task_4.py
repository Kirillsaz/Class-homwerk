class Warehouse:
    def __init__(self):
        self.printers = 0
        self.scanners = 0
        self.photocopiers = 0

    def add_printer(self, quantity):
        self.printers += quantity

    def add_scanner(self, quantity):
        self.scanners += quantity

    def add_photocopier(self, quantity):
        self.photocopiers += quantity

    def remove_printer(self, quantity):
        self.printers -= quantity

    def remove_scanner(self, quantity):
        self.scanners -= quantity

    def remove_photocopier(self, quantity):
        self.photocopiers -= quantity

class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, speed, resolution):
        super().__init__(brand, model, price)
        self.speed = speed
        self.resolution = resolution

class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, resolution, color):
        super().__init__(brand, model, price)
        self.resolution = resolution
        self.color = color

class Photocopier(OfficeEquipment):
    def __init__(self, brand, model, price, speed, paper_size):
        super().__init__(brand, model, price)
        self.speed = speed
        self.paper_size = paper_size
