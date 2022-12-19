from InstallWindow import *
from UpdateWindow import *
from UninstallWindow import *
from InfoWindow import *
from ContactUsWindow import *
from ListOfApps import *
from colorFormat import *

class App:

    def __init__(self, root):

        categories = init_categories()
        formatos = init_Formats()
        info = init_info()

        self.root = root
        self.root.title("Ubuntu Weaponizer")
        icon = PhotoImage(file='../../assets/logo.png')
        self.root.iconphoto(True, icon)
        Label(text="Welcome to the Weaponizer", bg=formatos['fondo1'], font= formatos['specialF'], fg=formatos['colorFontS']) \
            .pack(side=TOP, pady=10)

        self.root.minsize(500,360)
        self.root.maxsize(500,360)
        self.frame = tk.Frame(root)
        self.root.configure(bg=formatos['fondo1'], # backgound
                            cursor=formatos['cursor'], # cursor
                            relief="flat", # relieve root
                            bd=5) #borde en px

        # First row
        botInstall = tk.Button(self.root, text= "Install", width= 12, height= 3, bg=formatos['si'], fg=formatos['colorFontN2'],
                               font=formatos['specialF'], command=lambda: InstallWindow(root,categories, formatos) )
        botUpt = tk.Button(self.root, text="Update", width= 12, height= 3, bg=formatos['si'], fg=formatos['colorFontN2'],
                           font=formatos['specialF'], command=lambda : UpdateWindow(root, categories, formatos))
        botInstall.place(x= 50, y= 60)
        botUpt.place(x = 250, y = 60)

        # Second row
        botDesInst = tk.Button(self.root, text="Uninstall", width= 12, height= 3, bg=formatos['si'], fg=formatos['colorFontN2'],
                               font=formatos['specialF'], command=lambda : UninstallWindow(root, categories, formatos))
        botInfo = tk.Button(self.root, text="Information", width= 12, height= 3, bg=formatos['si'], fg=formatos['colorFontN2'],
                            font=formatos['specialF'], command=lambda: InfoWindow(root, info, formatos))
        botDesInst.place(x= 50, y= 190)
        botInfo.place(x= 250, y= 190)

        # Apart
        botContact = tk.Button(self.root, text="Contact us", width=10, bg=formatos['si'], fg=formatos['colorFontN2'],
                               font=formatos['normalF'], command=lambda : ContactWindow(root,formatos))
        botContact.place (x = 390, y = 315)

        botExit = tk.Button(self.root, text="Exit", width=10, bg=formatos['no'], fg= formatos['colorFontN'],
                               font=formatos["normalF"], command=exit)
        botExit.place(x=280, y=315)



# start the program
root = tk.Tk()
program = App(root)
root.mainloop()
