from flask import Flask, request, jsonify
from flask_sock import Sock
from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__)
sock = Sock(app)

@app.route('/api/detectShot', methods=['POST'])
def detect_shot():
    #file = request.files['file']

    #if 'file' not in request.files:
   #     return 'No file part in the request'

    #if file.filename == '':
   #     return 'No selected file'
    # send file to shot detector

    # result = subprocess.run(['python', '-c', 'import random; print(random.randint(0, 1))'], stdout=subprocess.PIPE)
    # output = result.stdout.decode('utf-8').strip()
    # random_number = int(output)
    subprocess_cmd = ['python', 'detector_out.py']
    subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)
    if subprocess_output.returncode != 0:
            return jsonify({'error': 'Subprocess failed'}), 500
   
    
    output_filename = subprocess_output.stdout.strip()
    directory_path , filename = os.path.split(output_filename)
    process_detect_path = os.path.join(directory_path, filename)

    if not os.path.exists(process_detect_path):
         return jsonify({'error': 'Processed file not found'}), 500
    
    
    # get return and return
    # shot = False
    # if random_number == 1:
    #     shot = True

    # resp = {S
    #     'shot':shot
    # }

    # return jsonify(resp)
    return send_file(process_detect_path, as_attachment=True)
        