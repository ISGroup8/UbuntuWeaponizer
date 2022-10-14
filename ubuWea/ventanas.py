import tkinter as tk
import pandas as pd
import base64
import os
from tkinter.filedialog import askdirectory
from tkinter import ttk
import sys

root = tk.Tk()
root.title("Ubuntu Weaponizer")
n = ttk.Notebook(root, width=600, height=400)
f1 = ttk.Frame(n, height=100, width=100)
f2 = ttk.Frame(n, height=100, width=100)
f3 = ttk.Frame(n, height=100, width=100)
n.grid(column=0, row=0)
n.add(f1, text='Instalar')
n.add(f2, text='Actualizar')
n.add(f3, text="Desinstalar")
n.pack()

tree = ttk.Treeview(f1)
tree["columns"] = ("one", "two")
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="Desarrollador")
tree.heading("two", text="Tamaño")
id2 = tree.insert("", 1, "dir2", text="Footprinting")
tree.insert(id2, "end", "dir3", text="App 1",
            values=("Desarrollador 1", "200Mb"))
tree.insert(id2, "end", "dir4", text="App 2", values=("Desarrollador 2", "350Mb"))
id3 = tree.insert("", 2, "dir5", text="Phishing")
tree.insert(id3, "end", "dir6", text="App 1", values=("Desarrollador 1", "320Mb"))
tree.insert(id3, "end", "dir7", text="App 2", values=("Desarrollador 2", "430Mb"))
tree.insert(id3, "end", "dir8", text="App 3", values=("Desarrollador 3", "215Mb"))
tree.pack()

tree = ttk.Treeview(f2)
tree["columns"] = ("one", "two")
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="Desarrollador")
tree.heading("two", text="Tamaño")
id2 = tree.insert("", 1, "dir2", text="Footprinting")
tree.insert(id2, "end", "dir3", text="App 1",
            values=("Desarrollador 1", "200Mb"))
tree.insert(id2, "end", "dir4", text="App 2", values=("Desarrollador 2", "350Mb"))
id3 = tree.insert("", 2, "dir5", text="Phishing")
tree.insert(id3, "end", "dir6", text="App 1", values=("Desarrollador 1", "320Mb"))
tree.insert(id3, "end", "dir7", text="App 2", values=("Desarrollador 2", "430Mb"))
tree.insert(id3, "end", "dir8", text="App 3", values=("Desarrollador 3", "215Mb"))
tree.pack()
root.mainloop()


