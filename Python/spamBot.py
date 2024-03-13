from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)

#for i in range(100):
while True:
    for char in "https://tenor.com/view/rat-spin-gif-10300642414513246571":
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(15)