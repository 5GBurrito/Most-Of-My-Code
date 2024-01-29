from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)

for i in range(100):
    for char in "test test test":
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)