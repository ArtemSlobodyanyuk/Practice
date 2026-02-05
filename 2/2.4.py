class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        if km > 0:
            self.mileage += km
        else:
            print("Пробіг повинен збільшуватися на додатне число")

    def info(self):
        print(f"Марка: {self.brand}")
        print(f"Рік випуску: {self.year}")
        print(f"Пробіг: {self.mileage} км")

    def __str__(self):
        return f"{self.brand} ({self.year}), пробіг: {self.mileage} км"

car1 = Car("Toyota", 2018, 50000)
car2 = Car("BMW", 2020, 30000)

car1.drive(150)
car2.drive(500)

car1.info()
print(car1)

print()
car2.info()
print(car2)
