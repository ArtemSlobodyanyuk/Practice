class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} видає звук: {self.make_sound()}")

    def make_sound(self):
        return "невідомий звук"

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав"

class Cat(Animal):
    def make_sound(self):
        return "Мяу"

class Cow(Animal):
    def make_sound(self):
        return "Му-у"

animals = [
    Dog("Собака"),
    Cat("Кіт"),
    Cow("Корова")
]

for animal in animals:
    animal.sound()