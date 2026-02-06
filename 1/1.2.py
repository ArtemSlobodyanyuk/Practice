def number_to_string(n):
    # обробка нуля
    if n == 0:
        return "0"

    result = ""
    negative = False

    # перевірка на від’ємне число
    if n < 0:
        negative = True
        n = -n

    # основний цикл
    while n > 0:
        digit = n % 10
        result = chr(ord('0') + digit) + result
        n //= 10

    # додаємо знак мінус, якщо потрібно
    if negative:
        result = "-" + result

    return result


# ввід
number = int(input("Введіть число: "))
print("Рядкове представлення:", number_to_string(number))