import os

USER = "paco"
HOME = f"/home/{USER}"
apt_apps = {"nmap", "ffuf", "wpscan", "sqlmap", "gdb", "wireshark", "libimage-exiftool-perl"}
git_apps = {"setoolkit", "hidden-eye", "shellpish", "pyphisher", "burpsuite", "rustscan", 
"ghidra", "cutter", "pwntools", "Radare2", "Volatility2", "the_spy_job", "Maltego", "TheHarvester", 
"Metagoofil", "Autopsy"}

def install_apps (l):
    install_apt = 'apt install -y'
    for item in l:
        if item in apt_apps:
            install_apt += ' ' + item
        else:
            usuario =  os.getenv('USER')
            os.system(f"./install.sh {usuario} {item}")

    if install_apt != 'apt install -y':
        os.system(install_apt)
        os.system(f"chown -R {USER}:{USER} {HOME}/tools")


def system_update ():
    os.system('apt update -y')


def system_upgrade ():
    os.system('sudo apt upgrade -y')


