import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name="Круг"):
        if type(radius) not in [int, float]:
            raise TypeError("Радиус круга должен быть числом, а имя строкой")
        if radius <= 0:
            raise ValueError("Недопустимые значения")
        super().__init__(name)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius ** 2
