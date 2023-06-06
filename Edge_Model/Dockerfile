FROM python:3.9
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip install --upgrade pip setuptools wheel

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Set the environment variable
ENV FLASK_APP=app.py

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
