# вхідні дані
students_grades = {
    "Іван": [5, 4, 4, 5],
    "Олена": [5, 5, 4, 5],
    "Андрій": [3, 4, 4, 4]
}

average_dict = {}      # {ім’я: середній_бал}
all_grades = []        # список усіх оцінок

# обчислення середнього балу
for name, grades in students_grades.items():
    average = sum(grades) / len(grades)
    average_dict[name] = round(average, 2)
    all_grades.extend(grades)

# унікальні оцінки
unique_grades = set(all_grades)

# вивід
print("Середній бал кожного студента:")
for name, avg in average_dict.items():
    print(f"{name}: {avg}")

print("\nУнікальні оцінки:", unique_grades)
print("Загальний середній бал:",
      round(sum(all_grades) / len(all_grades), 2))
