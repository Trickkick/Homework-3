import pytest

from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle


@pytest.fixture()
def default_square():
    test_square1 = Square(name="Тестовый квадрат", side=4)
    yield test_square1
    del test_square1


@pytest.fixture()
def second_default_square():
    test_square2 = Square(name="Тестовый квадрат 2", side=5)
    yield test_square2
    del test_square2


@pytest.fixture()
def default_circle():
    test_circle1 = Circle(name="Тестовый круг", radius=4)
    yield test_circle1
    del test_circle1


@pytest.fixture()
def default_circle():
    test_circle1 = Circle(name="Тестовый круг 2", radius=4)
    yield test_circle1
    del test_circle1


@pytest.fixture()
def second_default_circle():
    test_circle2 = Circle(name="Тестовый круг", radius=4)
    yield test_circle2
    del test_circle2


@pytest.fixture()
def default_rectangle():
    test_rectangle1 = Rectangle(name="Тестовый прямоугольник 1", length=4, width=5)
    yield test_rectangle1
    del test_rectangle1


@pytest.fixture()
def second_default_rectangle():
    test_rectangle2 = Rectangle(name="Тестовый прямоугольник 2", length=3, width=6)
    yield test_rectangle2
    del test_rectangle2


@pytest.fixture()
def default_triangle():
    test_triangle1 = Triangle(name="Тестовый прямоугольник 1", a=3, b=4, c=5)
    yield test_triangle1
    del test_triangle1


@pytest.fixture()
def second_default_triangle():
    test_triangle2 = Triangle(name="Тестовый прямоугольник 1", a=4, b=4, c=5)
    yield test_triangle2
    del test_triangle2
