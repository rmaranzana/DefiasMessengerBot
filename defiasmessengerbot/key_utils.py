from pynput import keyboard
import datetime

def check_key(i):
    key_str = str(i)
    return f"<{key_str.split('.')[-1]}>" if "Key" in key_str else key_str.replace("'", "")

def convert_keylist2str(key_list):
    key_list = list(map(check_key, key_list))
    return "+".join(key_list)

def press_and_release_key(hotkeys):
    kb = keyboard.Controller()

    [kb.press(i) for i in hotkeys]
    [kb.release(i) for i in hotkeys]

def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')