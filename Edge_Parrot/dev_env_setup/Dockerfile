# RHEL Host OS, but
# debian dev environment and drone container
FROM debian:buster

# basics
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
    git \
    emacs-nox

RUN apt-get install -y \
    python3 \
    python3-pip \
    ssh

RUN apt-get install lsb-release -y

# olympe
RUN apt-get install libgl1 -y && pip install parrot-olympe

# parrot repo
RUN apt-get install lsb-release sudo curl -y
RUN curl --fail --silent --show-error --location https://debian.parrot.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/debian.parrot.com.gpg > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/debian.parrot.com.gpg] https://debian.parrot.com/ $(lsb_release -cs) main generic" | sudo tee /etc/apt/sources.list.d/debian.parrot.com.list
RUN apt-get update

RUN useradd -m -G users,sudo -s /bin/bash -p "$(openssl passwd 1234)" developer
USER developer
WORKDIR /home/developer
COPY postinst.sh /home/developer/