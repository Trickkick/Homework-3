import pytest

from src.Rectangle import Rectangle
from conftest import default_rectangle, second_default_rectangle


@pytest.mark.parametrize("cond", [(0, 0),
                                  (0, 1),
                                  (0, -1),
                                  (1, 0),
                                  (1, -1),
                                  (-1, 1),
                                  (-1, -1),
                                  ])
def test_rectangle_creation_exist_negative(cond):
    with pytest.raises(ValueError):
        Rectangle(name="Test_rectangle", width=cond[0], length=cond[1])


@pytest.mark.parametrize("cond", [(2, 3),
                                  (2.4, 3.2)
                                  ])
def test_rectangle_creation_exist_positive(cond):
    Rectangle(name="Test_rectangle", width=cond[0], length=cond[1])
    pass


@pytest.mark.parametrize("cond", [("t", 1, "a"),
                                  ("t", 1, True),
                                  ("t", True, 1),
                                  ("t", "sada", 1),
                                  (True, 1, 1),
                                  (1, 1, 1),
                                  (1.5, 1, 1)
                                  ])
def test_rectangle_creation_type_error(cond):
    with pytest.raises(TypeError):
        Rectangle(name=cond[0], width=cond[1], length=cond[2])


def test_rectangle_perimeter_calculation():
    test_rectangle = Rectangle(name="Test_rectangle", width=4, length=5)
    assert test_rectangle.perimeter > 0
    assert test_rectangle.perimeter == 2 * (test_rectangle.width + test_rectangle.length)


def test_rectangle_area_calculation():
    test_rectangle = Rectangle(name="Test_rectangle", width=4, length=5)
    assert test_rectangle.area > 0
    assert test_rectangle.area == test_rectangle.width * test_rectangle.length


def test_rectangle_add_area_positive(default_rectangle, second_default_rectangle):
    assert default_rectangle.add_area(
        second_default_rectangle) == default_rectangle.area + second_default_rectangle.area


@pytest.mark.parametrize("cond", [1, 1.5, "asd", False])
def test_rectangle_add_area_negative(default_rectangle, cond):
    with pytest.raises(ValueError):
        default_rectangle.add_area(cond)
