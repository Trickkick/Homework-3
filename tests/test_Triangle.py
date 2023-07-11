from math import sqrt

import pytest


from src.Triangle import Triangle
from conftest import default_triangle, second_default_triangle


def test_triangle_creation_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(name="Test_triangle", a=1, b=4, c=5)


def test_triangle_perimeter_calculation():
    test_triangle = Triangle(name="Test_triangle", a=3, b=4, c=5)
    assert test_triangle.perimeter == test_triangle.a + test_triangle.b + test_triangle.c


def test_triangle_area_calculation():
    test_triangle = Triangle(name="Test_triangle", a=3, b=4, c=5)
    assert test_triangle.area == sqrt(
        test_triangle.perimeter / 2 * (test_triangle.perimeter / 2 - test_triangle.a) * (
                    test_triangle.perimeter / 2 - test_triangle.b) * (test_triangle.perimeter / 2 - test_triangle.c))


def test_triangle_add_area(default_triangle, second_default_triangle):
    assert default_triangle.add_area(second_default_triangle) == default_triangle.area + second_default_triangle.area


def test_triangle_add_area_value_error(default_triangle):
    with pytest.raises(ValueError):
        default_triangle.add_area(4)
