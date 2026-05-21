import keyboard 
import time
import datetime


def toggle_timer(started): # TODO: Something needs to stop it 
    started = not started
    if not started:
        return
    start = datetime.datetime.now()
    while True:
        print(f'\r{datetime.datetime.now() - start}')
        time.sleep(0.01)

def main():
    started = False
    while True:
        try:
            if keyboard.is_pressed('space'):
                print('\rYou pressed space mate!! ;)')
                toggle_timer(started)
                time.sleep(0.1)
            if keyboard.is_pressed('q'):
                print('See ya!')
                break
        except Exception as e: # TODO: do something with the exit status
            print(e)
            print('Make sure to use `sudo` when running this program.')
            break

if __name__ == '__main__':
    main()
