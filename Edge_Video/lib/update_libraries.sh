#!/bin/bash

# should be run inside this directory.

#curl https://cdn.jsdelivr.net/npm/hls.js@latest -o ./hls.js # the shorter one
curl https://unpkg.com/video.js@8.3.0/dist/video-js.css -o ./video-js.css 
curl https://unpkg.com/video.js@8.3.0/dist/video.js -o ./video.js 
curl https://unpkg.com/@videojs/http-streaming@3.4.0/dist/videojs-http-streaming-sync-workers.js -o ./stream_workers.js 
curl https://cdn.jsdelivr.net/npm/hls.js@latest/dist/hls.min.js -o ./hls.min.js 
curl https://cdn.jsdelivr.net/npm/hls.js@latest/dist/hls.min.js.map -o ./hls.min.js.map 
