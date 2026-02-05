import math

g = 9.81  # прискорення вільного падіння

# ввід
v0 = float(input("Введіть початкову швидкість (м/с): "))
angle_deg = float(input("Введіть кут вильоту (градуси): "))

# переведення кута в радіани
angle_rad = math.radians(angle_deg)

# обчислення параметрів
time_flight = (2 * v0 * math.sin(angle_rad)) / g
range_flight = (v0 ** 2 * math.sin(2 * angle_rad)) / g
max_height = (v0 ** 2 * (math.sin(angle_rad) ** 2)) / (2 * g)

print(f"\nЧас польоту: {time_flight:.2f} с")
print(f"Дальність польоту: {range_flight:.2f} м")
print(f"Максимальна висота: {max_height:.2f} м\n")

print("Висота снаряда по секундах:")

t = 0
while t <= time_flight:
    height = v0 * math.sin(angle_rad) * t - (g * t ** 2) / 2
    if height < 0:
        height = 0
    print(f"t = {t:>2} с → h = {height:.2f} м")
    t += 1