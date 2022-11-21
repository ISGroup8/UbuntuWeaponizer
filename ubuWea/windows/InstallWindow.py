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
    frame.configure(bg="LightSkyBlue2" ,
                    cursor="target", # cursor
                    relief="flat", # relieve root
                    bd=5)

    Label(frame,text=" Install the things you want :)",bg="LightSkyBlue2", font=('DejaVu Sans Mono', 15))\
        .pack(side=TOP, pady=10)

    #List of apps
    app_font = Text ()
    categories_font = Text ()




    botExit = tk.Button(frame, text="Exit", width=10, bg="navajo white",
                           font=('DejaVu Sans Mono', 10), command=frame.destroy)
    botExit.pack(side=BOTTOM, pady = 10)





