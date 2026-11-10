
import tkinter as tk
from tkinter import ttk


class OneTimePadGUI:

    def __init__(self, root):
        self.root = root

        self.root.title("One-Time Pad")
        self.root.geometry("900x700")

        self.create_widgets()

    def create_widgets(self):

        # Mode
        ttk.Label(
            self.root,
            text="Mode:"
        ).pack(
            anchor="w",
            padx=10,
            pady=(10, 0)
        )

        self.mode_var = tk.StringVar(value="Encrypt")

        self.mode_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.mode_var,
            values=["Encrypt", "Decrypt"],
            state="readonly"
        )

        self.mode_dropdown.pack(
            fill="x",
            padx=10
        )

        # Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        self.generate_button = ttk.Button(
            button_frame,
            text="Generate Random Key"
        )

        self.generate_button.pack(
            side="left",
            padx=5
        )

        self.process_button = ttk.Button(
            button_frame,
            text="Process"
        )

        self.process_button.pack(
            side="left",
            padx=5
        )

        # Panes
        self.paned_window = ttk.PanedWindow(
            self.root,
            orient="vertical"
        )

        self.paned_window.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # Message, Key, and Output
        self.message_box = self.create_text_pane("Message:")
        self.key_box = self.create_text_pane("Key:")
        self.output_box = self.create_text_pane("Output:")

    def create_text_pane(self, label_text):

        frame = ttk.Frame(self.paned_window)

        ttk.Label(
            frame,
            text=label_text
        ).pack(anchor="w")

        text_frame = ttk.Frame(frame)

        text_frame.pack(
            fill="both",
            expand=True
        )

        text_box = tk.Text(text_frame)

        text_box.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            text_frame,
            orient="vertical",
            command=text_box.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        text_box.configure(
            yscrollcommand=scrollbar.set
        )

        self.paned_window.add(
            frame,
            weight=1
        )

        return text_box
