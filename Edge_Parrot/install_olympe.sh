#!/bin/bash

# install anaconda
sudo apt install wget
wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
chmod +x Anaconda3-2023.03-1-Linux-x86_64.sh
./Anaconda3-2023.03-1-Linux-x86_64.sh -b

# add to path, refresh the terminal
echo "PATH=\"\$PATH:~/anaconda3/bin\"" >> .bashrc
source .bashrc

# install olympe
sudo apt install gcc
wget https://github.com/Parrot-Developers/olympe/releases/download/v7.6.1/parrot-olympe-src-7.6.1.tar.gz
tar -xvpf ./parrot-olympe-src-7.6.1.tar.gz

./olympe/install.sh -t all