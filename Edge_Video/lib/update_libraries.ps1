$ErrorActionPreference= "Stop"

# file to get client-side js HLS stream dependencies locally
# should be run inside this directory.

# Small Test index.html
Invoke-WebRequest "https://cdn.jsdelivr.net/npm/hls.js@latest" `
  -OutFile .\hls.js

# Surge App
Invoke-WebRequest "https://unpkg.com/video.js@8.3.0/dist/video-js.css" `
  -OutFile .\video-js.css
Invoke-WebRequest "https://unpkg.com/video.js@8.3.0/dist/video.js" `
  -OutFile .\video.js

$worker_url= "https://unpkg.com/@videojs/http-streaming@3.4.0"
$worker_url="$worker_url/dist/videojs-http-streaming-sync-workers.js"
Invoke-WebRequest "$worker_url" -OutFile .\stream_workers.js

Invoke-WebRequest "https://cdn.jsdelivr.net/npm/hls.js@latest/dist/hls.min.js" `
  -OutFile .\hls.min.js
$map_url= "https://cdn.jsdelivr.net/npm/hls.js@latest/dist/hls.min.js.map"
Invoke-WebRequest "$map_url" -OutFile .\hls.min.js.map
