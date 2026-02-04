import tkinter as tk
from tkinter import ttk
from logic import process_text

class MainWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Модульна програма")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e1e")  # dark theme

        self._create_widgets()

    def _create_widgets(self):
        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.text_input = tk.Text(
            frame,
            height=10,
            bg="#252526",
            fg="white",
            insertbackground="white"
        )
        self.text_input.pack(fill="x", pady=5)

        btn = ttk.Button(frame, text="Обробити", command=self.on_process)
        btn.pack(pady=5)

        self.result_label = tk.Label(
            frame,
            text="",
            bg="#1e1e1e",
            fg="#9cdcfe",
            justify="left"
        )
        self.result_label.pack(anchor="w", pady=5)

    def on_process(self):
        text = self.text_input.get("1.0", tk.END)
        result = process_text(text)  # ← виклик логіки
        self.result_label.config(text=result)