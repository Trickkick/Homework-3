import pytest

from src.Square import Square
from conftest import default_square, second_default_square


def test_square_perimeter_calculation():
    test_square = Square(name="Test_rectangle", side=4)
    assert test_square.perimeter == 4 * test_square.side


def test_square_area_calculation():
    test_square = Square(name="Test_rectangle", side=4)
    assert test_square.area == test_square.side ** 2


def test_square_add_area(default_square, second_default_square):
    assert default_square.add_area(
        second_default_square) == default_square.area + second_default_square.area


def test_square_add_area_value_error(default_square):
    with pytest.raises(ValueError):
        default_square.add_area(4)
