import math

# ввід
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

# перевірка, чи це квадратне рівняння
if a == 0:
    print("Це не квадратне рівняння (a = 0).")
else:
    # дискримінанта
    D = b**2 - 4*a*c
    print(f"Дискримінант D = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Рівняння має два корені: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"Рівняння має один корінь: x = {x}")
    else:
        print("Рівняння не має дійсних коренів.")