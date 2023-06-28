#!/bin/bash
nginx &
waitress-serve --host "0.0.0.0" --port=5000 app:app
#bash ./encode_vid.sh
#bash ./encode_stream.sh
