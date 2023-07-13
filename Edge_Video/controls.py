# file that includes functions to start and stop video for a drone given an arg.
# drone number.

import os
from enum import Enum

Status= Enum('Status', ['STARTED', 'STOPPED', 'FAILED'])

# starts encoding test_vid.mp4 into an HLS stream
def start_test() -> Status:
  os.system('/bin/bash ./encode_vid.sh')
  return Status.STARTED

# stops encoding test_vid.mp4
def stop_test() -> Status:
  os.system('/bin/bash ./encode_stop.sh')
  return Status.STOPPED

def start_drone(drone_number: int) -> Status:
  os.system('/bin/bash ./encode_stream.sh')
  return Status.STARTED

def stop_drone(drone_number: int) -> Status:
  os.system('/bin/bash ./encode_stop.sh')
  return Status.STOPPED
