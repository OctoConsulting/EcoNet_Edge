import simple_websocket


def main():
    # TODO change this to toto docker ip
    url = 'toto:5000/api'
    # TODO change the end point to match the flask app
    ws = simple_websocket.Client(f'ws://{url}/detection/audio')

    try:
        while True:
            data = ws.receive()

            # do something with the data
    
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main()