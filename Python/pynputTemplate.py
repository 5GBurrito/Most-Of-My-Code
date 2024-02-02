from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
import time

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
        mouse.click(MouseController().Button.left)

# Function to simulate a right mouse click
def right_click(times=1):
    for _ in range(times):
        mouse.click(MouseController().Button.right)

# Example usage
if __name__ == "__main__":
    try:
        # Move the mouse to coordinates (100, 100)
        move_mouse(100, 100)
        time.sleep(1)  # Pause for 1 second

        # Simulate pressing and releasing the 'a' key
        press_and_release_key('a')
        time.sleep(1)

        # Type the string "Hello, pynput!"
        type_text("Hello, pynput!")
        time.sleep(1)

        # Simulate a left mouse click
        left_click()

        # Simulate a right mouse click
        right_click()

        # You can add more actions based on your requirements

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure that the mouse and keyboard are left in a stable state
        # You can add cleanup code here if needed
        pass
