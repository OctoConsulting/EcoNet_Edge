FROM debian:bullseye

WORKDIR /app


# basics
RUN apt-get update
RUN apt-get upgrade -y
# dev basics
RUN apt-get install -y git emacs-nox ssh iputils-ping ssh

# python
RUN apt-get install -y python3 python3-pip

# build helpers :)
RUN apt-get install -y build-essential clinfo curl debconf-utils

# olympe depends
RUN apt-get install -y libgl1 libgl1-mesa-glx lsb-release \
    python3-opencv python3-opengl
RUN pip install opencv-python pysdl2 pysdl2-dll
RUN pip install flask
RUN pip install simple-websocket
# olympe
RUN pip install parrot-olympe

COPY . . 

ENV FLASK_APP=app.py


CMD ["flask", "run", "--host=0.0.0.0"]
