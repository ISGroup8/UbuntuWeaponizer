import tkinter as tk
from tkinter import ttk
from tkinter import *
from ttkwidgets import CheckboxTreeview

from InstallWindow import *
from UpdateWindow import *
from UninstallWindow import *
from InfoWindow import *
from ContactUsWindow import *
from ListOfApps import *

class App:

    def __init__(self, root):
        categories = init_categories()
        self.root = root
        self.root.title("Ubuntu Weaponizer")
        icon = PhotoImage(file='../../assets/logo.png')
        self.root.iconphoto(True, icon)
        Label(text="Welcome to the Weaponizer :)", bg="navajo white", font=('DejaVu Sans Mono', 15)) \
            .pack(side=TOP, pady=10)

        self.root.minsize(500,360)
        self.root.maxsize(500,360)
        self.frame = tk.Frame(root)
        self.root.configure(bg="navajo white", # backgound
                            cursor="target", # cursor
                            relief="flat", # relieve root
                            bd=5) #borde en px

        # First row
        botInstall = tk.Button(self.root, text= "Install", width= 15, height= 4,bg="LightSkyBlue2",
                               font=('DejaVu Sans Mono',15), command=lambda: InstallWindow(root,categories) )
        botUpt = tk.Button( text="Update", width= 15, height= 4, bg="LightSkyBlue2",
                           font=('DejaVu Sans Mono',15), command=lambda : UpdateWindow(root, categories))
        botInstall.place(x= 50, y= 60)
        botUpt.place(x = 250, y = 60)

        # Second row
        botDesInst = tk.Button(self.root, text="Uninstall", width= 15, height= 4, bg="LightSkyBlue2",
                               font=('DejaVu Sans Mono',15), command=lambda : UninstallWindow(root, categories))
        botInfo = tk.Button(self.root, text="Show apps", width= 15, height= 4, bg="LightSkyBlue2",
                            font=('DejaVu Sans Mono',15), command=lambda: InfoWindow(root, categories))
        botDesInst.place(x= 50, y= 190)
        botInfo.place(x= 250, y= 190)

        # Apart
        botContact = tk.Button(self.root, text="Contac us", width=10, bg="LightSkyBlue2",
                               font=('DejaVu Sans Mono', 10), command=lambda : ContactWindow(root))
        botContact.place (x = 390, y = 315)

        #botExit = tk.Button(self.root, text="Exit", width=10,
        #                       font=('DejaVu Sans Mono', 10), command=exit)
        #botExit.place(x=390, y=200)



# start the program
root = tk.Tk()
program = App(root)
root.mainloop()
