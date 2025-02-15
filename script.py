from pynput import keyboard
import threading
import time

# Global flags
move_forward = False
move_reverse = False
move_left = False
move_right = False
stop_movement = False

def forward():
    global move_forward
    while True:
        if move_forward and not move_reverse and not stop_movement:
            print("Forward")
        time.sleep(1)

def reverse():
    global move_reverse
    while True:
        if move_reverse and not stop_movement:
            print("Reverse")
        time.sleep(1)

def on_press(key):
    global move_forward, move_reverse, move_left, move_right, stop_movement

    try:
        key = key.char  # Handles letter keys (W, A, S, D, C, P, O)
    except AttributeError:
        key = key.name  # Handles special keys (Arrow keys)

    if key in ["w", "up"]:
        move_forward = True

    if key in ["s", "down"]:
        move_reverse = True
        move_forward = False  # Interrupts forward

    if key in ["a", "left"]:
        move_left = True

    if key in ["d", "right"]:
        move_right = True

    # Both left and right pressed together -> STOP for 5 seconds
    if move_left and move_right:
        stop_movement = True
        print("Stopping for 5 seconds...")
        time.sleep(5)
        stop_movement = False

    # Camera activation
    if key == "c":
        stop_movement = True
        print("Camera activated. Waiting for input (P for person, O for object)...")
        return  # Prevents continuous execution

def on_release(key):
    global move_forward, move_reverse, move_left, move_right, stop_movement

    try:
        key = key.char
    except AttributeError:
        key = key.name

    if key in ["w", "up"]:
        move_forward = False

    if key in ["s", "down"]:
        move_reverse = False
        move_forward = True  # Resume forward when S is released

    if key in ["a", "left"]:
        move_left = False

    if key in ["d", "right"]:
        move_right = False

    if key == "c":
        while True:
            person = input("Detected something! Press 'P' for Person or 'O' for Object: ").lower()
            if person == "p":
                print("Good morning, human")
                print("Reversing for 5 seconds...")
                time.sleep(5)
                print("Moving Forward + Right")
                break
            elif person == "o":
                print("Reversing...")
                time.sleep(2)
                print("Moving Forward + Left")
                break

        stop_movement = False  # Resume movement

# Start movement threads
threading.Thread(target=forward, daemon=True).start()
threading.Thread(target=reverse, daemon=True).start()

# Start keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
