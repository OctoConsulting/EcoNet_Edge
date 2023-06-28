import os
from enum import Enum

Status= Enum('Status', ['STARTED', 'STOPPED', 'FAILED'])

def start_drone(drone_number: int) -> Status:
  os.system('./encode_vid.sh')
  return Status.STARTED

def stop_drone(drone_number: int) -> Status:
  os.system('./stop_encode.sh')
  return Status.STOPPED