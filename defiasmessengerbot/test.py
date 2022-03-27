
from pynput import keyboard
import pickle
import warnings
from defiasmessengerbot.config import get_data_path
from defiasmessengerbot.key_utils import get_timestamp
import click
warnings.filterwarnings("ignore")

def create_intro_message(send_screen_wo_str, send_screen_wi_str):
    TITLE = "DefiasMessengerBot TEST"
    
    INSTRUCTIONS = \
    f"""
    Press the following hotkeys to test them:
        - Send screenshot WITHOUT UI: {send_screen_wo_str}
        - Send Screenshot WITH UI: {send_screen_wi_str}
        - Exit Test: <esc>

    If any issue arise, repeat the config routine.
    """
    click.secho(TITLE, fg="red", bold=True)
    click.secho("-" * len(TITLE), fg='red', bold=True)
    click.echo(INSTRUCTIONS)


def on_activate_print_wo():
    MSG = f"{get_timestamp()} - Sent WITHOUT UI"

    click.echo(MSG)

def on_activate_print_wi():
    MSG = f"{get_timestamp()} - Sent WITH UI"

    click.echo(MSG)

def on_activate_exit():
    exit()

def run_defiasmessengerbot_test():

    # Load pickle file:
    with open(get_data_path(), "rb") as f:
        data = pickle.load(f)

    # Load keyboard config from pickle:
    send_screen_wo_str = data["sk_key_wo"]
    send_screen_wi_str = data["sk_key_wi"]

    # Define messages:
    create_intro_message(send_screen_wo_str, send_screen_wi_str)

    with keyboard.GlobalHotKeys({
            send_screen_wo_str: on_activate_print_wo,
            send_screen_wi_str: on_activate_print_wi,
            "<esc>": on_activate_exit
            }) as listener:
        listener.join()

if __name__ == "__main__":
    run_defiasmessengerbot_test()