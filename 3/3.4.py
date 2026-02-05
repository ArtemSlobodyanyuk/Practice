import tkinter as tk

# ===== ТЕМНА ТЕМА =====
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
ENTRY_BG = "#2b2b2b"
BTN_BG = "#3a3a3a"
ERROR_COLOR = "#ff6b6b"

# ===== ВІКНО =====
window = tk.Tk()
window.title("Калькулятор")
window.geometry("600x200")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

# ===== ЗМІННІ =====
num1_var = tk.StringVar()
num2_var = tk.StringVar()
operation_var = tk.StringVar(value="+")
result_var = tk.StringVar()

# ===== ЛОГІКА =====
def calculate():
    try:
        a = float(num1_var.get())
        b = float(num2_var.get())
        op = operation_var.get()

        if op == "+":
            r = a + b
        elif op == "-":
            r = a - b
        elif op == "*":
            r = a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError
            r = a / b

        result_var.set(r)
        result_label.config(fg=FG_COLOR)

    except ValueError:
        result_var.set("Помилка")
        result_label.config(fg=ERROR_COLOR)
    except ZeroDivisionError:
        result_var.set("Ділення на 0")
        result_label.config(fg=ERROR_COLOR)

# інтерфейс

tk.Entry(
    window, textvariable=num1_var,
    bg=ENTRY_BG, fg=FG_COLOR,
    insertbackground=FG_COLOR,
    width=10, justify="center"
).grid(row=0, column=0, padx=5, pady=40)

# OptionMenu
operation_menu = tk.OptionMenu(
    window,
    operation_var,
    "+", "-", "*", "/"
)
operation_menu.config(
    bg=BTN_BG,
    fg=FG_COLOR,
    activebackground=BTN_BG,
    borderwidth=0,
    width=3
)
operation_menu["menu"].config(
    bg=BTN_BG,
    fg=FG_COLOR
)
operation_menu.grid(row=0, column=1)

tk.Entry(
    window, textvariable=num2_var,
    bg=ENTRY_BG, fg=FG_COLOR,
    insertbackground=FG_COLOR,
    width=10, justify="center"
).grid(row=0, column=2, padx=5)

tk.Label(
    window, text="=",
    bg=BG_COLOR, fg=FG_COLOR,
    font=("Arial", 16)
).grid(row=0, column=3, padx=10)

result_label = tk.Label(
    window, textvariable=result_var,
    bg=ENTRY_BG, fg=FG_COLOR,
    width=12, font=("Arial", 14),
    relief="solid"
)
result_label.grid(row=0, column=4)

tk.Button(
    window, text="Обчислити",
    command=calculate,
    bg=BTN_BG, fg=FG_COLOR,
    borderwidth=0, width=20
).grid(row=1, column=0, columnspan=5, pady=10)

window.mainloop()
