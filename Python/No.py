import pyttsx3
import time

def speak(text):
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()

while True:
     speak("No")
     print("no")
     time.sleep(0.1)