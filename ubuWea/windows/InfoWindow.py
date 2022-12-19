import copy
from tkinter import messagebox

import tkinter
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *



class InfoWindow(tk.Toplevel):
    def __init__(self, root, categories, formatos):
        super().__init__(root)
        self.minsize(500, 550)
        self.title("Ubuntu Weaponizer/Information")
        self.configure(bg=formatos['fondo1'],
                        cursor=formatos['cursor'],  # cursor
                        relief="flat",  # relieve root
                        bd=5)

        Label(self, text="View the information about these applications", bg=formatos['fondo1'], font=formatos['specialF'], fg= formatos['colorFontS']) \
            .pack(side=TOP, pady=10)

        Label(self, text="Applications:", font=formatos['specialF'], bg=formatos['fondo1'], fg= formatos['colorFontS']).pack(pady=10)

        # Scrollbar
        wrapper = LabelFrame(self, bg=formatos['fondo1'])
        wrapper.pack(fill="both", expand=YES, padx=10)

        myCanvas = Canvas(wrapper, bg=formatos['fondo1'], width=500, height=300, relief="flat")
        myCanvas.pack(side=LEFT)

        scrollbar = Scrollbar(wrapper, orient=VERTICAL, command=myCanvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        myCanvas.config(yscrollcommand=scrollbar.set)
        myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

        myframe = Frame(myCanvas, bg=formatos['fondo1'], height=1000, width=1000, relief=SUNKEN)

        myCanvas.create_window((0, 0), window=myframe, anchor=NW)

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
                Label(myframe, text=item[0], font=formatos['specialF'], bg=formatos['fondo1'],
                      fg=formatos['colorFontS']).place(x=l, y=m)
                # m += 20
            else:
                n += 50
                Label(myframe, text=item[0], font=formatos['specialF'], bg=formatos['fondo1'],
                      fg=formatos['colorFontS']).place(x=k, y=n)
                # n += 20
            for subItem in item[1]:

                self.checkbox = Checkbutton(myframe, text=subItem[0], font=formatos['normalF'], bg=formatos['fondo1'], fg=formatos['colorFontN'],
                                            variable=subItem[1], onvalue=True, offvalue=False, selectcolor=formatos['fondo1'],
                                            command= lambda: self.showInfo(categories,formatos))
                if (o):
                    m += 30
                    self.checkbox.place(x=l, y=m)
                else:
                    n += 30
                    self.checkbox.place(x=k, y=n)

            o = not o
        myframe.configure(height=max(n, m) + 50)

        goBackButton = tk.Button(self, text="Go back", width=10, bg=formatos['no'], fg=formatos['colorFontN'],
                                 font=formatos['normalF'], command=lambda: self.destroy())
        goBackButton.pack(side=RIGHT, anchor=S, pady=10)



    def showInfo(self, categories, formatos):
        window = tk.Toplevel(self)
        window.minsize(700,400)
        window.title("Displaying information...")
        window.configure(bg=formatos['fondo1'],
                        cursor=formatos['cursor'],
                        relief="flat",
                        bd=5)
        aux = None
        for item in categories:
            for subItem in item[1]:
                if subItem[1].get():
                    subItem[1].set(False)
                    if subItem[2]:
                        aux = subItem[3]

        if aux != None:

            # Scrollbar
            wrapper = LabelFrame(window, bg=formatos['fondo1'])
            wrapper.pack(fill="both", expand=YES, padx=10)

            myCanvas = Canvas(wrapper, bg=formatos['fondo1'], width=700, height=400, relief="flat")
            myCanvas.pack(side=LEFT)

            scrollbar = Scrollbar(wrapper, orient=VERTICAL, command=myCanvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            myCanvas.config(yscrollcommand=scrollbar.set)
            myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

            myframe = Frame(myCanvas, bg=formatos['fondo1'], height=700, width=400, relief=SUNKEN)

            myCanvas.create_window((10, 15), window=myframe, anchor=NW, width=700, height=400)

            ## 0 name, 1 version, 2 author, 3 description, 4 source
            Label(myframe, text="Name: " + aux[0], font=formatos['specialF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontS']).pack(side=TOP, pady=25)

            Label(myframe, text="Version: ", font=formatos['specialF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontS']).place(x= 20, y= 60)
            Label(myframe, text=aux[1], font=formatos['normalF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontN']).place(x= 190, y= 67)

            Label(myframe, text="Author: ", font=formatos['specialF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontS']).place(x= 20, y= 100)
            Label(myframe, text=aux[2], font=formatos['normalF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontN']).place(x=190, y=107)

            Label(myframe , text="Description: ", font=formatos['specialF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontS']).place(x= 20, y= 140)
            Label(myframe, text=aux[3], font=formatos['normalF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontN']).place(x=190, y=147)

            Label(myframe, text="Source: ", font=formatos['specialF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontS']).place(x= 20, y= 220)
            Label(myframe, text=aux[4], font=formatos['normalF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontN']).place(x=190, y=227)

        else:
            Label(window, text="There isn't information \nabout this application, \nso sorry...\n :c", font=formatos['specialF'], bg=formatos['fondo1'],
                  fg=formatos['colorFontS']).pack(side=TOP, pady=100)
            window.after(3000, lambda: window.destroy())



        goBackButton = tk.Button(window, text="Go back", width=10, bg=formatos['no'], fg=formatos['colorFontN'],
                                 font=formatos['normalF'], command=lambda: window.destroy())
        goBackButton.pack(side=RIGHT, anchor=S, pady=10)



