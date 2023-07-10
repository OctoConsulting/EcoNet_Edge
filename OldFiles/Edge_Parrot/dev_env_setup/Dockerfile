# Parrot drone development container based on Debian 11

FROM debian:bullseye

# basics
RUN apt-get update
RUN apt-get upgrade -y

# dev basics
RUN apt-get install -y git emacs-nox ssh iputils-ping ssh

# python
RUN apt-get install -y python3 python3-pip

# build helpers :)
RUN apt-get install -y build-essential clinfo curl debconf-utils

# python depends
RUN apt-get update && apt-get install python3-opencv python3-opengl -y

# olympe depends
RUN apt-get update && apt-get install -y libgl1 libgl1-mesa-glx lsb-release
RUN pip install opencv-python pysdl2 pysdl2-dll

# olympe
RUN pip install parrot-olympe

# parrot-olympe repo
RUN apt-get install lsb-release sudo curl -y
RUN curl --fail --silent --show-error \
    --location https://debian.parrot.com/gpg | gpg --dearmor | \
    tee /usr/share/keyrings/debian.parrot.com.gpg > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/debian.parrot.com.gpg] \
    https://debian.parrot.com/ $(lsb_release -cs) main generic" | \
    tee /etc/apt/sources.list.d/debian.parrot.com.list
RUN apt-get update

# default user developer password 1234
RUN useradd -m -G users,sudo -s /bin/bash -p "$(openssl passwd 1234)" developer
USER developer
WORKDIR /home/developer

# copy sphinx install script
COPY postinst.sh /home/developer/