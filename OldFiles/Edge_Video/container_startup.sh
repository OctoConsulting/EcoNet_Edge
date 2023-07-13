#!/bin/bash

# run on startup on the encode container. Currently not in use.
# was located in Edge_Video/container_startup.sh

waitress-serve --host "0.0.0.0" --port=5000 app:app 

#bash ./encode_vid.sh
#bash ./encode_stream.sh