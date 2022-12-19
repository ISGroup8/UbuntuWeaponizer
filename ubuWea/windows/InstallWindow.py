
import tkinter as tk
from tkinter import *

import functions

class InstallWindow (tk.Toplevel):

    def __init__(self, root, categories, formatos):
        super().__init__(root)
        self.minsize(500,450)
        self.title("Ubuntu Weaponizer/Install")

        self.configure(bg=formatos['fondo1'],
                        cursor=formatos['cursor'],  # cursor
                        relief="flat",  # relieve root
                        bd=5)

        Label(self, text="Choose what you want to install...", bg= formatos['fondo1'],font=formatos['specialF'], fg=formatos['colorFontS']) \
            .pack(side=TOP, pady=10)

        Label(self, text="Applications:", font=formatos['specialF'], bg=formatos['fondo1'], fg=formatos['colorFontS'])\
            .pack(pady=10)

        # Scrollbar
        wrapper = LabelFrame(self, bg=formatos['fondo1'])
        wrapper.pack(fill="both", expand=YES, padx=10)

        myCanvas = Canvas(wrapper, bg=formatos['fondo1'], width= 500, height=300, relief="flat")
        myCanvas.pack(side=LEFT)

        scrollbar = Scrollbar(wrapper, orient=VERTICAL, command=myCanvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        myCanvas.config(yscrollcommand=scrollbar.set)
        myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

        myframe = Frame(myCanvas, bg=formatos['fondo1'], height=1000, width=1000, relief=SUNKEN)

        myCanvas.create_window((0,0), window=myframe, anchor=NW)


        # Variables de posición de las apps
        l = 30
        k = 310
        m = -30
        n = -30
        o = True

        # Poner las apps y los checkbox
        for item in categories:
            if (o):
                m += 50
                Label(myframe, text=item[0], font=formatos['specialF'], bg=formatos['fondo1'], fg=formatos['colorFontS']).place(x=l, y=m)
                #m += 20
            else:
                n += 50
                Label(myframe, text=item[0], font=formatos['specialF'], bg=formatos['fondo1'], fg=formatos['colorFontS']).place(x=k, y=n)
                #n += 20
            for subItem in item[1]:
                self.checkbox = Checkbutton (myframe, text= subItem[0], font=formatos['normalF'], bg=formatos['fondo1'], fg=formatos['colorFontN'],
                                             variable= subItem[1], onvalue= True, offvalue= False, selectcolor=formatos['fondo1'])
                if (o):
                    m += 30
                    self.checkbox.place(x=l, y=m)
                else:
                    n += 30
                    self.checkbox.place(x=k, y=n)

            o = not o
        myframe.configure(height=max(n,m)+50)
        installButton = tk.Button(self, text="Install", width=10, bg=formatos['si'], fg=formatos['colorFontN2'],
                            font=formatos['normalF'], command=lambda: self.install(categories, formatos))
        installButton.pack(side=RIGHT, anchor = S, padx=15, pady= 10)

        goBackButton = tk.Button(self, text="Go back", width=10, bg=formatos['no'], fg= formatos['colorFontN'],
                            font=formatos['normalF'], command=lambda: self.destroy())
        goBackButton.pack(side=RIGHT, anchor = S, pady= 10)



    def install(self, categories, formatos):
        window = tk.Toplevel(self)
        window.minsize(200,100)
        window.title("Installing...")
        window.configure(bg=formatos['fondo1'],
                        cursor=formatos['cursor'],
                        relief="flat",
                        bd=5)
        Label(window,text="--> The applicactions are being installed, please wait...\n\nThese are the apps that are going to be installed:", font=formatos['specialF'],
              bg=formatos['fondo1'], fg=formatos['colorFontS']).pack(side=TOP, pady=25)
        listOfApps = ""
        to_install = []
        for item in categories:
            for subItem in item[1]:
                if subItem[1].get():
                    to_install.append(subItem[0])
                    listOfApps += str(subItem[0]) + "\n"
        functions.install_apps(to_install)
        Label(window, text=listOfApps, font=formatos['specialF'],
              bg=formatos['fondo1'], fg= formatos['colorFontN']).pack(side=TOP, pady=25)

        window.after(5000, lambda :window.destroy())