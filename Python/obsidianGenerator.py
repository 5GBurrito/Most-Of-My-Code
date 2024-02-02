from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from time import sleep

# Create instances of MouseController and KeyboardController
mouse = MouseController()
keyboard = KeyboardController()

# Function to move the mouse to a specific position
def move_mouse(x, y):
    mouse.position = (x, y)

# Function to simulate a key press and release
def press_and_release_key(key):
    keyboard.press(key)
    keyboard.release(key)

# Function to type a string
def type_text(text):
    keyboard.type(text)

# Function to simulate a left mouse click
def left_click(times=1):
    for _ in range(times):
        mouse.click(MouseController().left)

# Function to simulate a right mouse click
def right_click(times=1):
    for _ in range(times):
        mouse.click(MouseController().right)


sleep(5)


for  i in range(10):
    press_and_release_key("2")
    right_click()
    press_and_release_key("2")
    right_click()

