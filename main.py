import keyboard 
import time
import datetime

global started 
started = False

def main():
    while True:
        try:
            if keyboard.is_pressed('space'):
                print('\rYou pressed space mate!! ;)')
                global started
                started = not started
                time.sleep(0.1)
            if keyboard.is_pressed('q'):
                print('See ya!')
                break
        except Exception as e: # TODO: do something with the exit status
            print(e)
            print('Make sure to use `sudo` when running this program.')
            break
        start = datetime.datetime.now()
        while started:
            print(f'\r{datetime.datetime.now() - start}')
            time.sleep(0.01)

if __name__ == '__main__':
    main()
