from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle

square = Square(name="Квадрат", side=4)
print(f"Площадь фигуры {square.NAME} равна {square.AREA}")

square2 = Square(name="Квадратик", side=2)
print(f"Площадь фигуры {square2.NAME} равна {square2.AREA}")

circle = Circle(name="Круг", radius=5)
print(f"Площадь фигуры {circle.NAME} равна {circle.AREA}")

triangle = Triangle(name="Треугольник", a=3, b=4, c=5)
print(f"Площадь фигуры {triangle.NAME} равна {triangle.AREA}")

rectangle = Rectangle(name="Прямоугольник", width=3, length=4)
print(f"Площадь фигуры {rectangle.NAME} равна {rectangle.AREA}")

print(f"Площадь фигуры {circle.NAME} равна {circle.AREA}, если добавить к ней площадь фигуры {square.NAME}, которая "
      f"равна {square.AREA}, то получится {circle.add_area(square)}")
