# import post_queries
import requests
import json

print("Testing POST Requests")
print("Test post_marker_db")
data={
    '_ID': "e1d372a4-53f4-4037-b83c-abc7832ee1d5",
    '_Lat': 36.695633889847855,
    '_Lon': 36.695633889847855,
    '_Type': 'drone',
    '_isActive': True,
    '_Alt': 50,
    '_Direction': 20,
    '_Distance': 100,
    '_Timestamp': 0,
}

headers = {'Content-Type': 'application/json'}
json_data = json.dumps(data)

r = requests.post('http://localhost:80/db/post_marker_db', data=json_data, headers=headers)
print(r.status_code)
print(r.text)

r = requests.get('http://localhost:80/db/get_all_markers')

print(r.json())

r = requests.delete(f'http://localhost:80/db/delete_marker_db/{data["_ID"]}')
print(r.status_code)
print(r.text)

r = requests.get('http://localhost:80/db/get_all_markers')

print(r.json())