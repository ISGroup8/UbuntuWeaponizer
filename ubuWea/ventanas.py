import tkinter as tk
import pandas as pd
import base64
import os
from tkinter.filedialog import askdirectory
from tkinter import ttk
import sys
from tkinter import *
from ttkwidgets import CheckboxTreeview


def install():
    lbl.configure(text="Button was clicked !!")


root = tk.Tk()
root.title("Ubuntu Weaponizer")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../assets/logo.png'))
lbl = Label(text="Welcome to the Weaponizer :)")
lbl.pack()
n = ttk.Notebook(root, width=600, height=400)
f1 = ttk.Frame(n, height=100, width=100)
f2 = ttk.Frame(n, height=100, width=100)
f3 = ttk.Frame(n, height=100, width=100)
n.add(f1, text='Instalar')
n.add(f2, text='Actualizar')
n.add(f3, text="Desinstalar")
n.pack()


lab = Label(f1, text="Choose what you want to install:")
lab.pack()
tree = CheckboxTreeview(f1)  # Crear una instancia de lista de estructura de árbol
tree["columns"] = ("one", "two")  # Establecer nombres de objetos de dos columnas
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="Desarrollador")  # Establecer título
tree.heading("two", text="Tamaño")
id2 = tree.insert("", 1, "dir2", text="Footprinting")  # Inserte la segunda fila de la categoría superior id2
tree.insert(id2, "end", "dir3", text="App 1",
            values=("Desarrollador 1", "200Mb"))  # Inserte la tercera fila de clasificación secundaria
tree.insert(id2, "end", "dir4", text="App 2", values=("Desarrollador 2", "350Mb"))
id3 = tree.insert("", 2, "dir5", text="Phishing")  # Inserte el id3 de categoría superior en la fila 5
tree.insert(id3, "end", "dir6", text="App 1", values=("Desarrollador 1", "320Mb"))
tree.insert(id3, "end", "dir7", text="App 2", values=("Desarrollador 2", "430Mb"))
tree.insert(id3, "end", "dir8", text="App 3", values=("Desarrollador 3", "215Mb"))
tree.pack()  # Especifique la orientación
btn = Button (f1,text="Install", command= install)
btn.pack()

lab1 = Label(f2, text="Choose what you want to update:")
lab1.pack()
tree = CheckboxTreeview(f2)  # Crear una instancia de lista de estructura de árbol
tree["columns"] = ("one", "two")  # Establecer nombres de objetos de dos columnas
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="Desarrollador")  # Establecer título
tree.heading("two", text="Tamaño")
id2 = tree.insert("", 1, "dir2", text="Footprinting")  # Inserte la segunda fila de la categoría superior id2
tree.insert(id2, "end", "dir3", text="App 1",
            values=("Desarrollador 1", "200Mb"))  # Inserte la tercera fila de clasificación secundaria
tree.insert(id2, "end", "dir4", text="App 2", values=("Desarrollador 2", "350Mb"))
id3 = tree.insert("", 2, "dir5", text="Phishing")  # Inserte el id3 de categoría superior en la fila 5
tree.insert(id3, "end", "dir6", text="App 1", values=("Desarrollador 1", "320Mb"))
tree.insert(id3, "end", "dir7", text="App 2", values=("Desarrollador 2", "430Mb"))
tree.insert(id3, "end", "dir8", text="App 3", values=("Desarrollador 3", "215Mb"))
tree.pack()  # Especifique la orientación
root.mainloop()

