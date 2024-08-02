import requests
import pyautogui
import time
import platform
import json
from executor import execute_command  # Ensure this module is properly defined to handle the commands
import datetime

# Function to get current timestamp with millisecond precision
def get_current_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'


# Configuration
BACKEND_URL = "http://192.168.137.228:8000"

# Get the screen size and OS information
screen_width, screen_height = pyautogui.size()
os_info = platform.platform()

# Prepare initial data for the session
prompt = "Start of session: Download the following Github repository: Mobile Agent, Cradle Github, RustDesk Github"
frontend_info = {
    "screen_size": f"{screen_width}x{screen_height}",
    "os_info": os_info
}

# Initial session setup
response = requests.post(f"{BACKEND_URL}/sessions/", json={"prompt": prompt, "frontend_info": frontend_info, "is_script": True, "is_script_link": True,"script_name_link": "http://public2.yuantsy.com/Project/DesktopAgent/Scripts/Script_win_DownloadGithubZip.json"})
session_data = response.json()
session_id = session_data.get("session_id")
print(session_data)

try:
    last_action = "START"
    last_action_timestamp = get_current_timestamp()  # Use the new timestamp function

    while True:
        # Take a screenshot and save it
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        
        # Get current timestamp for the screenshot with millisecond precision
        screenshot_timestamp = get_current_timestamp()
        
        with open('screenshot.png', 'rb') as f:
            files = {
                "screenshot": f,
                "screenshot_timestamp": (None, screenshot_timestamp),
                "last_action": (None, last_action),
                "last_action_timestamp": (None, last_action_timestamp)
            }
            response = requests.post(f"{BACKEND_URL}/sessions/{session_id}", files=files)
        
        # Check response and update action details
        if response.status_code == 200:
            action_data = response.json()
            action_command = action_data.get('next_action')
            print(f"Action to perform: {action_command}")

            # Update last action details
            last_action = action_command
            last_action_timestamp = screenshot_timestamp

            if action_command == "END":
                print("Session ended by the server.")
                break

            # Execute the action using the executor module
            if action_command:
                execute_command(action_command)

            # Small delay before next loop iteration
            time.sleep(3)
        else:
            print("Error from server:", response.text)
            break

except KeyboardInterrupt:
    print("Session ended by user.")
