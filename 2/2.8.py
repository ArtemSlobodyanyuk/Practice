from abc import ABC, abstractmethod
import math

# Абстрактний клас
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Коло
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Прямокутник
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Приклад використання
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Площа кола:", circle.area())
print("Площа прямокутника:", rectangle.area())
