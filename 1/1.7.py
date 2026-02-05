SUBJECTS_COUNT = 5

# ввід кількості студентів
n = int(input("Введіть кількість студентів: "))

students = []

# ввід даних про студентів
for i in range(n):
    print(f"\nСтудент {i + 1}")
    name = input("Ім'я: ")
    surname = input("Прізвище: ")

    grades = []
    for j in range(SUBJECTS_COUNT):
        grade = float(input(f"Оцінка з дисципліни {j + 1}: "))
        grades.append(grade)

    students.append({
        "name": name,
        "surname": surname,
        "grades": grades
    })

# вивід
print("\nТаблиця студентів:")
print("-" * 70)
print(f"{'Імʼя':<10}{'Прізвище':<15}{'Сер. бал':<10}")
print("-" * 70)

for student in students:
    avg_student = sum(student["grades"]) / SUBJECTS_COUNT
    print(f"{student['name']:<10}{student['surname']:<15}{avg_student:<10.2f}")

print("-" * 70)

# обчислення середнього балу групи з кожної дисципліни
print("\nСередній бал групи з дисциплін:")

for i in range(SUBJECTS_COUNT):
    subject_sum = 0
    for student in students:
        subject_sum += student["grades"][i]

    subject_avg = subject_sum / n
    print(f"Дисципліна {i + 1}: {subject_avg:.2f}")