# ввід довжини масиву
n = int(input("Введіть кількість елементів масиву: "))

arr = []

# Ввід елементів масиву
for i in range(n):
    value = float(input(f"Елемент {i + 1}: "))
    arr.append(value)

print("\nПочатковий масив:")
print(arr)

# бульбашкове сортування
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("\nВідсортований масив:")
print(arr)