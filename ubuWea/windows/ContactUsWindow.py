from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *

class ContactWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.minsize(500, 300)
        self.title("Ubuntu Weaponizer")

        self.configure(bg="LightSkyBlue2",
                       cursor="target",  # cursor
                       relief="flat",  # relieve root
                       bd=5)

        Label(self, text=" Want to contact us 0^0)?", bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15)) \
            .pack(side=TOP, pady=10)

        normalF = Text(font=('DejaVu Sans Mono', 10))
        specialF = Text(font=('DejaVu Sans Mono', 15, "bold"))

        Label(self, text="Email:", font=specialF, bg="navajo white").pack(pady=15)
        Label(self, text="ubuntu_weaponizer@example.com", font=normalF, bg="navajo white").pack()

        Label(self, text="Phone:", font=specialF, bg="navajo white").pack(pady=15)
        Label(self, text="(+34)12-312-31-23", font=normalF, bg="navajo white").pack()

        botExit = tk.Button(self, text="Exit", width=10, bg="navajo white",
                            font=('DejaVu Sans Mono', 10), command=self.destroy)
        botExit.pack(side=BOTTOM, pady=10)

