
import tkinter as tk
from tkinter import *

import functions

class InstallWindow (tk.Toplevel):

    def __init__(self, root, categories):
        super().__init__(root)
        self.minsize(500,450)
        self.title("Ubuntu Weaponizer")

        self.configure(bg="LightSkyBlue2",
                        cursor="target",  # cursor
                        relief="flat",  # relieve root
                        bd=5)

        Label(self, text="Apps.install()", bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15)) \
            .pack(side=TOP, pady=10)

        Label(self, text="../Categories", font=specialF, bg="navajo white").pack(pady=10)

        # Scrollbar
        wrapper = LabelFrame(self, bg="AntiqueWhite1")
        wrapper.pack(fill="both", expand=YES, padx=10)

        myCanvas = Canvas(wrapper, bg="AntiqueWhite1", width= 500)
        myCanvas.pack(side=LEFT)

        scrollbar = Scrollbar(wrapper, orient=VERTICAL, command=myCanvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        myCanvas.config(yscrollcommand=scrollbar.set)
        myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

        myframe = Frame(myCanvas, bg="AntiqueWhite1", height=1000, width=500, relief=SUNKEN)

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
                Label(myframe, text=item[0], font=specialF, bg="navajo white").place(x=l, y=m)
                #m += 20
            else:
                n += 50
                Label(myframe, text=item[0], font=specialF, bg="navajo white").place(x=k, y=n)
                #n += 20
            for subItem in item[1]:
                self.checkbox = Checkbutton (myframe, text= subItem[0], font=normalF, bg="AntiqueWhite1",
                                             variable= subItem[1], onvalue= True, offvalue= False)
                if (o):
                    m += 30
                    self.checkbox.place(x=l, y=m)
                else:
                    n += 30
                    self.checkbox.place(x=k, y=n)

            o = not o
        myframe.configure(height=max(n,m)+50)
        installButton = tk.Button(self, text=".install()", width=10, bg="navajo white",
                            font=('DejaVu Sans Mono', 10), command=lambda: self.install(categories))
        installButton.pack(side=RIGHT, anchor = S, padx=15, pady= 10)

        goBackButton = tk.Button(self, text=".goBack()", width=10, bg="dark grey",
                            font=('DejaVu Sans Mono', 10), command=lambda: self.destroy())
        goBackButton.pack(side=RIGHT, anchor = S, pady= 10)



    def install(self, categories):
        window = tk.Toplevel(self)
        window.minsize(200,100)
        window.title("")
        window.configure(bg="navajo white",
                        cursor="target",
                        relief="flat",
                        bd=5)
        Label(window,text="-- Apps are being installed please wait, you will be notified when everything's done.", 
        font=('DejaVu Sans Mono', 15, "bold"), bg="LightSkyBlue2").pack(side=TOP, pady=25)
        listOfApps = ""
        to_install = []
        for item in categories:
            for subItem in item[1]:
                if subItem[1].get():
                    to_install.append(subItem[0])
                    listOfApps += str(subItem[0]) + "\n"
        functions.install_apps(to_install)
        listOfApps += "These are the apps that are going to install"
        Label(window, text=listOfApps, font=('DejaVu Sans Mono', 15, "bold"),
              bg="LightSkyBlue2").pack(side=TOP, pady=25)

        window.after(5000, lambda :window.destroy())