import json

data1= {
  "shot_time": "2023-04-20 06:09:55 +05:00",
  "audio_hash": "d0f875515d72d8ce4255443529b57ca2cf9ca95a"
}

data2= {
  "shot_time": "2023-04-20 06:12:32 +05:00",
  "audio_hash": "7820b2a002681a7e887bdd8fa73cbc0292ffec1c"
}

file= open("test_single.json", "w")
json.dump(data1, file, indent= 2)
file.close()

file= open("test_multi.json", "w")
json.dump([data1, data2], file, indent= 2)
file.close()