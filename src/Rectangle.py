from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, width, length):
        super().__init__(name)
        self.width = width
        self.length = length
        self.PERIMETER = 2 * (self.width + self.length)
        self.AREA = self.width * self.length
