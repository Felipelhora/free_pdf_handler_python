import tkinter as tk
from src.views.AppMain import AppMain


if __name__ == "__main__":
    root = tk.Tk()
    app = AppMain(root)
    root.mainloop()