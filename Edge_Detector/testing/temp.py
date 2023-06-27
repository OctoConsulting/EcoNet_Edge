import asyncio
import json
import simple_websocket

def main():
    ws = simple_websocket.Client(f'ws://localhost:5000/api/detectShot')
    # ws.recive()
    ws.send(b'\x02\x03\x05\x07')

    file = ws.receive()

    j = ws.receive()

    print(file)

    print(j)



if __name__ == "__main__":
    main()
