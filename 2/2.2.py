class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self):
        print(f"Ім’я: {self.name}")
        print(f"Група: {self.group}")
        print(f"Середній бал: {self.average_grade}")
        print("-" * 20)


# Створення об’єктів
student1 = Student("Іван Петренко", "КН-21", 4.5)
student2 = Student("Олена Коваль", "КН-21", 4.8)
student3 = Student("Андрій Шевченко", "КН-22", 4.2)

# Виведення інформації
student1.show_info()
student2.show_info()
student3.show_info()
