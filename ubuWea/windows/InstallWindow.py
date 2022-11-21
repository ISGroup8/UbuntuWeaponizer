import tkinter
from tkinter import messagebox, Label, ttk
import tkinter as tk
from tkinter import *
from tkinter.ttk import Button
from ttkwidgets import CheckboxTreeview


def installWindow(root):
    frame = tkinter.Toplevel(root)
    frame.lift(root)
    frame.minsize(500, 360)
    frame.title("Ubuntu Weaponizer")
    frame.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../assets/logo.png'))
    frame.configure(bg="LightSkyBlue2" ,
                    cursor="target", # cursor
                    relief="flat", # relieve root
                    bd=5)

    Label(frame,text=" Install the things you want :)",bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15))\
        .pack(side=TOP, pady=10)

    #List of apps
    normalF = Text (font=('DejaVu Sans Mono', 10))
    specialF = Text (font=('DejaVu Sans Mono', 15, "bold"))
    Label(frame, text="--Categories--", font=specialF, bg="navajo white").pack(side=LEFT, pady = 20)
    listbox = Listbox(frame)
    listbox.place(x= 20 , y = 70)

    phising = ['SET', 'SocialPhish', 'Hidden-Eye', 'ShellPhish', 'PyPhisher']
    Web = ['Nmap', 'BurpSuite', 'FFUF', 'RustScan', 'WPSCAN']
    Forense = ['Autopsy', 'Metagoofil', 'Exiftool', 'Wireshark']
    osint = []
    pwn = []
    categories = [('Phising',phising), ('Web',Web),('Forense',Forense),('OSINT',osint),('PWN',pwn)]

    for item in categories:
        Label(frame, text=item[0], font=specialF, bg="navajo white").pack(side=LEFT, pady=20)
        listbox.insert(END, item)
        for subItem in item[1]:
             Checkbutton(frame, text=subItem)

    def onselect(evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        x = 0
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item %d: "%s"' % (index, value))

        for y in enable:
            for item in list_for_listbox:
                globals()["checkbox{}{}".format(item, y)].place_forget()
            globals()["checkbox{}{}".format(value, y)].place(x=300, y=0 + x)
            x += 50

    listbox.bind('<<ListboxSelect>>', onselect)

    print(enable)



    botExit = tk.Button(frame, text="Exit", width=10, bg="navajo white",
                           font=('DejaVu Sans Mono', 10), command=frame.destroy)
    botExit.pack(side=BOTTOM, pady = 10)





