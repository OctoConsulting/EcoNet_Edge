FROM python:3.11

WORKDIR /app

COPY . /app/

RUN pip install scikit-learn
RUN pip install -U Flask
RUN pip install flask-socketio

ENV FLASK_APP=client.py

CMD ["flask", "run", "--host=0.0.0.0"]
