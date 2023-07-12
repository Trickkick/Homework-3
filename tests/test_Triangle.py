from math import sqrt

import pytest


from src.Triangle import Triangle
from conftest import default_triangle, second_default_triangle


@pytest.mark.parametrize("cond", [(1, 0, 0),
                                  (1, 1, 0),
                                  (1, 0, 1),
                                  (0, 1, 0),
                                  (0, 0, 1),
                                  (0, 1, 1),
                                  (1, -1, -1),
                                  (1, 1, -1),
                                  (1, -1, 1),
                                  (-1, 1, -1),
                                  (-1, -1, 1),
                                  (-1, 1, 1),
                                  (1, 0, -1),
                                  (1, -1, 0),
                                  (-1, 0, 1),
                                  (-1, 1, 0),
                                  (0, 1, -1),
                                  (0, -1, 1),
                                  (4, 2, 7)
                                  ])
def test_triangle_creation_exist_negative(cond):
    with pytest.raises(ValueError):
        Triangle(name="Test_triangle", a=cond[0], b=cond[1], c=cond[2])


@pytest.mark.parametrize("cond", [(3, 3, 3),
                                  (3.5, 3.3, 3.4)
                                  ])
def test_triangle_creation_exist_positive(cond):
    Triangle(name="Test_triangle", a=cond[0], b=cond[1], c=cond[2])
    pass


@pytest.mark.parametrize("cond", [("t", True, 1, 1),
                                  ("t", 1, "sdwr", 1),
                                  (1, 1, 1, 1),
                                  (False, 1, 1, 1),
                                  (1.5, 1.4, 1.3, 1.2)
                                  ])
def test_triangle_creation_type_error(cond):
    with pytest.raises(TypeError):
        Triangle(name=cond[0], a=cond[1], b=cond[2], c=cond[3])


def test_triangle_perimeter_calculation():
    test_triangle = Triangle(name="Test_triangle", a=3, b=4, c=5)
    assert test_triangle.perimeter > 0
    assert test_triangle.perimeter == test_triangle.a + test_triangle.b + test_triangle.c


def test_triangle_area_calculation():
    test_triangle = Triangle(name="Test_triangle", a=3, b=4, c=5)
    assert test_triangle.area > 0
    assert test_triangle.area == sqrt(
        test_triangle.perimeter / 2 * (test_triangle.perimeter / 2 - test_triangle.a) * (
                    test_triangle.perimeter / 2 - test_triangle.b) * (test_triangle.perimeter / 2 - test_triangle.c))


def test_triangle_add_area_positive(default_triangle, second_default_triangle):
    assert default_triangle.add_area(second_default_triangle) == default_triangle.area + second_default_triangle.area


@pytest.mark.parametrize("cond", [1, 1.5, "dqw", True])
def test_triangle_add_area_negative(default_triangle, cond):
    with pytest.raises(ValueError):
        default_triangle.add_area(cond)
