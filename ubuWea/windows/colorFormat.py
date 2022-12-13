from tkinter import *

def init_Formats():
    global formatos
    formatos = { }
    formatos['normalF'] = Text(font=('DejaVu Sans Mono', 10))
    formatos['specialF'] = Text(font=('DejaVu Sans Mono', 15, "bold"))

    return formatos