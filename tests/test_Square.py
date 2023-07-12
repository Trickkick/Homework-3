import pytest

from src.Square import Square
from conftest import default_square, second_default_square


@pytest.mark.parametrize("cond", [0, -1])
def test_square_exist_negative(cond):
    with pytest.raises(ValueError):
        Square(name="Test_circle", side=cond)


@pytest.mark.parametrize("cond", [1, 1.5])
def test_square_exist_positive(cond):
    Square(name="Test_square", side=cond)
    pass


@pytest.mark.parametrize("cond", [("t", "sad"),
                                  ("t", False),
                                  (1, 1),
                                  (1.5, 1.5),
                                  (False, 1)
                                  ])
def test_square_creation_type_error(cond):
    with pytest.raises(TypeError):
        Square(name=cond[0], side=cond[1])


def test_square_perimeter_calculation():
    test_square = Square(name="Test_rectangle", side=4)
    assert test_square.perimeter > 0
    assert test_square.perimeter == 4 * test_square.side


def test_square_area_calculation():
    test_square = Square(name="Test_rectangle", side=4)
    assert test_square.area > 0
    assert test_square.area == test_square.side ** 2


def test_square_add_area_positive(default_square, second_default_square):
    assert default_square.add_area(
        second_default_square) == default_square.area + second_default_square.area


@pytest.mark.parametrize("cond", [1, 1.5, "dqw", True])
def test_square_add_area_negative(default_square, cond):
    with pytest.raises(ValueError):
        default_square.add_area(cond)
