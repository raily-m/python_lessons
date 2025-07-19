class Shape:
    def __init__(self, name):
        self.name = name
    

class Rectangle(Shape):
    pass


class Square(Rectangle):
    pass
    

class Triangle(Shape):
    pass


class Iso_triangle(Triangle):
    pass


class Equ_triangle(Triangle):
    pass


class Circle(Shape):
    pass

print(issubclass(Square, Rectangle))


