# RHEL Host OS, but
# debian dev environment and sql environment
FROM debian:bullseye

# basics
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install git emacs-nox tmux -y
RUN apt-get install sudo curl tmux ssh git -y

# for C
RUN apt-get install gcc -y

# ffmpeg
RUN apt-get install ffmpeg libavformat-dev libavcodec-dev -y

# new user. Default password is 1234
RUN useradd -m -G users,sudo -s /bin/bash -p "$(openssl passwd 1234)" developer
USER developer
WORKDIR /home/developer

CMD [ "/bin/bash" ]