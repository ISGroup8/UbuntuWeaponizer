from tkinter import *

def init_Formats():
    global formatos
    formatos = {
        'normalF'
    }

    normalF = Text(font=('DejaVu Sans Mono', 10))
    specialF = Text(font=('DejaVu Sans Mono', 15, "bold"))


    return formatos