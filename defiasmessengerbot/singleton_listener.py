from pynput import keyboard
from defiasmessengerbot.key_utils import convert_keylist2str
import click

class Singleton:
    instance = None
    keys = []
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def on_press(self, new_key):
        if new_key == keyboard.Key.esc:
            # Stop listener
            return False
        else:
            self.keys.append(new_key)

    def on_release(self, new_key):
        self.show_keys()

        return False

    def reset_keys(self):
        self.keys = []
    
    def show_keys(self):
        MSG = f"Hotkeys pressed: {convert_keylist2str(self.keys)}"

        # Print keys joined by "+":
        click.echo(MSG)

def get_keys_from_user():
    # Restart Singleton:
    Singleton().reset_keys()

    # Start pynput listener:
    start_listener()
    
    # retrieve keys:
    return Singleton().keys

def start_listener():
    # Collect events until released
    with keyboard.Listener(
            on_press=Singleton().on_press,
            on_release=Singleton().on_release,
            suppress=True) as listener:
            listener.join()