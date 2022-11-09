import os


apt_apps = {"nmap", "ffuf", "wpscan", "sqlmap", "gdb", "wireshark", "libimage-exiftool-perl"}
git_apps = {"setoolkit", "socialpish", "hidden-eye", "shellpish", "pyphisher", "burpsuite",
 "rustscan", "ghidra", "cutter", "pwntools", "Radare2", "Volatility 2", "Volatility 3", "Autopsy",
  "Metagoofil", "The Harvester", "Sherlock", "Maltego", "The Spy Job"} #añadir el comando para instalar.

def install_apps (l):
    install_apt = 'sudo apt install -y'
    for item in l:
        if item in apt_apps:
            install_apt += ' ' + item
        else:
            os.system(git_apps[item])

    if install_apt != 'sudo apt install -y':
        os.system(install_apt)


def system_update ():
    os.system('sudo apt update -y')


def system_upgrade ():
    os.system('sudo apt upgrade -y')


