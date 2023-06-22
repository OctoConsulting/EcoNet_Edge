FROM python:3.8.17-slim-bullseye

# Set the working directory inside the container
WORKDIR /app
#RUN ["python", "droneProtocol.py"]


RUN apt-get update && apt-get upgrade -y
#RUN apt-get install -y python3 python3-pip

# build helpers :)



COPY . . 

RUN pip install flask
# RUN cat /etc/debian_version && sleep 15

# COPY . .
#RUN apt-get install python3-waitress -y

#ENV FLASK_APP = app.py
# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
