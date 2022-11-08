import os

if __name__ == "__main__":
    t = []
    to_install="sudo apt install -y"

    message = "[+] Instalando"

    for item in t:
        message += " " + item
        to_install += " " + item

    print(message)

    os.system(to_install)

    print("[+] Todo instalado")