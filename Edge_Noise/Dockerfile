FROM python:3.9 

ADD client.py .

WORKDIR /app

COPY . /app/
COPY audioPlayer.py /app

RUN pip install scikit-learn
RUN pip install -U Flask
RUN pip install flask-socketio




#EXPOSE 5000


ENV FLASK_APP=client.py

CMD ["flask", "run", "--host=0.0.0.0"]
