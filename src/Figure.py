class Figure:
    NAME = None
    AREA = None
    PERIMETER = None

    def __init__(self, name):
        self.NAME = name

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.AREA + figure.AREA
        else:
            raise ValueError
