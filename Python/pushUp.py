from random import randint
import random
from time import sleep
import pyttsx3


list = [
    "All the way up",
    "All the way down",
    "Half way down",
    "One quarter down",
    "Three quarters down"
]

while True:
    print(random.choice(list))
    sleep(randint(1,5))