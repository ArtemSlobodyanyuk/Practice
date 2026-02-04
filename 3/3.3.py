import tkinter as tk

# кольори темної теми
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
ENTRY_BG = "#2b2b2b"
BTN_BG = "#3a3a3a"
BORDER = "#555555"

# вікно
window = tk.Tk()
window.title("Анкета користувача")
window.geometry("420x360")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

# змінні
name_var = tk.StringVar()
gender_var = tk.StringVar(value="Чоловіча")
agree_var = tk.BooleanVar()

# функція
def save_data():
    name = name_var.get()
    gender = gender_var.get()
    agree = "Так" if agree_var.get() else "Ні"

    result_label.config(
        text=f"Ім'я: {name}\nСтать: {gender}\nПогодження з умовами: {agree}"
    )

# інтерфейс

# ім'я
tk.Label(
    window, text="Ім'я:",
    bg=BG_COLOR, fg=FG_COLOR
).grid(row=0, column=0, sticky="w", padx=10, pady=10)

tk.Entry(
    window,
    textvariable=name_var,
    bg=ENTRY_BG,
    fg=FG_COLOR,
    insertbackground=FG_COLOR,
    width=28
).grid(row=0, column=1, padx=10)

# стать
tk.Label(
    window, text="Стать:",
    bg=BG_COLOR, fg=FG_COLOR
).grid(row=1, column=0, sticky="w", padx=10, pady=10)

tk.Radiobutton(
    window, text="Чоловіча",
    variable=gender_var, value="Чоловіча",
    bg=BG_COLOR, fg=FG_COLOR,
    selectcolor=BG_COLOR,
    activebackground=BG_COLOR
).grid(row=1, column=1, sticky="w")

tk.Radiobutton(
    window, text="Жіноча",
    variable=gender_var, value="Жіноча",
    bg=BG_COLOR, fg=FG_COLOR,
    selectcolor=BG_COLOR,
    activebackground=BG_COLOR
).grid(row=2, column=1, sticky="w")

# погодження
tk.Checkbutton(
    window,
    text="Погоджуюсь із умовами",
    variable=agree_var,
    bg=BG_COLOR, fg=FG_COLOR,
    selectcolor=BG_COLOR,
    activebackground=BG_COLOR
).grid(row=3, column=1, sticky="w", pady=10)

# кнопка
tk.Button(
    window,
    text="Зберегти",
    command=save_data,
    bg=BTN_BG,
    fg=FG_COLOR,
    width=20,
    borderwidth=0
).grid(row=4, column=1, pady=10)

# результат
tk.Label(
    window, text="Введена інформація:",
    bg=BG_COLOR, fg=FG_COLOR
).grid(row=5, column=0, sticky="nw", padx=10, pady=10)

result_label = tk.Label(
    window,
    text="",
    bg=ENTRY_BG,
    fg=FG_COLOR,
    justify="left",
    anchor="nw",
    width=32,
    height=5,
    relief="solid",
    borderwidth=1
)
result_label.grid(row=5, column=1, padx=10, pady=10)

# запуск
window.mainloop()
