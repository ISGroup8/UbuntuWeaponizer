from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *

class ContactWindow(tk.Toplevel):
    def __init__(self, root, formatos):
        super().__init__(root)
        self.minsize(500, 300)
        self.title("Ubuntu Weaponizer/ContactUs")

        self.configure(bg=formatos['fondo1'], # backgound
                        cursor=formatos['cursor'], # cursor
                        relief="flat", # relieve root
                        bd=5) #borde en px

        Label(self, text="Want to contact us?", bg=formatos['fondo1'], font=formatos['specialF'], fg=formatos['colorFontS']) \
            .pack(side=TOP, pady=10)

        Label(self, text="Email:", font=formatos['specialF'], bg=formatos['fondo1'],fg=formatos['colorFontS']).pack(pady=15)
        Label(self, text="ubuntu_weaponizer@example.com", font=formatos['normalF'], bg=formatos['fondo1'],fg=formatos['colorFontN']).pack()

        Label(self, text="Phone:", font=formatos['specialF'], bg=formatos['fondo1'],fg=formatos['colorFontS']).pack(pady=15)
        Label(self, text="(+34)12-312-31-23", font=formatos['normalF'], bg=formatos['fondo1'],fg=formatos['colorFontN']).pack()

        botExit = tk.Button(self, text="Go back", width=10, bg=formatos['no'],fg=formatos['colorFontN'],
                            font=formatos['normalF'], command=self.destroy)
        botExit.pack(side=BOTTOM, pady=10)

