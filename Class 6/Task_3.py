class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

worker = Worker("John", "Doe", "Developer", 50000, 10000)
position = Position("Jane", "Doe", "Manager", 75000, 15000)
print(worker.name)   # John
print(position.position)   # Manager
print(position.get_full_name())   # Jane Doe
print(position.get_total_income())   # 90000