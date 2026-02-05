from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} видає звук: {self.make_sound()}")

    @abstractmethod
    def make_sound(self):
        pass

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