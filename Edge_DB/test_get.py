import requests
import json

print("Test I")
x= requests.get('http://localhost:80/db/get_all_shots')
x2= x.json()
assert(type(x2) == list)

print("Test II")
params= {
    'hash': "d0f875515d72d8ce4255443529b57ca2cf9ca95a"
}
x= requests.get('http://localhost:80/db/get_shot_by_pre', params= params)
x2= x.json()
print(type(x2))
print(x2)

print("Test III")
params= {
    'id': "1"
}
x= requests.get('http://localhost:80/db/get_shot_by_id', params= params)
print(x)
x2= x.json()
print(type(x2))
print(x2)