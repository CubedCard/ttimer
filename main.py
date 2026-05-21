import sys
import threading
import keyboard 
import time
import datetime

running = True 
started = False
start = datetime.datetime.now()

def format_time(t):
    s = t.seconds
    m = (s // 60) % 60
    ms = int(t.total_seconds() * 100) - (s * 100)
    result = str()
    if m > 0:
        result += f'{m}:'
    result += f'{s}:{ms}'
    return result

def timer():
    while running:
        if started:
            t = datetime.datetime.now() - start
            time_str = format_time(t)
            sys.stdout.write(f'\r{time_str}')
            sys.stdout.flush()
        time.sleep(0.01)

def listen():
    while True:
        global started
        global start

        try:
            if keyboard.is_pressed('space'):
                started = not started
                if started:
                    start = datetime.datetime.now()
                time.sleep(0.1)
            if keyboard.is_pressed('q'):
                print('See ya!')
                break
        except Exception as e: # TODO: do something with the exit status
            running = False
            print(e)
            print('Make sure to use `sudo` when running this program.')
            break

def main():
    thread = threading.Thread(target=timer, daemon=True)
    thread.start()
    listen()

if __name__ == '__main__':
    main()
