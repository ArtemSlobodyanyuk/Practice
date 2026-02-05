import math

# функції для обчислення площі
def rectangle_area(width, height):
    return width * height
def circle_area(radius):
    return math.pi * radius ** 2

print("Процедурний підхід:")
print("Площа прямокутника 5x10:", rectangle_area(5, 10))
print("Площа кола з радіусом 3:", circle_area(3))


# базовий клас фігури
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

print("\nОб’єктно-орієнтований підхід:")
rect = Rectangle(10, 15)
circle = Circle(5)

print("Площа прямокутника:", rect.area())
print("Площа кола:", circle.area())