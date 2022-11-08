import os

def install_apps (apt_list):
    install = 'sudo apt install -y'
    for item in apt_list:
        install += ' ' + item
    os.system(install)


def install_git_app (number):


def system_update ():
    os.system('sudo apt update -y')


def system_upgrade ():
    os.system('sudo apt upgrade -y')


