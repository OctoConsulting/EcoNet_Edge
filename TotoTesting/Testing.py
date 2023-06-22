import simple_websocket

def main():
    ws = simple_websocket.Client('ws://{host_ip}:8001/toto/192.168.53.1')
    try:
        while True:
            data = ws.receive()
            print(f'< {data}')
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()

if __name__ == '__main__':
    import os
    host_ip = os.popen('ipconfig').read().split('IPv4 Address. . . . . . . . . . . : ')[1].split('\n')[0]
    main()

if __name__ == '__main__':
    main()