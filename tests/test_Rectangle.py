import pytest

from src.Rectangle import Rectangle
from conftest import default_rectangle, second_default_rectangle


def test_rectangle_perimeter_calculation():
    test_rectangle = Rectangle(name="Test_rectangle", width=4, length=5)
    assert test_rectangle.perimeter == 2 * (test_rectangle.width + test_rectangle.length)


def test_rectangle_area_calculation():
    test_rectangle = Rectangle(name="Test_rectangle", width=4, length=5)
    assert test_rectangle.area == test_rectangle.width * test_rectangle.length


def test_rectangle_add_area(default_rectangle, second_default_rectangle):
    assert default_rectangle.add_area(
        second_default_rectangle) == default_rectangle.area + second_default_rectangle.area


def test_rectangle_add_area_value_error(default_rectangle):
    with pytest.raises(ValueError):
        default_rectangle.add_area(4)
