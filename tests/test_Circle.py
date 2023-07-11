import math

import pytest


from src.Circle import Circle
from conftest import default_circle, second_default_circle


def test_circle_perimeter_calculation():
    test_circle = Circle(name="Test_circle", radius=4)
    assert test_circle.perimeter == 2 * math.pi * test_circle.radius


def test_triangle_area_calculation():
    test_circle = Circle(name="Test_circle", radius=4)
    assert test_circle.area == math.pi * test_circle.radius ** 2


def test_circle_add_area(default_circle, second_default_circle):
    assert default_circle.add_area(second_default_circle) == default_circle.area + second_default_circle.area


def test_circle_add_area_value_error(default_circle):
    with pytest.raises(ValueError):
        default_circle.add_area(4)
