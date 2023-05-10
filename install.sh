#!/bin/bash
# Video Download Terminal
echo "Hello "
user=$ whoami
echo "$user"
echo "Init install packges"
echo "Upgrade system"
sudo apt update && sudo apt upgrade -y
echo "Install Packges"
sudo apt install python3
sudo apt install python-pip
sudo apt-get install youtube-dl
cd /home/$user
echo "###Alias" >> ~/.bash_aliases
echo "alias aliasconf='nano ~/.bash_aliases'" >> ~/.bash_aliases
echo "###comandos" >> ~/.bash_aliases
echo "alias dvs='pytho3 ~/DVS/src/main.py'" >> ~/.bash_aliases
source ~/.bash_aliases
