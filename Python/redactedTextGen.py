from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()

links = [
"██████", "███████████ ", "██ █", "███", "███", "███ ", "███", "██ "
]
currentLink= "https://youtu.be/dQw4w9WgXcQ"

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Liftoff")

#for i in range(30):
while True:

    #selects a  random link
    try:
        currentLink = random.choice(links)
    except:
        currentLink= "https://youtu.be/dQw4w9WgXcQ"

    for char in currentLink:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.01)        
print("all done :3")