import pyautogui
from special_gesture_mac import enter_exit_full_screen, minimize_window, close_window


def execute_command(command):
    action_type, params = command.split(':', 1)
    action_dict = {
        'move': execute_move,
        'click': execute_click,
        'double-click': execute_double_click,  # Added double-click
        'right-click': execute_right_click,    # Added right-click
        'scroll': execute_scroll,
        'key-down': execute_key_down,
        'key-up': execute_key_up,
        'press': execute_press,  # Single key press
        'type': execute_type,  # Type out a string
        'sequence': execute_sequence,
        'hold-click': execute_hold_click,
        'multi-click': execute_multi_click,
        'drag': execute_drag,
        'scroll-to': execute_scroll_to,
        'autocomplete-text': execute_autocomplete_text,
        'batch': execute_batch,
        'shortcut': execute_shortcut,

        'special_gesture_mac': execute_special_gesture_mac,
    }
    action_function = action_dict.get(action_type)
    if action_function:
        action_function(params)
    else:
        print(f"Action type '{action_type}' not recognized.")

def execute_move(params):
    x, y = map(int, params.split(','))
    pyautogui.moveTo(x, y)

def execute_click(params):
    x, y = map(int, params.split(','))
    pyautogui.click(x/2, y/2)

def execute_double_click(params):
    x, y = map(int, params.split(','))
    pyautogui.doubleClick(x, y)

def execute_right_click(params):
    x, y = map(int, params.split(','))
    pyautogui.rightClick(x, y)

def execute_scroll(params):
    amount = int(params)
    pyautogui.scroll(amount)

def execute_key_down(params):
    key = params
    pyautogui.keyDown(key)

def execute_key_up(params):
    key = params
    pyautogui.keyUp(key)

def execute_press(params):
    pyautogui.press(params)

def execute_type(params):
    pyautogui.write(params)

def execute_sequence(params):
    keys = params.split('+')
    for key in keys:
        pyautogui.press(key)

def execute_hold_click(params):
    key, x, y = params.split(',')
    pyautogui.keyDown(key)
    pyautogui.click(x=int(x), y=int(y))
    pyautogui.keyUp(key)

def execute_multi_click(params):
    x, y, times = map(int, params.split(','))
    pyautogui.click(x=x, y=y, clicks=times)

def execute_drag(params):
    x1, y1, x2, y2 = map(int, params.split(','))
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, button='left')

def execute_scroll_to(params):
    x, y = map(int, params.split(','))
    pyautogui.moveTo(x, y)
    pyautogui.scroll(500)  # Adjust scroll amount as necessary

def execute_autocomplete_text(params):
    prefix, options = params.split(',')
    pyautogui.write(prefix)
    pyautogui.typewrite(options)

def execute_batch(params):
    actions = params.split(';')
    for action in actions:
        execute_command(action)

def execute_shortcut(params):
    keys = params.split('+')
    pyautogui.hotkey(*keys)


def execute_special_gesture_mac(params):
    gesture = params.strip().lower()
    if gesture == 'enter_exit_full_screen':
        enter_exit_full_screen()
    elif gesture == 'minimize_window':
        minimize_window()
    elif gesture == 'close_window':
        close_window()
    else:
        print(f"Special gesture '{gesture}' not recognized.")