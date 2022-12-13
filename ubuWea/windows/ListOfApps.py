from tkinter import BooleanVar

def init_categories():
    global valueArray, categories, phising, Web, Forence, osint, pwn

    valueArray, phising, Web, Forense, osint, pwn = [], [], [], [], [], []
    for i in range(26):
        valueArray.append(BooleanVar())

    ## valores libres -> 11, 1, 24
    phising = [('SEToolkit', valueArray[0]), ('Hidden Eye', valueArray[2]),
           ('ShellPhish', valueArray[3]), ('PyPhisher', valueArray[4])]
    Web = [('Nmap', valueArray[5]), ('BurpSuite', valueArray[6]), ('Ffuf', valueArray[7]),
       ('WPScan', valueArray[14]), ('SQLMap', valueArray[15]), ('RustScan', valueArray[17])]
    Forense = [('Metagoofil', valueArray[8]), ('Libimage ExifTool Perl', valueArray[9]),
           ('Wireshark', valueArray[10]), ('Volatility2', valueArray[20]), ('Autopsy', valueArray[25])]
    osint = [('The Spy Job', valueArray[21]), ('Maltego', valueArray[22]),
         ('TheHarvester', valueArray[23]), ('Metagoofil', valueArray[10])]
    pwn = [('Cutter', valueArray[12]), ('PWNTools', valueArray[13]), ('GDB', valueArray[16]),
       ('Ghidra', valueArray[18]), ('Radare2', valueArray[19])]

    categories = [('Phising', phising), ('Web', Web), ('Forense', Forense), ('OSINT', osint), ('PWN', pwn)]

    return categories
