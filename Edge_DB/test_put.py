import put_queries
import requests

#put_queries.put_shot("2023-08-20 10:12:32 +05:00", "7820b2a002681a7e887bdd8fa73cbc0292ffec1c")

print("Test I")
data={
    'shot_time': '2023-08-20 10:12:32 +05:00',
    'preprocessed_audio_hash': '7820b2a002681a7e887bdd8fa73cbc0292ffec1c'
}
r = requests.post('http://localhost:5000/db/put_shot_raw', params=data)