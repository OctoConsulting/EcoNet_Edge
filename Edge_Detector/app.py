from flask import Flask, request, jsonify
from flask import Flask, send_file
import subprocess
import os
import json

app = Flask(__name__)

@app.route('/api/detectShot', methods=['GET'])
def detect_shot():
    #file = request.files['file']

    #if 'file' not in request.files:
   #     return 'No file part in the request'

    #if file.filename == '':
   #     return 'No selected file'

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

                # send resp as in the body
                # send filePath seperatly

        if not os.path.exists(filePath):
                return jsonify({'error': 'Processed file not found'}), 502


        # get return and return
        # return jsonify(resp)

        return send_file(filePath, as_attachment=True, download_name='downloaded.txt')
        
#         #Protocols: dict file ftp ftps http https imap imaps pop3 pop3s smtp smtps telnet tftp
# Features: AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile NTLM SPNEGO SSL SSPI threadsafe Unicode UnixSockets