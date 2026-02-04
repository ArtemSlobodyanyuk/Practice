import tkinter as tk
from tkinter import filedialog, messagebox

# ===== КОЛЬОРИ ТЕМНОЇ ТЕМИ =====
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
TEXT_BG = "#2b2b2b"
TEXT_FG = "#ffffff"
BTN_BG = "#3a3a3a"

# ===== ГЛОБАЛЬНІ ЗМІННІ =====
current_file = None
is_saved = True  # прапорець, чи були зміни

# ===== ФУНКЦІЇ =====
def new_file():
    global current_file, is_saved
    if not is_saved:
        if not ask_save_changes():
            return
    text_area.delete("1.0", tk.END)
    current_file = None
    window.title("Блокнот")
    is_saved = True

def open_file():
    global current_file, is_saved
    if not is_saved:
        if not ask_save_changes():
            return
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, text)
        current_file = file_path
        window.title(f"Блокнот - {current_file}")
        is_saved = True

def save_file():
    global current_file, is_saved
    if current_file is None:
        save_as()
    else:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))
        is_saved = True

def save_as():
    global current_file, is_saved
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))
        current_file = file_path
        window.title(f"Блокнот - {current_file}")
        is_saved = True

def exit_app():
    if not is_saved:
        if not ask_save_changes():
            return
    window.destroy()

def ask_save_changes():
    response = messagebox.askyesnocancel(
        "Зберегти зміни?",
        "У файлі є незбережені зміни. Зберегти перед виходом?"
    )
    if response:  # Так
        save_file()
        return True
    elif response is False:  # Ні
        return True
    else:  # Скасувати
        return False

def on_text_change(event=None):
    global is_saved
    is_saved = False

# ===== ВІКНО =====
window = tk.Tk()
window.title("Блокнот")
window.geometry("600x500")
window.configure(bg=BG_COLOR)

# ===== ТЕКСТОВЕ ПОЛЕ =====
text_area = tk.Text(window, bg=TEXT_BG, fg=TEXT_FG, insertbackground=FG_COLOR)
text_area.pack(fill=tk.BOTH, expand=True)
text_area.bind("<<Modified>>", on_text_change)

# ===== МЕНЮ =====
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0, bg=BG_COLOR, fg=FG_COLOR)
file_menu.add_command(label="Новий", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_command(label="Зберегти як...", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=exit_app)

menu_bar.add_cascade(label="Файл", menu=file_menu)

# ===== ОБРОБКА ЗАКРИТТЯ ВІКНА =====
window.protocol("WM_DELETE_WINDOW", exit_app)

window.mainloop()
