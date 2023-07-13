#!/bin/bash

# file to get client-side js HLS stream dependencies locally
# should be run inside this directory.

# Small Test index.html
curl https://cdn.jsdelivr.net/npm/hls.js@latest -o ./hls.js

# Surge App
curl https://unpkg.com/video.js@8.3.0/dist/video-js.css -o ./video-js.css
curl https://unpkg.com/video.js@8.3.0/dist/video.js -o ./video.js

worker_url="https://unpkg.com/@videojs/http-streaming@3.4.0"
worker_url="$worker_url/dist/videojs-http-streaming-sync-workers.js"
curl $worker_url -o ./stream_workers.js

curl https://cdn.jsdelivr.net/npm/hls.js@latest/dist/hls.min.js \
  -o ./hls.min.js
curl https://cdn.jsdelivr.net/npm/hls.js@latest/dist/hls.min.js.map \
  -o ./hls.min.js.map
