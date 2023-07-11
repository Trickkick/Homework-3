from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            super().__init__(name)
            self.a = a
            self.b = b
            self.c = c
            self.perimeter = self.calculate_perimeter()
            self.area = self.calculate_area()
        else:
            raise ValueError("Нельзя создать треугольник с такими сторонами")

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        return sqrt(self.perimeter / 2 * (self.perimeter / 2 - self.a) * (self.perimeter / 2 - self.b) * (
                    self.perimeter / 2 - self.c))
