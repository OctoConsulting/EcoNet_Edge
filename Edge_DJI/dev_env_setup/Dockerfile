FROM python:3.7-slim-buster

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/dronekit/dronekit-python.git && \
    cd dronekit-python && \
    pip install -r requirements.txt && \
    python setup.py build && \
    python setup.py install
#RUN git clone https://github/RosettaDrone/rosettadrone.git
RUN pip install opencv-python

WORKDIR /app
COPY . /app

