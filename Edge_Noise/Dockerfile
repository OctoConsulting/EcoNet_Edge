FROM python:3.10

WORKDIR /app


RUN pip install PyWavelets
RUN pip install numpy
RUN pip install librosa
RUN pip install flask

COPY . .

ENV FLASK_APP=client.py

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["flask", "run", "--host=0.0.0.0"]
