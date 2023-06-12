import os
import subprocess
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/process_wav', methods=['POST'])
def process_wav():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    # Check if the file has a valid extension
    if file.filename == '' or not file.filename.endswith('.wav'):
        return jsonify({'error': 'Invalid file type'}), 400
    
    # Save the WAV file
    wav_path = 'input.wav'
    file.save(wav_path)
    
    # Process the .wav file using audioPlayer.py as a subprocess
    subprocess_cmd = ['python', 'audioPlayer.py', wav_path]
    subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)
    
    # Check if the subprocess succeeded
    if subprocess_output.returncode != 0:
        return jsonify({'error': 'Subprocess failed'}), 500
    
    # Extract the processed WAV filename  and directory from the stdout of the subprocess
    output_filename = subprocess_output.stdout.strip()
    
    # Splitting the direcorty and filename into two seperate variables
    directory_path, filename = os.path.split(output_filename)

    # Validating the full path to the processed file
    processed_wav_path = os.path.join(directory_path, filename)

    wav_path = "DUDE"

# Check if the processed file exists
    if not os.path.exists(processed_wav_path):
        return jsonify({'error': 'Processed file not found'}), 500
    # Return the processed WAV file to the client
    return send_file(processed_wav_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
