# from flask import Flask, request, jsonify
# from flask_sock import Sock
# import requests

# def main():
#     theta = 45
#     phi = 90
#     r = 5.5
#     url = "http://127.0.0.1:5000/api/detection/getLocation"
#     payload = {
#         "theta": theta,
#         "phi": phi,
#         "r": r
#     }
#     response = requests.post(url, json=payload)
#     if response.status_code == 200:
#         print('Data sent successfully.')
#     else:
#         print('Error:', response.text)
        

# if __name__ == '__main__':
#     main()