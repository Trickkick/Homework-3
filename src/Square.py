from src.Figure import Figure


class Square(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
        self.PERIMETER = 4 * self.side
        self.AREA = self.side**2
