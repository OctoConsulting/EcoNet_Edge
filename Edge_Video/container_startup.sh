#!/bin/bash
nginx &
waitress-serve --host "0.0.0.0" --port=8080 app:app
#bash ./encode_vid.sh
#bash ./encode_stream.sh
