def factorial(n):
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід’ємних чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ввід
number = int(input("Введіть число: "))

try:
    result = factorial(number)
    print(f"Факторіал числа {number} = {result}")
except ValueError as e:
    print(e)