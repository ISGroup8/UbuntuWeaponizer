import os


def system_update ():
    os.system('sudo apt update -y')


def system_upgrade ():
    os.system('sudo apt upgrade -y')