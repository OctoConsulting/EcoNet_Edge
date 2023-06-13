import requests
import sys

def main(audio):
    print('deployment and prossess')
    # take in file from stdin
    # pass file to model
    # convert to drone portocal
    # select drone
        # sets up socket connection with drone
    # send drone

    url = 'api:5000/api'

    body = {}
    body['audio'] = audio

    resp_preprossessing = requests.post(f'http://{url}/preporessing', json=body)
    preprossessed = resp_preprossessing.json()

    response = requests.post(f'http://{url}/detection/getLocation', json=preprossessed)
    location = response.json()

    # analyze the location data -> make sure it is resonalble

    # if resonable
        # drone deployment operations




if __name__ == '__main__':
    main(sys.argv[1])