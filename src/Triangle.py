from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            super().__init__(name)
            self.a = a
            self.b = b
            self.c = c
            self.PERIMETER = self.a + self.b + self.c
            self.AREA = sqrt(self.PERIMETER/2 * (self.PERIMETER/2 - a) * (self.PERIMETER/2 - b) * (self.PERIMETER/2 - c))
        else:
            raise ValueError
