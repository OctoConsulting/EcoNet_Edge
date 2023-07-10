import requests
import json
import datetime
#put_queries.put_shot("2023-08-20 10:12:32 +05:00", "7820b2a002681a7e887bdd8fa73cbc0292ffec1c")

print("Testing PUT Requests")
print("Test update_marker_db")
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
print(r.text)

data={
    '_ID': "e1d372a4-53f4-4037-b83c-abc7832ee1d5",
    '_Lat': 36.695633889847855,
    '_Lon': 36.695633889847855,
    '_Type': 'drone',
    '_isActive': True,
    '_Alt': 50,
    '_Direction': 20,
    '_Distance': 100,
    '_Timestamp': 100,
}

json_data = json.dumps(data)
r = requests.put(f'http://localhost:80/db/update_marker_db/{data["_ID"]}', data=json_data, headers=headers)
print(r.status_code)
print(r.text)

r = requests.get('http://localhost:80/db/get_all_markers')

print(r.json())

print("")
print("Test update_shot")
data = {
    "id" : "test",
    "shot_time" : datetime.datetime.now(),
    "process_time" :datetime.datetime.now(),
    "event_id": -1,
    "preprocessed_audio_hash" : "1234",
    "postprocessed_audio_hash" : "5678",
    "distance" : 150,
    "microphone_angle" :30,
    "shooter_angle" :25,
    "latitude" :85,
    "longitude" :60,
    "gun_type" :'rifle',
}

headers = {'Content-Type': 'application/json'}
json_data = json.dumps(data)

r = requests.post('http://localhost:80/db/post_shot', data=json_data, headers=headers)
print(r.json)

# data = {
#     "shot_time" : datetime.datetime.now(),
#     "process_time" :datetime.datetime.now(),
#     "event_id": -1,
#     "preprocessed_audio_hash" : "1234",
#     "postprocessed_audio_hash" : "5678",
#     "distance" : 150,
#     "microphone_angle" :30,
#     "shooter_angle" :25,
#     "latitude" :85,
#     "longitude" :60,
#     "gun_type" :'rifle',
# }

# json_data = json.dumps(data)
# r = requests.put(f'http://localhost:80/db/update_shot/{data["id"]}', data=json_data, headers=headers)
# print(r.status_code)
# print(r.text)

# r = requests.get('http://localhost:80/db/get_all_markers')

# print(r.json())



# print("Test I")
# data={
#     'shot_time': '2023-08-20 10:12:32 +05:00',
#     'preprocessed_audio_hash': '7820b2a002681a7e887bdd8fa73cbc0292ffec1c'
# }
# r = requests.post('http://localhost:5000/db/put_shot_raw', params=data)