from flask import Flask, request
import droneProtocol

app = Flask(__name__)

 
# Dictionary to store information about active drones
active_drones = {}

 

@app.route('/drones/<drone_id>/command', methods=['POST'])
def send_command(drone_id):
    command = request.json['command']
    if drone_id in active_drones:
        # Send the command to the specified drone
        # Your logic to send the command to the drone goes here
        tempD = get_key(active_drones, drone_id)
        droneProtocol.main(tempD)
        return f"Command '{command}' sent to Drone {drone_id}"
    else:
        return f"Drone {drone_id} not found"

#helper methd to iterate throught the dictionary to find the correct drone
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

@app.route('/drones/<drone_id>/status')
def get_status(drone_id):
    if drone_id in active_drones:
        # Retrieve and return the status of the specified drone
        # Your logic to retrieve the drone status goes here
        status = active_drones.get(drone_id)
        return f"Status of Drone {drone_id} is {status}"
    else:
        return f"Drone {drone_id} not found"

 


@app.route('/drones')
def get_active_drones():
    return "Active Drones: " + ', '.join(active_drones.keys())

 


@app.route('/drones/<drone_id>', methods=['POST'])
def add_drone(drone_id):
    if drone_id not in active_drones:
        # Add the new drone to the active drones dictionary
        active_drones[drone_id] = {}
        return f"Drone {drone_id} added successfully"
    else:
        return f"Drone {drone_id} already exists"

 


@app.route('/drones/<drone_id>', methods=['DELETE'])
def remove_drone(drone_id):
    if drone_id in active_drones:
        # Remove the specified drone from the active drones dictionary
        del active_drones[drone_id]
        return f"Drone {drone_id} removed successfully"
    else:
        return f"Drone {drone_id} not found"

 


if __name__ == '__main__':
    app.run()