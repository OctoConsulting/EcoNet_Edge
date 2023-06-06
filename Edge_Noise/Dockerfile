FROM python:3.9 

ADD client.py .


COPY . . 

RUN pip install scikit-learn
RUN pip install docker
RUN pip install -U Flask
RUN pip install flask-socketio




#EXPOSE 5000


ENV FLASK_APP=client.py

CMD ["flask", "run", "--host=0.0.0.0"]
