import random
import time
import pyttsx3

def speak(text):
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()

list = [
    "All the way down",
    "All the way up",
    "Half way down",
    "One quarter down",
    "Three quarters down"
]

count = 1
lastValue = 0

print("Welcome to the jungle!")
speak("Welcome to the jungle!")
time.sleep(3.5)

while True:
    if lastValue == 0:
        value = random.randint(1, 4)
    else:
        value = random.randint(0, 4)
    print(list[value])
    speak(list[value])
    if value == 0:
        print(count)
        speak(count)
        count = count + 1
    lastValue = value
    time.sleep(random.randint(5, 10))