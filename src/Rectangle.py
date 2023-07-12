from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, length, name="Прямоугольник"):
        if (type(width) not in [int, float]) or (type(length) not in [int, float]):
            raise TypeError("Длина и ширина прямоугольника должны быть числами, а имя строкой")
        if width <= 0 or length <= 0:
            raise ValueError("Недопустимые значения")
        super().__init__(name)
        self._width = width
        self._length = length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @property
    def perimeter(self):
        return 2 * (self._width + self._length)

    @property
    def area(self):
        return self._width * self._length
