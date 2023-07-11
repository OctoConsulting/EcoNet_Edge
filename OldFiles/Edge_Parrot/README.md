# Edge_Parrot
Parrot Drone Code for Project EdgeNet

Some nice links :)
https://developer.parrot.com/docs/groundsdk-tools/overview.html

https://developer.parrot.com/docs/olympe/installation.html

##Installation:

done with a Debian WSL machine. Will migrate to RHEL later. Should work with all debian-based glibc x86_64 systems

Install Conda

```bash
  sudo apt install wget
  wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
  chmod +x Anaconda3-2023.03-1-Linux-x86_64.sh

  ./Anaconda3-2023.03-1-Linux-x86_64.sh
```

add to $PATH and refresh the terminal

```bash
  echo "PATH=\"\$PATH:~/anaconda3/bin\"" >> .bashrc
  source .bashrc
```

install olympe

```bash
  wget https://github.com/Parrot-Developers/olympe/releases/download/v7.6.1/parrot_olympe-7.6.1-py3-none-manylinux_2_27_x86_64.whl

  conda install ./parrot_olympe-7.6.1-py3-none-manylinux_2_27_x86_64.whl
```