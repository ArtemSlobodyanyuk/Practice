from abc import ABC, abstractmethod


# ===== Абстракція + Наслідування =====
class Animal(ABC):
    def __init__(self, name):
        self._name = name  # інкапсуляція

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass


# ===== Поліморфізм =====
class Lion(Animal):
    def make_sound(self):
        return "Р-р-р!"

    def eat(self):
        return "Лев їсть м'ясо"


class Elephant(Animal):
    def make_sound(self):
        return "Тру-у-у!"

    def eat(self):
        return "Слон їсть траву"


# ===== Окремий клас для взаємодії =====
class Keeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal: Animal):
        print(f"{self.name} годує {animal._name}: {animal.eat()}")

    def listen_animal(self, animal: Animal):
        print(f"{animal._name} каже: {animal.make_sound()}")

lion = Lion("Сімба")
elephant = Elephant("Дамбо")

keeper = Keeper("Олексій")

animals = [lion, elephant]

for animal in animals:
    keeper.feed_animal(animal)
    keeper.listen_animal(animal)
