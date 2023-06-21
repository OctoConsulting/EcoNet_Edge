How to Run Byte Array Update
1) Build Docker-Compose File using ("Docker-compose build")
2) Run Docker-Compose File using ("Docker-compose up")
3) Conversion of .Wav to Base64
	1X) CD to /Econet_Edge
	2X) CD to /Byte_arr_helper
	3X) RUN "Python file_to_encode.py /PATH/TO/FILE/{.wav}" 
	4X) COPY OUTPUT (Ctrl+C) from "out.txt"
	5X) PASTE base64 from out.txt into Testing_client.py (NOTE: ERASE the VALUE ASSOCIATED WITH "audio")
	TO AVOID SCROLLING USE CTRL+SHIFT+END to AUTOSCROOL TO BOTTOM.
	6x)RUN "python testing_client.py"