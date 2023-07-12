from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c, name="Треугольник"):
        if (type(a) not in [int, float]) or (type(b) not in [int, float]) or (type(c) not in [int, float]):
            raise TypeError("Стороны треугольника могут быть только числами, а имя строкой")
        if a + b < c or a + c < b or b + c < a:
            raise ValueError("Недопустимые значения")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Недопустимые значения")
        super().__init__(name)
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def perimeter(self):
        return self._a + self._b + self._c

    @property
    def area(self):
        return sqrt(self.perimeter / 2 * (self.perimeter / 2 - self._a) * (self.perimeter / 2 - self._b) * (
                self.perimeter / 2 - self._c))
