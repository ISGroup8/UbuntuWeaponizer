import tkinter as tk
from tkinter import ttk
from tkinter import *
from ttkwidgets import CheckboxTreeview

from InstallWindow import *
from UpdateWindow import *
from UninstallWindow import *
from InfoWindow import *
from ContactUsWindow import *

class App:

    def __init__(self, root):
        global valueArray, categories, phising, Web, Forence, osint, pwn

        valueArray, phising, Web, Forense,  osint, pwn = [], [], [], [], [], []
        for i in range(26):
            valueArray.append(BooleanVar())
        


        phising = [('setoolkit', valueArray[0]), ('shellpish', valueArray[1]), ('hidden-eye', valueArray[2]), ('ShellPhish', valueArray[3]),
                   ('PyPhisher', valueArray[4])]
        Web = [('nmap', valueArray[5]), ('Burpsuite', valueArray[6]), ('fuff', valueArray[7]), ('wpscan', valueArray[14]), ('sqlmap', valueArray[15]), ('rustscan', valueArray[17])]
        Forense = [('Metagoofil', valueArray[8]), ('libimage-exiftool-perl', valueArray[9]), ('wireshark', valueArray[10]), ('Volatility2', valueArray[20]), ('Autopsy', valueArray[25])]
        osint = [('Void', valueArray[11]), ('the_spy_job', valueArray[21]), ('Maltego', valueArray[22]), ('TheHarvester', valueArray[23]), ('Metagoofil', valueArray[24])]
        pwn = [('cutter', valueArray[12]), ('pwntools', valueArray[13]), ('gdb', valueArray[16]), ('ghidra', valueArray[18]), ('Radare2', valueArray[19])]

        categories = [('Phising', phising), ('Web', Web), ('Forense', Forense), ('OSINT', osint), ('PWN', pwn)]

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
                           font=('DejaVu Sans Mono',15), command=lambda : UpdateWindow(root))
        botInstall.place(x= 50, y= 60)
        botUpt.place(x = 250, y = 60)

        # Second row
        botDesInst = tk.Button(self.root, text="Uninstall", width= 15, height= 4, bg="LightSkyBlue2",
                               font=('DejaVu Sans Mono',15), command=lambda : UninstallWindow(root))
        botInfo = tk.Button(self.root, text="Show apps", width= 15, height= 4, bg="LightSkyBlue2",
                            font=('DejaVu Sans Mono',15), command=lambda: InfoWindow(root))
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
