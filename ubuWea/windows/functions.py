import os

USER = "imarcex"
HOME = f"/home/{USER}"
apt_apps = {"nmap", "ffuf", "wpscan", "sqlmap", "gdb", "wireshark", "libimage-exiftool-perl"}
git_apps = {"setoolkit", "hidden-eye", "shellpish", "PyPhisher", "Burpsuite", "rustscan", 
"ghidra", "cutter", "pwntools", "Radare2", "Volatility2", "the_spy_job", "Maltego", "TheHarvester", 
"Metagoofil", "Autopsy"}

def install_apps (l):

    install_apt = 'apt install -y'
    for item in l:
        if item in apt_apps:
            install_apt += ' ' + item
        else:
            os.system(f"./install.sh {USER} {item}")
            print(os.system(f"figlet {item}  Instalado"))

    os.system(f"chown -R {USER}:{USER} {HOME}/tools")

    if install_apt != 'apt install -y':
        os.system(install_apt)

def uninstall_apps (l):

    uninstall_apt = 'apt remove -y'
    for item in l:
        if item in apt_apps:
            uninstall_apt += ' ' + item
        else:
            os.system(f"./uninstall.sh {USER} {item}")
            print(os.system(f"figlet {item}  Desinstalado"))

    if uninstall_apt != 'apt remove -y':
        os.system(uninstall_apt)


def system_update ():
    os.system('apt update -y')


def system_upgrade ():
    os.system('sudo apt upgrade -y')


