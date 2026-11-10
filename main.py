import tkinter as tk

from gui import OneTimePadGUI
from controller import OneTimePadController

if __name__ == "__main__":
    root = tk.Tk()

    gui = OneTimePadGUI(root)

    controller = OneTimePadController(gui)

    root.mainloop()
