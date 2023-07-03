# shot detect dockerfile

FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Gunicorn
RUN pip install gunicorn

# Install the Python dependencies
RUN pip install flask-sock
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip install --upgrade pip setuptools wheel
RUN pip install pyaudio

COPY . .

# Set the environment variable
ENV FLASK_APP=app.py

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
# Create the output data true(1) and false(0)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
# CMD ["flask", "run", "--host=0.0.0.0"]
