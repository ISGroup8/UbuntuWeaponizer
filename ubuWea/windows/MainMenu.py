import tkinter as tk
from tkinter import ttk
from tkinter import *
from ttkwidgets import CheckboxTreeview

from ubuWea.windows.InstallWindow import *
from ubuWea.windows.UpdateWindow import *
from ubuWea.windows.UninstallWindow import *
from ubuWea.windows.InfoWindow import *
from ubuWea.windows.ContactUsWindow import *



class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Ubuntu Weaponizer")
        self.root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../assets/logo.png'))

        Label(text="Welcome to the Weaponizer :)", font= ('DejaVu Sans Mono',15))\
            .pack(side = TOP, pady = 10)

        self.root.minsize(500,350)
        self.root.maxsize(500,350)
        self.frame = tk.Frame(root)

        # First row
        botInstall = tk.Button(self.root, text= "Install", width= 15, height= 4,
                               font=('DejaVu Sans Mono',15), command=  installWindow())
        botUpt = tk.Button(self.root, text="Update", width= 15, height= 4,
                           font=('DejaVu Sans Mono',15), command= updateWindow)
        botInstall.place(x= 50, y= 50)
        botUpt.place(x = 250, y = 50)

        # Second row
        botDesInst = tk.Button(self.root, text="Uninstall", width= 15, height= 4,
                               font=('DejaVu Sans Mono',15), command= uninstallWindow)
        botInfo = tk.Button(self.root, text="Show apps", width= 15, height= 4,
                            font=('DejaVu Sans Mono',15), command= infoWindow)
        botDesInst.place(x= 50, y= 200)
        botInfo.place(x= 250, y= 200)

        # Apart
        botContact = tk.Button(self.root, text="Contac us", width=10,
                               font=('DejaVu Sans Mono', 10), command= contactWindow)
        botContact.place (x = 390, y = 315)



# start the program
root = tk.Tk()
program = App(root)
root.mainloop()
