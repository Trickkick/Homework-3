import abc
from abc import ABC


class Figure(ABC):

    def __init__(self, name="Фигура"):
        if type(name) != str:
            raise TypeError("Имя должно быть строкой")
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    @abc.abstractmethod
    def perimeter(self):
        pass

    @property
    @abc.abstractmethod
    def area(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("Метод принимает геометрическую фигуру")
