#!/bin/bash
# script run at container startup. We run a waitress server, and broadcast it
# along with the webpage with nginx
nginx &
waitress-serve --host "0.0.0.0" --port=5000 app:app
#bash ./encode_vid.sh
#bash ./encode_stream.sh