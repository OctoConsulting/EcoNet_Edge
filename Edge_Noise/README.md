
# EchoNet API
READ RUN LOCAL SECTION BELOW FIRST!

This portion of the echo_net project focusing on taking inpud data from the shot detector and preprocessing the data back into a .wav file. 


You must have both the client script(master of subprocess) and the subprocess script() together for this code to work. 

if your running outside of a container first run 

```Shell
python3 ./client.py
```

Call the serving flask script

###### CURL COMMAND####

We need to pass a .wav file into the script, in order for core functionality to work. 

```Shell
curl +X POST +F "file=@/dir/to/file.wav" localhost:5000/process_wav
```
+X looks for a specific request type
+F specifies adding a file to send with curl, 
Double quotes are need and use the file= and location of file
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd Edge_ANoise
```

```making a vitual enviroment

  python -m venv .venv

  .venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

