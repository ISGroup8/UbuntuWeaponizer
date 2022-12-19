#!/bin/bash

user=$1
installpath=/home/$user/tools
mkdir -p $installpath
cd $installpath

function setoolkit() {
    git clone https://github.com/trustedsec/social-engineer-toolkit.git
    chown -R $user:$user social-engineer-toolkit
    mv setoolkit $installpath
    apt-get install python3 python3-pip python3-dev -y
    cd $installpath/setoolkit
    sudo -u $user 'python3 -m pip install -r requirements.txt'
}

function hidden-eye { 
    git clone https://github.com/Morsmalleo/HiddenEye.git
    chown -R $user:$user HiddenEye
    mv HiddenEye $installpath
}

function shellpish { 
    git clone https://github.com/suljot/shellphish.git
    mv shellphish $installpath
    chown -R $user:$user $installpath/shellphish
}
    
function PyPhisher { 
    apt install python3 php openssh-client -y
    git clone https://github.com/KasRoudra/PyPhisher
    chown +R $user:$user PyPhisher
    mv PyPhisher $installpath
    cd $installpath/PyPhisher
    pip3 install -r files/requirements.txt
}

function Burpsuite {  
    apt-get install openjdk-8-jre
    wget 'https://portswigger.net/burp/releases/startdownload?product=community&amp;version=2022.9.6&amp;type=linux'
    chmod + x burpsuite*
    chown -R $user:$user burpsuite*
    sudo -u $user './burpsuite*'
    rm -f burpsuite*
}
    
function rustscan {  
    wget https://github.com/RustScan/RustScan/archive/refs/tags/2.1.1.tar.gz
    tar -xf RustScan*
    cd RustScan*
    sudo -u $user 'dpkg -i RustScan*'
    cd ..
    rm -rf RustScan
}
    
function ghidra {
    apt install flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub org.ghidra_sre.Ghidra
}

function cutter { 
    cd $installpath
    wget https://github.com/rizinorg/cutter/releases/download/v2.1.2/Cutter-v2.1.2-Linux-x86_64.AppImage
    chmod +x Cutter-v2.1.2-Linux-x86_64.AppImage
    chown +R $user:$user Cutter-v2.1.2-Linux-x86_64.AppImage
}

function pwntools { 
    apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
    sudo -u $user 'python3 -m pip install --upgrade pip'
    sudo -u $user 'python3 -m pip install --upgrade pwntools'
}

function Radare2 { 
    git clone https://github.com/radareorg/radare.git
    chown -R $user:$user radare
    sudo -u $user radare2/sys/install.sh
}

function Volatility2 {
    apt install -y python2 python2.7-dev libpython2-dev
    sudo -u $user 'curl https://bootstrap.pypa.io/pip/2.7/get-pip.py'
    sudo -u $user 'python2 get-pip.py'
    sudo -u $user 'python2 -m pip install -U setuptools wheel'
    sudo -u $user 'python2 -m pip install -U distorm3 yara pycrypto pillow openpyxl ujson pytz ipython capstone'
    sudo -u $user 'ln -s /usr/local/lib/python2.7/dist-packages/usr/lib/libyara.so /usr/lib/libyara.so'
    sudo -u $user 'python2 -m pip install -U git+https://github.com/volatilityfoundation/volatility.git'
}

function the_spy_job {
    git clone https://github.com/XDeadHackerX/The_spy_job.git
    chown -R $user:$user The_spy_job
}

function Sherlock {
    git clone https://github.com/sherlock-project/sherlock.git
    chown -R $user:$user sherlock
    cd sherlock
    sudo -u $user 'python3 -m pip install -r requirements.txt'
}

function Maltego {
    apt-get install openjdk-11-jdk
    git clone https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.3.1.deb
    dpkg -i Maltego.v4.3.1.deb
}

function TheHarvester {
    git clone https://github.com/laramies/theHarvester.git
    cd theHarvester
    sudo -u $user 'pip3 install -r requirements.txt'
}

function Metagoofil {
    git clone https://github.com/opsdisk/metagoofil.git
    chown -R $user:$user metagoofil
    cd metagoofil
    sudo -u $user 'pip3 install -r requirements.txt'
}


function Autopsy {
    wget https://github.com/sleuthkit/autopsy/releases/download/autopsy-4.19.2/autopsy-4.19.2.zip
    wget https://github.com/sleuthkit/sleuthkit/releases/download/sleuthkit-4.11.1/sleuthkit-java_4.11.1-1_amd64.deb
    chown -R $user:$user autopsy-4.19.2.zip
    chown -R $user:$user sleuthkit-java_4.11.1-1_amd64.deb
}

$2
