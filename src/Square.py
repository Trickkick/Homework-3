from src.Figure import Figure


class Square(Figure):
    def __init__(self, side, name="Квадрат"):
        if type(side) not in [int, float]:
            raise TypeError("Сторона квадрата должна быть числом, а имя строкой")
        if side <= 0:
            raise ValueError("Недопустимые значения")
        super().__init__(name)
        self._side = side

    @property
    def side(self):
        return self._side

    @property
    def perimeter(self):
        return 4 * self._side

    @property
    def area(self):
        return self._side ** 2
