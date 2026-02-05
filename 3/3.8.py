import tkinter as tk
from tkinter import ttk, colorchooser, filedialog


class GraphicsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графіка")
        self.root.geometry("800x500")
        self.root.configure(bg="#1e1e1e")  # dark theme

        self.current_color = "#ffffff"
        self.current_tool = "line"
        self.start_x = None
        self.start_y = None
        self.temp_item = None

        self.create_ui()

    def create_ui(self):
        control_frame = tk.Frame(self.root, bg="#1e1e1e")
        control_frame.pack(side="top", fill="x", padx=5, pady=5)

        ttk.Button(control_frame, text="Лінія", command=lambda: self.set_tool("line")).pack(side="left", padx=5)
        ttk.Button(control_frame, text="Коло", command=lambda: self.set_tool("oval")).pack(side="left", padx=5)
        ttk.Button(control_frame, text="Колір", command=self.choose_color).pack(side="left", padx=5)
        ttk.Button(control_frame, text="Очистити", command=self.clear_canvas).pack(side="left", padx=5)
        ttk.Button(control_frame, text="Зберегти (.ps)", command=self.save_canvas).pack(side="left", padx=5)

        self.canvas = tk.Canvas(
            self.root,
            width=600,
            height=400,
            bg="#252526",
            highlightthickness=0
        )
        self.canvas.pack(pady=10)

        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def set_tool(self, tool):
        self.current_tool = tool

    def choose_color(self):
        color = colorchooser.askcolor(title="Вибір кольору")
        if color[1]:
            self.current_color = color[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".ps",
            filetypes=[("PostScript files", "*.ps")]
        )
        if file_path:
            self.canvas.postscript(file=file_path)

    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_move(self, event):
        if self.temp_item:
            self.canvas.delete(self.temp_item)

        if self.current_tool == "line":
            self.temp_item = self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y,
                fill=self.current_color, width=2
            )
        elif self.current_tool == "oval":
            self.temp_item = self.canvas.create_oval(
                self.start_x, self.start_y, event.x, event.y,
                outline=self.current_color, width=2
            )

    def on_mouse_up(self, event):
        self.temp_item = None


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicsApp(root)
    root.mainloop()