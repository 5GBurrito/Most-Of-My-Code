#Import all neccessary features to code.
import RPi.GPIO as GPIO
from time import sleep

#If code is stopped while the solenoid is active it stays active
#This may produce a warning if the code is restarted and it finds the GPIO Pin, which it defines as non-active in next line, is still active#from previous time the code was run. This line prevents that warning syntax popping up which if it did would stop the code running.
GPIO.setwarnings(False)

#This means we will refer to the GPIO pins
#by the number directly after the word GPIO. A good Pin Out Resource can be found here https://pinout.xyz/
GPIO.setmode(GPIO.BCM)

#This sets up the GPIO 18 pin as an output pinGPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
    state = input("close 1, 2, b(oth), or n(one)")

    if state == "1":
        GPIO.output(17, 1)
        GPIO.output(18, 0)
    if state == "2":
        GPIO.output(17, 0)
        GPIO.output(18, 1)
    if state =="b":
        GPIO.output(17, 1)
        GPIO.output(18, 1)
    if state == "n":
        GPIO.output(17, 0)
        GPIO.output(18, 0)