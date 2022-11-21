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

    #Añadir un scroll
    #scroll = Scrollbar (frame)
    #scroll.pack(side=RIGHT, fill = Y)
    #scroll.grid(in_=frame, side=RIGHT)

    Label(frame,text=" Install the things you want :)",bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15))\
        .pack(side=TOP, pady=10)

    #List of apps
    normalF = Text (font=('DejaVu Sans Mono', 10))
    specialF = Text (font=('DejaVu Sans Mono', 15, "bold"))
    Label(frame, text="--Categories--", font=specialF, bg="navajo white").pack( pady = 10)

    phising = ['SET', 'SocialPhish', 'Hidden-Eye', 'ShellPhish', 'PyPhisher']
    Web = ['Nmap', 'BurpSuite', 'FFUF', 'RustScan', 'WPSCAN']
    Forense = ['Autopsy', 'Metagoofil', 'Exiftool', 'Wireshark']
    osint = ['Null']
    pwn = ['Null']
    categories = [('Phising',phising), ('Web',Web),('Forense',Forense),('OSINT',osint),('PWN',pwn)]

    l = 40
    k = 300
    m = 60
    n = 60
    o = True
    frame.checkbox_value = tk.BooleanVar(frame)
    for item in categories:
        if (o):
            m += 40
            Label(frame, text=item[0], font=specialF, bg="navajo white").place(x=l,y=m)
            m += 20
        else:
            n += 40
            Label(frame, text=item[0], font=specialF, bg="navajo white").place(x=k, y=n)
            n += 20
        for subItem in item[1]:

            frame.checkbox = ttk.Checkbutton(frame, text=subItem, variable= frame.checkbox_value)
            if (o):
                m += 20
                frame.checkbox.place(x=l,y=m)
            else:
                n += 20
                frame.checkbox.place(x=k, y=n)
        o = not o


    botExit = tk.Button(frame, text="Exit", width=10, bg="navajo white",
                           font=('DejaVu Sans Mono', 10), command=frame.destroy)
    botExit.pack(side=BOTTOM, pady = 10)





