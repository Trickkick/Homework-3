import math

import pytest

from src.Circle import Circle
from conftest import default_circle, second_default_circle


@pytest.mark.parametrize("cond", [0, -1])
def test_circle_creation_exist_negative(cond):
    with pytest.raises(ValueError):
        Circle(name="Test_circle", radius=cond)


@pytest.mark.parametrize("cond", [1, 1.5])
def test_circle_creation_exist_positive(cond):
    Circle(name="Test_circle", radius=cond)
    pass


@pytest.mark.parametrize("cond", [("a", "t"),
                                  ("a", True),
                                  (1, 1),
                                  (1.6, 1),
                                  (True, False)
                                  ])
def test_circle_creation_type_error(cond):
    with pytest.raises(TypeError):
        Circle(name=cond[0], radius=cond[1])


def test_circle_perimeter_calculation():
    test_circle = Circle(name="Test_circle", radius=4)
    assert test_circle.perimeter == 2 * math.pi * test_circle.radius


def test_triangle_area_calculation():
    test_circle = Circle(name="Test_circle", radius=4)
    assert test_circle.area > 0
    assert test_circle.area == math.pi * test_circle.radius ** 2


def test_circle_add_area_positive(default_circle, second_default_circle):
    assert default_circle.add_area(second_default_circle) > default_circle.area
    assert default_circle.add_area(second_default_circle) == default_circle.area + second_default_circle.area


@pytest.mark.parametrize("cond", ["t", True, 4, 5.5])
def test_circle_add_area_negative(default_circle, cond):
    with pytest.raises(ValueError):
        default_circle.add_area(cond)
