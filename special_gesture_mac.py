import os

def enter_exit_full_screen():
    apple_script = """
    tell application "System Events"
        keystroke "f" using {control down, command down}
    end tell
    """
    os.system(f"osascript -e '{apple_script}'")

def minimize_window():
    apple_script = """
    tell application "System Events"
        keystroke "m" using {command down}
    end tell
    """
    os.system(f"osascript -e '{apple_script}'")

def close_window():
    apple_script = """
    tell application "System Events"
        keystroke "w" using {command down}
    end tell
    """
    os.system(f"osascript -e '{apple_script}'")
