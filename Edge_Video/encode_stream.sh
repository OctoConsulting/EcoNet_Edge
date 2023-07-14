#!/bin/bash

# file that encodes an rtsp stream into an hls stream (.m3u8). Currently
# hardcoded to the default ip address of Parrot drones

# TODO: --drone_number argument for differentiating between drones
# TODO: detect if a stream is running for a certain drone, and do not start a
# new enode process
    # ffmpeg -fflags nobuffer \
    # -loglevel debug \
    # -rtsp_transport tcp \
    # -i rtsp://192.168.53.1:554/live \
    # -vsync 0 \
    # -copyts \
    # -vcodec copy \
    # -movflags frag_keyframe+empty_moov \
    # -an \
    # -hls_flags delete_segments+append_list \
    # -f segment \
    # -segment_list_flags live \
    # -segment_time 1 \
    # -segment_list_size 3 \
    # -segment_format mpegts \
    # -segment_list /srv/feed1/streaming.m3u8 \
    # -segment_list_type m3u8 \
    # -segment_list_entry_prefix /stream/ \
    # /srv/feed1/%d.ts

    ffmpeg -y \
    -i rtsp://192.168.53.1:554/live \
      /srv/feed1/streaming.m3u8
# ffmpeg -fflags nobuffer \
#   -loglevel debug \
#   -rtsp_transport tcp \
#   -i "rtsp://192.168.53.1/live" \
#   -vsync 0 \
#   -copyts \
#   -vcodec copy \
#   -movflags frag_keyframe+empty_moov \
#   -an \
#   -hls_flags delete_segments+append_list \
#   -f hls \
#   -hls_time 1 \
#   -hls_list_size 3 \
#   -hls_segment_type mpegts \
#   /srv/feed1/streaming.m3u8 &
# cp ./index.html /srv/feed1/index.html # for reverse-proxy issues
