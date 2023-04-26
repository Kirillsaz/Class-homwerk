class Warehouse:
    def __init__(self):
        self.equipment = {}

    def receive_equipment(self, name, quantity):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if name in self.equipment:
            self.equipment[name] += quantity
        else:
            self.equipment[name] = quantity

warehouse = Warehouse()

name = input("Enter the name of the equipment: ")
while not isinstance(name, str):
    print("Invalid input. Name must be a string.")
    name = input("Enter the name of the equipment: ")

quantity = input("Enter the quantity of the equipment: ")
while not quantity.isdigit():
    print("Invalid input. Quantity must be an integer.")
    quantity = input("Enter the quantity of the equipment: ")

warehouse.receive_equipment(name, int(quantity))
print(warehouse.equipment)
