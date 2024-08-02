import os
import time
import pyautogui

def enter_exit_full_screen():
    time.sleep(3)  # Wait for 3 seconds
    apple_script = """
    tell application "System Events"
        keystroke "f" using {control down, command down}
    end tell
    """
    os.system(f"osascript -e '{apple_script}'")

def minimize_window():
    time.sleep(3)  # Wait for 3 seconds
    apple_script = """
    tell application "System Events"
        keystroke "m" using {command down}
    end tell
    """
    os.system(f"osascript -e '{apple_script}'")

def close_window():
    time.sleep(3)  # Wait for 3 seconds
    apple_script = """
    tell application "System Events"
        keystroke "w" using {command down}
    end tell
    """
    os.system(f"osascript -e '{apple_script}'")


# enter_exit_full_screen()  # Yiyun: this works well
# minimize_window()  # Yiyun: this works well
close_window()  # Yiyun: this works well



"""
Yiyun: This function does not work on my Mac, it turns out command + f only, opened a search bar.
"""
def toggle_full_screen():
    # Give yourself a couple of seconds to switch to the desired window
    time.sleep(2)

    # Press the shortcut to toggle full screen
    pyautogui.hotkey('ctrl', 'command', 'f')


