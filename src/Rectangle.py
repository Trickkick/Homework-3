from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, width, length):
        super().__init__(name)
        self.width = width
        self.length = length
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

    def calculate_area(self):
        return self.width * self.length
