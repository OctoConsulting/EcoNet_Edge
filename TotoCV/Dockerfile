FROM debian:bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY ./requirements.txt .

RUN apt-get update 
RUN apt-get upgrade -y

RUN apt-get update && apt-get install -y python3-pip

# Install Gunicorn
RUN pip install gunicorn

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install klvdata \
    && pip install psutil \
    && pip install ultralytics

RUN apt-get install libgl1-mesa-glx -y
RUN apt-get install libglib2.0-0 -y
RUN pip install --upgrade flask_sock
RUN apt-get install ssh -y

# Copy the entire project to the container
COPY . .

# CMD cd ../TotoCV/toto/bh_runner/kvldata-master
WORKDIR /app/toto/bh_runner/kvldata-master
CMD ["python3","setup.py","install"]
# Expose the port that Flask will run on
EXPOSE 5000
WORKDIR /app

# Run the Flask application using Gunicorn
# CMD ["gunicorn" "-b" ":5000" "--threads" "100" "module:app"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
CMD ["flask", "run", "--host=0.0.0.0"]

