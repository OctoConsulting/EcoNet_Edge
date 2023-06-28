FROM debian:bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY ./requirements.txt .

RUN apt-get update 
RUN apt-get upgrade -y


RUN apt-get install -y python3-pip

# Install Gunicorn
RUN pip install gunicorn
RUN pip install gunicorn flask

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# RUN pip install flask flask_sock flask_sqlalchemy flash-socketio
RUN pip install uvicorn

RUN pip install klvdata \
    && pip install psutil \
    && pip install ultralytics

RUN apt-get install libgl1-mesa-glx -y
RUN apt-get install libglib2.0-0 -y
RUN pip install --upgrade flask_sock

# Copy the entire project to the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application using Gunicorn
# CMD ["gunicorn" "-b" ":5000" "--threads" "100" "module:app"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
CMD ["flask", "run", "--host=0.0.0.0"]

