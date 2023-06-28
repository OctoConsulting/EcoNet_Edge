import simple_websocket
import time

def main():
    time.sleep(10)
    ws = simple_websocket.Client('ws://localhost:5000/toto/192.168.53.1')
    try:
        while True:
            data = ws.receive()
            print(f'< {data}')
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()
        
if __name__ == '__main__':
    main()