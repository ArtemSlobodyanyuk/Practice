import pandas as pd

# зчитування даних з файлу
df = pd.read_csv("students.csv")

# список колонок з оцінками
subjects = ["sub1", "sub2", "sub3", "sub4", "sub5"]

# середній бал кожного студента
df["average"] = df[subjects].mean(axis=1)

# вивід
print("\nТаблиця студентів із середнім балом:")
print(df[["name", "surname", "average"]])

# середній бал групи з кожної дисципліни
print("\nСередній бал групи з дисциплін:")
group_averages = df[subjects].mean()

for subject, avg in group_averages.items():
    print(f"{subject}: {avg:.2f}")