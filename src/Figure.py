class Figure:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("Метод принимает геометрическую фигуру")

    def calculate_perimeter(self):
        raise NotImplementedError("Переопределяется в подклассе")

    def calculate_area(self):
        raise NotImplementedError("Переопределяется в подклассе")
