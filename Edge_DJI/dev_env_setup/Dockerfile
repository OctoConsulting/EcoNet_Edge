
FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev
RUN git clone https://github/RosettaDrone/rosettadrone.git
RUN pip install dronekit
#RUN git submodule update --init --recursive 

WORKDIR /app
COPY . /app

