import simple_websocket
import os
import sys


def main():
    PARENT_PID = os.getpid()
    ws = simple_websocket.Client('ws://localhost:5000/api/detection/audio')
    try:
        while True:
            data = ws.receive()
            # take data an feed into shot detector
            # if data has shot 
                # fork and exec to new prossess
            shot = True
            if shot:
                # run preprossing
                # store in a file
                # maybe use subporssess or fork+exec
                os.fork()
                PID_AFTER_FORK = os.getpid()
                if PID_AFTER_FORK != PARENT_PID:
                    # might need pipe to send data from current to model and deployment code
                    program = 1
                    arguments = 1 
                    os.execlp(program, program, *arguments)
            
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()


if __name__ == '__main__':
    main()