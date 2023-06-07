from flask import Flask, request, jsonify
from flask_sock import Sock
import random


app = Flask(__name__)
sock = Sock(app)


def main():
    #with open("testD.txt", "w") as f:
    #    f.write('Hello docker!')
     #  f.close()
    #...
    print(random.randint(0, 1))


if __name__ == "__main__":
    main()

