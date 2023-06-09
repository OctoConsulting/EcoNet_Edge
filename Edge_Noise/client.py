import os
import subprocess
from flask import Flask, request, jsonify, send_file
import base64
import wave

app = Flask(__name__)

@app.route('/process_wav', methods=['POST'])
def process_wav():
    
    body = request.json

    base64_bytes = body['audio']

    # convert from base64 to bytes
    my_bytes = base64.b64decode(base64_bytes)

    # make .wav file
  
    with wave.open('myfile.wav', 'wb') as f:
        f.setnchannels(4)
        f.setsampwidth(2)
        f.setframerate(44100)
        f.writeframes(my_bytes)

    wav_path = 'myfile.wav'
    output_filename = 'out.wav'
    # Process the .wav file using audioPlayer.py as a subprocess
    subprocess_cmd = ['python', 'JSP.py', wav_path, output_filename] 
    # arg1 = input file, arg2 = out file
     
    subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)
    
    # Check if the subprocess succeeded
    if subprocess_output.returncode != 0:
        print(subprocess_output.stderr.strip(), flush= True)
        return jsonify({'Subprocess failed': subprocess_output.stderr.strip()}), 501
    
    # # Extract the processed WAV filename  and directory from the stdout of the subprocess
    # output_filename = subprocess_output.stdout.strip()
    
    # # Splitting the direcorty and filename into two seperate variables
    # directory_path, filename = os.path.split(output_filename)

    # # Validating the full path to the processed file
    # processed_wav_path = os.path.join(directory_path, filename)

    # # Check if the processed file exists
    # if not os.path.exists(processed_wav_path):
    #     return jsonify({'error': output_filename}), 500
    
    resp = {}
    with open(output_filename, 'rb') as fd:
        contents = fd.read()
        resp['audio'] = convert_to_base64(contents)

    return jsonify(resp)

def convert_to_base64(byte_array):
    base64_bytes = base64.b64encode(byte_array)
    return base64_bytes.decode('utf-8')

if __name__ == '__main__':
    app.run()
