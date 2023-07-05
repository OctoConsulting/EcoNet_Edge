FROM debian:bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY ./requirements.txt .

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y python3-pip

# Install Gunicorn
RUN pip install gunicorn

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install flask flask_sock flask_sqlalchemy 

RUN pip install klvdata

RUN apt-get install libgl1-mesa-glx -y

RUN apt-get install libglib2.0-0 -y

RUN pip install psutil

RUN pip install ultralytics

# Copy the entire project to the container
COPY . .

# # Set the environment variable
# ENV FLASK_APP=app.py

# Expose the port that Flask will run on
EXPOSE 8000

# Run the Flask application using Waitress
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]


