import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        self.PERIMETER = 2 * math.pi * self.radius
        self.AREA = math.pi * radius**2
