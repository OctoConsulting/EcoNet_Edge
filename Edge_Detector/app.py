from flask import Flask, request, jsonify
from flask import Flask, send_file
from flask_sock import Sock
import subprocess
import os
import json

app = Flask(__name__)
sock = Sock(app)

@sock.route('/api/detectShot', methods=['GET'])
def detect_shot(ws):

        while True:
                message = ws.recive()
                if message and message == 'file_upload':
                        file_data = ws.recive()
                        file = file_data['file']
                        
                        # this returns a tupple with file path and shot result
                        status = prossess_file(file)

                        # send_file(filePath, as_attachment=True, download_name='downloaded.txt')
                        
                        filePath = status['filePath']
                        shot = status['shot']

                        if not os.path.exists(filePath):
                                ws.send({'error': 'Processed file not found'})
                                return 
                        
                        #send the flie
                        ws.send({'file': filePath})

                        #send the json with the result of 
                        ws.send(jsonify(shot))

                        return
                else:
                        ws.send({'error': 'no file sent'})
                        return 



def prossess_file(file):
        subprocess_cmd = ['python', 'detector_out.py']
        subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)
        if subprocess_output.returncode != 0:
                return jsonify({'error': 'Subprocess failed'}), 501


        output = subprocess_output.stdout.strip()
                
        json_output = json.loads(output)
        print(json_output)

        resp = {}
        resp['shot'] = json_output['shot']
        filePath = json_output['filePath']

        return resp
        
