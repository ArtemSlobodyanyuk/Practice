import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import json
import os

# ===== ФАЙЛ КОНФІГУРАЦІЇ =====
CONFIG_FILE = "../config.json"

# ===== КОЛЬОРИ ТЕМНОЇ ТЕМИ =====
BG_COLOR_DEFAULT = "#1e1e1e"
FG_COLOR = "#ffffff"
ENTRY_BG = "#2b2b2b"
BTN_BG = "#3a3a3a"

# ===== ЗАВАНТАЖЕННЯ КОНФІГУРАЦІЇ =====
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
        BG_COLOR = config.get("bg_color", BG_COLOR_DEFAULT)
else:
    BG_COLOR = BG_COLOR_DEFAULT

# ===== ВІКНО =====
window = tk.Tk()
window.title("Програма з вкладками")
window.geometry("500x400")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

# ===== ЗМІННІ =====
name_var = tk.StringVar()
age_var = tk.StringVar()

# ===== СТИЛІ TTK =====
style = ttk.Style()
style.theme_use("default")

style.configure("TNotebook", background=BG_COLOR)
style.configure("TNotebook.Tab", background=BTN_BG, foreground=FG_COLOR)
style.map("TNotebook.Tab",
          background=[("selected", BG_COLOR)],
          foreground=[("selected", FG_COLOR)])

# ===== Notebook =====
notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# ===== Вкладки =====
tabs = {}

# --- Головна ---
tab_main = tk.Frame(notebook, bg=BG_COLOR)
tabs["Головна"] = tab_main
notebook.add(tab_main, text="Головна")

tk.Label(tab_main, text="Ім'я:", bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(tab_main, textvariable=name_var, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR).grid(row=0, column=1, padx=10, pady=10)

tk.Label(tab_main, text="Вік:", bg=BG_COLOR, fg=FG_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(tab_main, textvariable=age_var, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR).grid(row=1, column=1, padx=10, pady=10)

def save_data():
    name = name_var.get()
    age = age_var.get()
    messagebox.showinfo("Введені дані", f"Ім'я: {name}\nВік: {age}")

tk.Button(tab_main, text="Зберегти", command=save_data, bg=BTN_BG, fg=FG_COLOR, borderwidth=0).grid(row=2, column=0, columnspan=2, pady=20)

# --- Налаштування ---
tab_settings = tk.Frame(notebook, bg=BG_COLOR)
tabs["Налаштування"] = tab_settings
notebook.add(tab_settings, text="Налаштування")

tk.Label(tab_settings, text="Колір фону:", bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)

def choose_color():
    global BG_COLOR
    color_code = colorchooser.askcolor(title="Оберіть колір фону", initialcolor=BG_COLOR)[1]
    if color_code:
        BG_COLOR = color_code
        # Зміна фону всіх вкладок
        for tab in tabs.values():
            tab.configure(bg=BG_COLOR)
            # Перевстановлюємо bg для всіх Label/Entry/Button у вкладках
            for widget in tab.winfo_children():
                if isinstance(widget, tk.Label) or isinstance(widget, tk.Entry) or isinstance(widget, tk.Button):
                    widget.configure(bg=BG_COLOR if isinstance(widget, tk.Label) else ENTRY_BG, fg=FG_COLOR)
        # Збереження
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"bg_color": BG_COLOR}, f)

tk.Button(tab_settings, text="Вибрати колір", command=choose_color, bg=BTN_BG, fg=FG_COLOR, borderwidth=0).pack()

# --- Про програму ---
tab_about = tk.Frame(notebook, bg=BG_COLOR)
tabs["Про програму"] = tab_about
notebook.add(tab_about, text="Про програму")

info_text = (
    "Автор: The Creative Core\n"
    "Програма: Приклад роботи з вкладками\n"
    "Тема: Створити програму з кількома вкладками (Notebook), \n"
    "які мають назви «Головна», «Налаштування» та «Про програму». \n"
    "У вкладці «Головна» розмістити форму введення даних, \n"
    "у «Налаштування» — вибір кольору фону за допомогою colorchooser, \n"
    "а у вкладці «Про програму» — інформацію про автора. \n"
    "Реалізувати збереження вибраного кольору при повторному запуску."
)
tk.Label(tab_about, text=info_text, bg=BG_COLOR, fg=FG_COLOR, justify="left").pack(padx=20, pady=20, anchor="nw")

# ===== ЗАПУСК =====
window.mainloop()
