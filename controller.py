import tkinter as tk
from tkinter import messagebox
import string
import encryption


class OneTimePadController:

    def __init__(self, gui):
        self.gui = gui

        self.gui.generate_button.configure(command=self.generate_key)

        self.gui.process_button.configure(command=self.process)

    def generate_key(self):
        message = encryption.clean_text(self.gui.message_box.get("1.0", tk.END).strip())

        if not message:
            messagebox.showerror("Error", "Enter a message first.")
            return

        if not all(c in string.ascii_uppercase for c in message):
            messagebox.showerror("Error", "Message must contain only A-Z and spaces.")
            return

        key = encryption.generate_key(len(message))

        self.gui.key_box.delete("1.0", tk.END)
        self.gui.key_box.insert("1.0", key)

    def process(self):

        message = encryption.clean_text(self.gui.message_box.get("1.0", tk.END).strip())

        key = encryption.clean_text(self.gui.key_box.get("1.0", tk.END).strip())

        if not message:
            messagebox.showerror("Error", "Enter a message.")
            return

        if not key:
            messagebox.showerror("Error", "Enter a key.")
            return

        if not all(c in string.ascii_uppercase for c in message):
            messagebox.showerror("Error", "Message must contain only A-Z and spaces.")
            return

        if not all(c in string.ascii_uppercase for c in key):
            messagebox.showerror("Error", "Key must contain only A-Z.")
            return

        if len(key) != len(message):
            messagebox.showerror("Error", "The key must be the same length as the message.")
            return

        mode = self.gui.mode_var.get()

        if mode == "Encrypt":
            result = encryption.encrypt(message, key)
        else:
            result = encryption.decrypt(message, key)

        self.gui.output_box.delete("1.0", tk.END)
        self.gui.output_box.insert("1.0", result)
