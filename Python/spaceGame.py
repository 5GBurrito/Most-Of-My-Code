import time
import pyttsx3
import random

turnsPassed = 0

hunger = random.randint(0, 80)
thirst = random.randint(0, 80)
o2 = random.randint(20, 100)
sanity = random.randint(0, 80)
health = random.randint(0,80)
pain = random.randint(0, 80)

food = random.randint(20, 300)
water = random.randint(20, 300)
medicalSuplies = random.randint(0, 150)

def speak(text):
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()

print("What Mode?")
print("1 = Endless")



if input() == "1":
    print("You Chose Mode 1, Endless Mode")