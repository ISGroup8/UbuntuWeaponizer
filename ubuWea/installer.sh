#! /bin/bash

user=$1
installpath=/home/$user/tools


function setoolkit() 
{
    sudo -u {USER} 'git clone https://github.com/trustedsec/social-engineer-toolkit/ {HOME}/tools/setoolkit/'
    sudo -u {USER} 'git clone https://github.com/UndeadSec/SocialFish.git'
    apt-get install python3 python3-pip python3-dev -y
    cd SocialFish
    sudo -u {USER} 'python3 -m pip install -r requirements.txt'
}

function hidden-eye { 
    git clone https://github.com/Morsmalleo/HiddenEye.git
    mv HiddenEye {HOME}/tools
}

function shellpish{ 
    git clone https://github.com/suljot/shellphish.git
    mv shellphish {HOME}/tools
}
    
function pyphisher { apt install python3 php openssh-client -y
    git clone https://github.com/KasRoudra/PyPhisher {HOME}/tools
    cd {HOME}/tools/PyPhisher; pip3 install -r files/requirements.txt}

function burpsuite{  apt-get install openjdk-8-jre; \
    sudo -u {USER} "wget 'https://portswigger.net/burp/releases/startdownload?product=community&amp;version=2022.9.6&amp;type=linux'"; \
    sudo -u {USER} 'chmod + x burpsuite*'
    sudo -u user './burpsuite*'
    }
    
 function rustscan{  
    sudo -u {USER} 'wget https://github.com/RustScan/RustScan/archive/refs/tags/2.1.1.tar.gz'
    sudo -u {USER} 'tar -xf RustScan*'
    cd RustScan*
    sudo -u {USER} 'dpkg -i Rust'
    cd ..
    rm -rf RustScan
}
    
function ghidra 
{
    apt install flatpak
    sudo apt install gnome-software 
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub org.ghidra_sre.Ghidra
}
function cutter 
{ 
    cd {HOME}/tools
    wget https://github.com/rizinorg/cutter/releases/download/v2.1.2/Cutter-v2.1.2-Linux-x86_64.AppImage
    chmod +x Cutter*

}
function pwntools 
{ 
    apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade pwntools
 }

function Radare2 
{ 
    git clone https://github.com/radareorg/radare
    sudo -u {USER} radare2/sys/install.sh
 }

function Volatility2 {
    apt install -y python2 python2.7-dev libpython2-dev
    sudo -u {USER} 'curl https://bootstrap.pypa.io/pip/2.7/get-pip.py'
    python2 get-pip.py
    python2 -m pip install -U setuptools wheel
    sudo -u {USER} 'python2 -m pip install -U distorm3 yara pycrypto pillow openpyxl ujson pytz ipython capstone'
    ln -s /usr/local/lib/python2.7/dist-packages/usr/lib/libyara.so /usr/lib/libyara.so
    sudo -u {USER} 'python2 -m pip install -U git+https://github.com/volatilityfoundation/volatility.git'
}
