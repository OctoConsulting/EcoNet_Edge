# Dev environment container for parrot drone

# RHEL Host OS, but
# debian dev environment and drone container
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

RUN adduser -D developer

RUN apt-get install lsb-release -y

USER developer
ENTRYPOINT ["su"]
CMD ["developer", "/bin/bash"]

# parrot
RUN apt-get libgl1 && pip install parrot-olympe