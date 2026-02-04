import tkinter as tk

# кольори темної теми
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
BTN_COLOR = "#2d2d2d"
BTN_HOVER = "#3a3a3a"

# створення вікна
window = tk.Tk()
window.title("Події та кнопки")
window.geometry("400x220")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

# напис
label = tk.Label(
    window,
    text="",
    font=("Arial", 16),
    bg=BG_COLOR,
    fg=FG_COLOR
)
label.pack(pady=20)

# обробники подій
def greet():
    label.config(text="Вітаю, користувач!")

def clear_text():
    label.config(text="")

def exit_program():
    window.destroy()

# кнопки
def create_button(text, command):
    btn = tk.Button(
        window,
        text=text,
        command=command,
        width=15,
        bg=BTN_COLOR,
        fg=FG_COLOR,
        activebackground=BTN_HOVER,
        activeforeground=FG_COLOR,
        borderwidth=0
    )
    return btn

btn_greet = create_button("Привітати", greet)
btn_clear = create_button("Очистити", clear_text)
btn_exit = create_button("Вийти", exit_program)

# розміщення
btn_greet.pack(pady=5)
btn_clear.pack(pady=5)
btn_exit.pack(pady=5)

# запуск
window.mainloop()
