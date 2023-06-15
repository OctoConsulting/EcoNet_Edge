#Edge_DJI

Rosseta Drone- wrapper for DJI for AI scripting 
Dronekit-Python- used python compatability with Rosseta Drone for AI scripting
https://dronekit-python.readthedocs.io/en/latest/develop/installation.html

##important##
go into the Drone-kit base directory and update "collections import MutableMapping" to "collections.abc import MutableMapping" to avoid Python version conflicts

#imports for the drone-kit software:
$pip install dronekit

#IMPORTANT#
Must install and use DJI Assistant 2(Consumer Drones Series) for the mini 2 to communicate with droneKit
https://www.dji.com/downloads/softwares/dji-assistant-2-consumer-drones-series

Must also use send_mavlink() command to talk to the drone

