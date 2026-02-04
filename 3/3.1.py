import tkinter as tk

# створення головного вікна
window = tk.Tk()
window.title("Перша програма")

# фіксований розмір 1024x768
window.geometry("1024x768")
window.resizable(False, False)

# напис "Hello, world!"
label = tk.Label(window, text="Hello, world!", font=("Arial", 24))
label.pack(pady=50)

# кнопка "Закрити"
close_button = tk.Button(window, text="Закрити", command=window.destroy)
close_button.pack()

# запуск програми
window.mainloop()
