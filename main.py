import requests
import pyautogui
import time
import platform
from executor import execute_command  # Ensure this module is properly defined to handle the commands

# Configuration
BACKEND_URL = "http://192.168.137.228:8000"

# Get the screen size and OS information
screen_width, screen_height = pyautogui.size()
os_info = platform.platform()

# Initial session setup
response = requests.get(f"{BACKEND_URL}/new_session/", params={"screen_size": f"{screen_width}x{screen_height}", "os_info": os_info})
print(response.json())

try:
    while True:
        # Take a screenshot and send to backend
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        with open('screenshot.png', 'rb') as f:
            response = requests.post(f"{BACKEND_URL}/upload_screenshot/", files={"image": f})
        
        # Extract the action command from the backend's response
        action_command = response.json().get('action_command', '')
        print(f"Action to perform: {action_command}")

        # Execute the action using the executor module
        if action_command:
            execute_command(action_command)

        # Small delay before next loop iteration
        time.sleep(3)

except KeyboardInterrupt:
    print("Session ended by user.")
