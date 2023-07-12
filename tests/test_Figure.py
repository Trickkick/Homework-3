import math

import pytest

from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from conftest import default_circle, default_rectangle, default_triangle, default_square


@pytest.mark.parametrize("test_figure", [(Square(1), Triangle(1, 1, 1)),
                                         (Square(1), Circle(1)),
                                         (Square(1), Rectangle(1, 1)),
                                         (Triangle(1, 1, 1), Circle(1)),
                                         (Triangle(1, 1, 1), Rectangle(1, 1)),
                                         (Circle(1), Rectangle(1, 1))
                                         ])
def test_figure_add_area(test_figure):
    assert test_figure[0].add_area(test_figure[1]) == test_figure[0].area + test_figure[1].area
