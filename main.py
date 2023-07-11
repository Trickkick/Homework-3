from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle

square = Square(name="Квадрат", side=4)
print(f"Площадь фигуры {square.name} равна {square.area}")

square2 = Square(name="Квадратик", side=2)
print(f"Площадь фигуры {square2.name} равна {square2.area}")

circle = Circle(name="Круг", radius=5)
print(f"Площадь фигуры {circle.name} равна {circle.area}")

triangle = Triangle(name="Треугольник", a=3, b=4, c=5)
print(f"Площадь фигуры {triangle.name} равна {triangle.area}")

rectangle = Rectangle(name="Прямоугольник", width=3, length=4)
print(f"Площадь фигуры {rectangle.name} равна {rectangle.area}")

print(f"Площадь фигуры {circle.name} равна {circle.area}, если добавить к ней площадь фигуры {square.name}, которая "
      f"равна {square.area}, то получится {circle.add_area(square)}")
