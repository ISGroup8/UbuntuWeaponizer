
import tkinter as tk
from tkinter import *

import functions

class InstallWindow (tk.Toplevel):

    def __init__(self, root, categories):
        super().__init__(root)
        self.minsize(500,550)
        self.title("Ubuntu Weaponizer")

        self.configure(bg="LightSkyBlue2",
                        cursor="target",  # cursor
                        relief="flat",  # relieve root
                        bd=5)

        Label(self, text=" Install the things you want :)", bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15)) \
            .pack(side=TOP, pady=10)

        normalF = Text(font=('DejaVu Sans Mono', 10))
        specialF = Text(font=('DejaVu Sans Mono', 15, "bold"))

        # List of apps
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
                self.checkbox = Checkbutton (self, text= subItem[0], font=normalF,
                                             variable= subItem[1], onvalue= True, offvalue= False,
                                             command=lambda: self.check_clicked(categories))

                if (o):
                    m += 25
                    self.checkbox.place(x=l, y=m)
                else:
                    n += 25
                    self.checkbox.place(x=k, y=n)

            o = not o

        botExit = tk.Button(self, text="Exit and install", width=10, bg="navajo white",
                            font=('DejaVu Sans Mono', 10), command=lambda: self.exitAndInstall(categories))
        botExit.pack(side=BOTTOM, pady=10)




    def check_clicked(self, categories):
        window = tk.Toplevel(self)
        window.minsize(200,100)
        window.title("")
        window.configure(bg="navajo white",
                       cursor="target",  # cursor
                       relief="flat",  # relieve root
                       bd=5)
        Label(window,text="-- App added --", font=('DejaVu Sans Mono', 15, "bold"),
              bg="LightSkyBlue2").pack(side=TOP, pady = 25)

        for item in categories:
            for subItem in item[1]:
                if subItem[1].get():
                    Label(window, text=subItem[0], font=('DejaVu Sans Mono', 15, "bold"), bg="LightSkyBlue2").pack(
                        side=TOP)

                    ## Aqui va la funcion de instalación
                    ## subItem[0]= nombre app / subItem[1].get()=booleano de si está marcado o no

        window.after(2000, lambda :window.destroy())

    
    def exitAndInstall(self, categories):
        window = tk.Toplevel(self)
        window.minsize(200,100)
        window.title("")
        window.configure(bg="navajo white",
                        cursor="target",
                        relief="flat",
                        bd=5)
        Label(window,text="-- Apps are being installed please wait, you will be notified when everything's done.", 
        font=('DejaVu Sans Mono', 15, "bold"), bg="LightSkyBlue2").pack(side=TOP, pady=25)

        to_install = []
        for item in categories:
            for subItem in item[1]:
                if subItem[1].get():
                    to_install.append(subItem[0])
        functions.install_apps(to_install)

        window.after(5000, lambda :window.destroy())