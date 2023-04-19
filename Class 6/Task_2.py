class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asphalt_mass(self, thickness, asphalt_density):
        area = self._length * self._width
        asphalt_mass = area * thickness * asphalt_density
        return asphalt_mass

my_road = Road(1000, 10)
asphalt_mass = my_road.calculate_asphalt_mass(0.05, 2000)
print(f"The total mass of asphalt needed to cover the road is: {asphalt_mass} kg")