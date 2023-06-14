# RHEL Host OS, but
# debian dev environment and sql environment
FROM debian:bullseye

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

RUN apt-get install tmux -y

RUN apt-get install python3-waitress
#RUN mkdir -p /tmp/tmux-1000

#EXPOSE 5000

# new user. Default password is 1234
RUN useradd -m -G users,sudo -s /bin/bash -p "$(openssl passwd 1234)" developer
USER developer
WORKDIR /home/developer

COPY ../app.py .
COPY ../get_queries.py .
COPY ../put_queries.py .
COPY ../tessdata/put_test_data.py .

CMD [ "waitress-serve", "--host", "0.0.0.0", "--port=80", "app:app" ]
#CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]