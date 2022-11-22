import tkinter
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *


class Checkbox(ttk.Checkbutton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = tk.BooleanVar(self)
        self.configure(variable=self.variable)

    def checked(self):
        return self.variable.get()

    def check(self):
        self.variable.set(True)

    def uncheck(self):
        self.variable.set(False)


class UpdateWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.minsize(500, 550)
        self.title("Ubuntu Weaponizer")

        self.configure(bg="LightSkyBlue2",
                       cursor="target",  # cursor
                       relief="flat",  # relieve root
                       bd=5)

        Label(self, text=" Update the things you want owo)", bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15)) \
            .pack(side=TOP, pady=10)

        normalF = Text(font=('DejaVu Sans Mono', 10))
        specialF = Text(font=('DejaVu Sans Mono', 15, "bold"))

        # List of apps
        Label(self, text="--Categories--", font=specialF, bg="navajo white").pack(pady=10)
        # phising = {'SET': False, 'SocialPhish':False, 'Hidden-Eye':False, 'ShellPhish':False, 'PyPhisher':False}
        phising = ['SET', 'SocialPhish', 'Hidden-Eye', 'ShellPhish', 'PyPhisher']
        Web = ['Nmap', 'BurpSuite', 'FFUF', 'RustScan', 'WPSCAN']
        Forense = ['Autopsy', 'Metagoofil', 'Exiftool', 'Wireshark']
        osint = ['Void']
        pwn = ['void']
        categories = [('Phising', phising), ('Web', Web), ('Forense', Forense), ('OSINT', osint), ('PWN', pwn)]

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
                self.checkbox = Checkbox(self, text=subItem
                                         , command=lambda: self.check_clicked())

                if (o):
                    m += 25
                    self.checkbox.place(x=l, y=m)
                else:
                    n += 25
                    self.checkbox.place(x=k, y=n)

            o = not o

        botExit = tk.Button(self, text="Exit", width=10, bg="navajo white",
                            font=('DejaVu Sans Mono', 10), command=self.destroy)
        botExit.pack(side=BOTTOM, pady=10)

    def check_clicked(self):
        window = tk.Toplevel(self)
        window.minsize(200, 100)
        window.title("")
        window.configure(bg="navajo white",
                         cursor="target",  # cursor
                         relief="flat",  # relieve root
                         bd=5)
        Label(window, text="-- App updated --", font=('DejaVu Sans Mono', 15, "bold"),
              bg="LightSkyBlue2").pack(side=TOP, pady=25)

        window.after(2000, lambda: window.destroy())





