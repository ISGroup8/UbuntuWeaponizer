# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk
import pandas as pd
import base64
import os
from tkinter.filedialog import askdirectory
from tkinter import ttk
import sys



def fun1():
    print("1")

def fun2():
    print("2")

class Aplicacion:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Ubuntu Weaponizer")
        self.canvas1=tk.Canvas(self.root, width=600, height=400, background="lavender")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_line(100, 100, 100,1000, fill="black")

        btn = tk.Button (self.root, text = "Func 1", command=fun1)
        #btn.pack(side=tk.LEFT)
        btn = tk.Button (self.root, text = "Func 2", command=fun2)
        #btn.pack(side=tk.LEFT)
        self.canvas1=tk.Canvas(self.root, width=600, height=400, background="lavender")
        self.canvas1.create_line(0, 0, 100,50, fill="white")
        self.root.mainloop()


aplicacion1=Aplicacion()

