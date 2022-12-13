from tkinter import messagebox

import tkinter
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *



class InfoWindow(tk.Toplevel):
    def __init__(self, root, categories):
        super().__init__(root)
        self.minsize(500, 550)
        self.title("Ubuntu Weaponizer")

        self.configure(bg="LightSkyBlue2",
                       cursor="target",  # cursor
                       relief="flat",  # relieve root
                       bd=5)

        Label(self, text=" Curious about the apps we offer uwu)?", bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15)) \
            .pack(side=TOP, pady=10)

        normalF = Text(font=('DejaVu Sans Mono', 10))
        specialF = Text(font=('DejaVu Sans Mono', 15, "bold"))

        Label(self, text="--Categories--", font=specialF, bg="navajo white").pack(pady=10)

        # Variables de posición de las apps
        l = 60
        k = 330
        m = 60
        n = 60
        o = True

        # Poner las apps y los checkbox
        for item in categories:
            if (o):
                m += 40
                Label(self, text=item[0], font=specialF, bg="navajo white").place(x=l, y=m)
                m += 20
            else:
                n += 40
                Label(self, text=item[0], font=specialF, bg="navajo white").place(x=k, y=n)
                n += 20
            for subItem in item[1]:
                if (o):
                    m += 25
                    Label(self, text=subItem, font= normalF).place(x=l, y = m)
                else:
                    n += 25
                    Label(self, text=subItem, font= normalF).place(x=k, y = n)
            o = not o

        botExit = tk.Button(self, text="Exit", width=10, bg="navajo white",
                            font=('DejaVu Sans Mono', 10), command=self.destroy)
        botExit.pack(side=BOTTOM, pady=10)






