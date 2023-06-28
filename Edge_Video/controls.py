import os
from enum import Enum

Status= Enum('Status', ['STARTED', 'STOPPED', 'FAILED'])

def start_drone(drone_number: int) -> Status:
  print(os.system('pwd'))
  return Status.STARTED

def stop_drone(drone_number: int) -> Status:
  print(os.system('pwd'))
  return Status.STOPPED