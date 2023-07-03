FROM python:3.11

WORKDIR /app

COPY . /app/

# Install Gunicorn
RUN pip install gunicorn

RUN pip install scikit-learn
RUN pip install -U Flask
RUN pip install flask-socketio

ENV FLASK_APP=client.py

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
CMD ["flask", "run", "--host=0.0.0.0"]
