import tkinter as tk

class App:

    def __init__(self, root):
        self.root = root
	self.root.title("Ubuntu Weaponizer")
        self.root.minsize(1000,400)
        self.root.maxsize(1000, 400)
        self.frame = tk.Frame(root)
        botInstall = tk.Button(self.root, text= "Instalaciones", width= 15, height= 5)
        botDesInst = tk.Button(self.root, text= "Desinstalaciones", width= 15, height= 5)
        botInstall.grid(row= 0, column= 0)
        botDesInst.grid(row= 1, column= 0)

# start the program
root = tk.Tk()
program = App(root)
root.mainloop()
