
in the dummy container in order for stdout to work
	1. subprocess_cmd = ['python', '{filename}.py',{argument for filename}]
    	    subprocess_output = subprocess.run(subprocess_cmd, capture_output=True, text=True)

	2. if subprocess_output.returncode != 0:
            return jsonify({'error': 'Subprocess failed'}), 500

	# extracts stdout filename 
	3. output_filename = subprocess_output.stdout.strip()
    
    	# Check if the processed file exists
   	 4. processed_wav_path = output_filename + '.wav'
   	 if not os.path.exists(processed_wav_path):
       	 	return jsonify({'error': 'Processed file not found'}), 500
    
    	# Return the processed WAV file to the client if file exist
   	 5. return send_file(processed_wav_path, as_attachment=True)

In order for the subprocess to work
	1. 
def (functionNAME)(ARGUMENT VARIABLE):
    try:
        # Read the input WAV file
        # Do any processing on the audio data here
        # For demonstration purposes, this example simply copies the input file to a new output file
        global output_filename
        output_filename = input_path.rsplit('.', 1)[0]  # Remove the extension
        output_path = output_filename + '_processed.wav'
        shutil.copyfile(input_path, output_path)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    # Expecting the input WAV file path as a command-line argument
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python audioPlayer.py <input_wav_file>\n')
        sys.exit(1)
    #takes in argument from client.py
    ARGUMENT VARIBALE = sys.argv[1]
    #sends the argument to the function
    process_audio(ARGUMENT VARIABLE)
    #sends the argument back into stdout to be read by mian
    sys.stdout.write(output_filename)




CURL -X POST -F 'file=@{filename}' 127.0.0.1:5000/dir

after file is ran with argument (if needed go to docker desktop)

fine specfic container instance, Files> app > pycache > output filename