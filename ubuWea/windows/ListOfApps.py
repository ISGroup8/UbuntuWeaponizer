from tkinter import BooleanVar

def init_categories():

    valueArray, phising, Web, Forense, osint, pwn = [], [], [], [], [], []
    for i in range(26):
        valueArray.append(BooleanVar())

    ## valores libres -> 11, 19, 24
    phising = [('SEToolkit', valueArray[0]),
               ('hidden-eye', valueArray[2]),
               ('shellpish', valueArray[3]),
               ('PyPhisher', valueArray[4])]

    Web = [('nmap', valueArray[5]),
           ('BurpSuite', valueArray[6]),
           ('Ffuf', valueArray[7]),
           ('WPScan', valueArray[14]),
           ('SQLMap', valueArray[15]),
           ('RustScan', valueArray[17])]

    Forense = [('Metagoofil', valueArray[10]),
               ('Libimage ExifTool Perl', valueArray[9]),
               ('Wireshark', valueArray[8]),
               ('Volatility2', valueArray[20]),
               ('Autopsy', valueArray[25])]

    osint = [('The Spy Job', valueArray[21]),
             ('Maltego', valueArray[22]),
             ('TheHarvester', valueArray[23]),
             ('Metagoofil', valueArray[10])]

    pwn = [('Cutter', valueArray[12]),
           ('PWNTools', valueArray[13]),
           ('Pwndbg', valueArray[16]),
           ('Ghidra', valueArray[18]),
           ('Radare2', valueArray[1])]

    categories = [('Phising', phising), ('Web', Web), ('Forense', Forense), ('OSINT', osint), ('PWN', pwn)]

    return categories


def init_info():

    valueArray, phising, Web, Forense, osint, pwn = [], [], [], [], [], []
    for i in range(26):
        valueArray.append(BooleanVar())

    Pwndbg = ["Pwndbg",
              "----",
              "Open-source",
              "pwndbg (/poʊndbæg/) is a GDB plug-in that makes debugging with GDB suck\n"
              "less, with a focus on features needed by low-level software developers,\n"
              "hardware hackers, reverse-engineers and exploit developers. It has a\n"
              "boatload of features, see FEATURES.md.",
              "GitHub - pwndbg/pwndbg: Exploit Development and Reverse Engineering with\n"
              "GDB Made Easy"]
    Burp = ["Burp Suite",
            "Community Edition",
            "PortSwigger",
            "Burp Suite is a leading Web Penetration Testing software written in Java.\n"
            "It has evolved into an industry - standard toolkit for information security\n"
            "experts worldwide.Burp Suite aids in the detection of online application\n"
            "vulnerabilities and the verification of attack vectors.",
            "Download Burp Suite Community Edition - PortSwigger"]
    ## 0 name, 1 version, 2 author, 3 description, 4 source


    ## valores libres -> 11, 19, 24
    phising = [('SEToolkit', valueArray[0], False),
               ('Hidden Eye', valueArray[2], False),
               ('ShellPhish', valueArray[3], False),
               ('PyPhisher', valueArray[4], False)]

    Web = [('Nmap', valueArray[5], False),
           ('BurpSuite', valueArray[6], True, Burp),
           ('Ffuf', valueArray[7], False),
           ('WPScan', valueArray[14], False),
           ('SQLMap', valueArray[15], False),
           ('RustScan', valueArray[17], False)]

    Forense = [('Metagoofil', valueArray[10], False),
               ('Libimage ExifTool Perl', valueArray[9], False),
               ('Wireshark', valueArray[8], False),
               ('Volatility2', valueArray[20], False),
               ('Autopsy', valueArray[25], False)]

    osint = [('The Spy Job', valueArray[21], False),
             ('Maltego', valueArray[22], False),
             ('TheHarvester', valueArray[23], False),
             ('Metagoofil', valueArray[10], False)]

    pwn = [('Cutter', valueArray[12], False),
           ('PWNTools', valueArray[13], False),
           ('Pwndbg', valueArray[16],True,Pwndbg),
           ('Ghidra', valueArray[18], False),
           ('Radare2', valueArray[1], False)]

    categories = [('Phising', phising), ('Web', Web), ('Forense', Forense), ('OSINT', osint), ('PWN', pwn)]

    return categories


