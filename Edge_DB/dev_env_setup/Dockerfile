# RHEL Host OS, but
# debian dev environment and sql environment
FROM debian

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

RUN apt-get install sudo curl tmux -y

RUN pip install flask flask_sock flask_sqlalchemy

RUN pip install requests psycopg

RUN apt-get install libpq5 -y

# new user. Default password is 1234
RUN useradd -m -G users,sudo -s /bin/bash -p "$(openssl passwd 1234)" developer
USER developer
WORKDIR /home/developer