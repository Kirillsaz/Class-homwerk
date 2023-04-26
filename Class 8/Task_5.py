class Warehouse:
    def __init__(self):
        self.equipment = {}

    def receive_equipment(self, name, quantity):
        if name in self.equipment:
            self.equipment[name] += quantity
        else:
            self.equipment[name] = quantity
