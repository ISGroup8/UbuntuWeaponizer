#!/bin/bash

user=$1
installpath=/home/$user/tools
mkdir -p $installpath
cd $installpath

function setoolkit() {
    rm -rf $installpath/social-engineer-toolkit
}

function hidden-eye { 
    rm -rf $installpath/HiddenEye
}

function shellpish { 
    rm -rf $installpath/shellphish
}
    
function PyPhisher { 
    rm -rf $installpath/PyPhisher
}
    
function rustscan {  
    echo "hola"
}
    

function cutter { 
    rm $installpath/Cutter-v2.1.2-Linux-x86_64.AppImage
}


function Radare2 { 
    rm -rf $installpath/radare
}


function the_spy_job {
    rm -rf $installpath/The_spy_job
}

function Sherlock {
    rm -rf $installpath/sherlock
}

function Maltego {
    sudo apt remove Maltego # No usar
}

function TheHarvester {
    rm -rf $installpath/theHarvester
}

function Metagoofil {
    rm -rf $installpath/metagoofil
    
}


function Autopsy {
    rm -rf autopsy-4.19.2.zip
    rm -rf sleuthkit-java_4.11.1-1_amd64.deb
}

$2
