FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

COPY detector_out.py .
COPY app.py .

# Install the Python dependencies

RUN pip install flask-sock
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable
ENV FLASK_APP=app.py

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
# Create the output data true(1) and false(0)

CMD ["flask", "run", "--host=0.0.0.0"]
