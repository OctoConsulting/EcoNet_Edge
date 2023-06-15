FROM python:3.8
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

WORKDIR /app/bh_runner/klvdata-master

RUN python setup.py install

WORKDIR /app/bh_runner

CMD ["python", "bh_runner.py"]
