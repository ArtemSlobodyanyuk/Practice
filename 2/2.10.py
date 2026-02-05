from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self._name = name
        self.weight = weight  # виклик setter

    # властивість weight
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Вага тварини не може бути від’ємною")
        self._weight = value

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass


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


class Keeper:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience  # setter

    # властивість experience
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            raise ValueError("Стаж доглядальника не може бути від’ємним")
        self._experience = value

    def feed_animal(self, animal: Animal):
        print(f"{self.name} годує {animal._name} ({animal.weight} кг): {animal.eat()}")

lion = Lion("Сімба", 190)
keeper = Keeper("Олексій", 5)

print(lion.weight)
lion.weight = 200