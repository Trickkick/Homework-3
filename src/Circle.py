import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
