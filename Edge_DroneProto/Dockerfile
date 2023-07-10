# Drone Protocol Dockerfile
FROM debian:bullseye

WORKDIR /app


# basics
RUN apt-get update
RUN apt-get upgrade -y
# dev basics
#RUN apt-get install -y git emacs-nox ssh iputils-ping ssh

# python
RUN apt-get update && apt-get install -y python3 python3-pip

# build helpers :)
# RUN apt-get install -y build-essential clinfo curl debconf-utils

# # python depends
# RUN apt-get install python3-opencv python3-opengl -y

# olympe depends
RUN apt-get update && apt-get install libgl1 -y 
# libgl1-mesa-glx -y

#RUN pip install opencv-python pysdl2 pysdl2-dll
RUN pip install flask
RUN pip install simple-websocket
# olympe
RUN pip install parrot-olympe
COPY . . 

ENV FLASK_APP=app.py

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
# CMD ["flask", "run", "--host=0.0.0.0"]

CMD ["flask", "run", "--host=0.0.0.0"]