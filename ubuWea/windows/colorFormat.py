from tkinter import *

def init_Formats():
    global formatos
    formatos = { }
    formatos['normalF'] = 'DejaVu Sans Mono', 11
    formatos['specialF'] = 'DejaVu Sans Mono', 18, "bold"
    formatos['colorFontN2'] = "black"
    formatos['colorFontN'] = 'white'
    formatos['colorFontS'] = '#DAF7A6'
    formatos['fondo1'] = '#581845'
    formatos['fondo2'] = ''
    formatos['cursor'] = 'X_cursor'
    formatos['si'] = '#DAF7A6'
    formatos ['no'] = '#E54242'

    return formatos