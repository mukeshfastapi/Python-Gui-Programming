# Introduce polymorphism

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangel(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(5), Square(6), Triangel(5, 7)]

for shape in shapes:
    print(shape.area())

print()

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.toppint = topping


shapes = [Circle(5), Square(6), Triangel(5, 7), Pizza('Peporoni', 12)]

for shape in shapes:
    print(shape.area())