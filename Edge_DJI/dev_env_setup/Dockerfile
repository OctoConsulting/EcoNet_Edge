
FROM python:3.7-slim-buster
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    build-essential \
    cmake \
    git \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev
RUN pip3 install dronekit
RUN git clone https://github/RosettaDrone/rosettadrone.git

WORKDIR /app
COPY . /app

