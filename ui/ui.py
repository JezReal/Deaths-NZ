import tkinter as tk
from tkinter import ttk


def run():
    root = tk.Tk()

    root.tk.call('source', 'theme/forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')
    root.geometry('1080x720')
    root.title('Python project baby')

    button = ttk.Button(root, style='Accent.TButton', text='I\'m a themed button')
    button.pack(pady=20)

    root.mainloop()
