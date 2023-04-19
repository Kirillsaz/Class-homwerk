class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"The {self.color} {self.name} car has started moving.")

    def stop(self):
        print(f"The {self.color} {self.name} car has stopped.")

    def turn(self, direction):
        print(f"The {self.color} {self.name} car turned {direction}.")

    def show_speed(self):
        print(f"The current speed of the {self.color} {self.name} car is {self.speed} km/h.")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Slow down! You're exceeding the speed limit.")
        else:
            print(f"The current speed of the {self.color} {self.name} car is {self.speed} km/h.")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Slow down! You're exceeding the speed limit.")
        else:
            print(f"The current speed of the {self.color} {self.name} car is {self.speed} km/h.")

class PoliceCar(Car):
    pass