
from venv import create
from pynput import keyboard
import pickle
import warnings
from defiasmessengerbot.config import get_data_path
import click
warnings.filterwarnings("ignore")

def create_intro_message(send_screen_wo_str, send_screen_wi_str):
    intro_message = \
    f"""** TEST de Hotkeys del DefiasMessengerBot **
    
    Presionar las siguientes combinaciones de teclas para probar su funcionamiento:
        - Enviar Screenshot SIN UI al BOT: ", {send_screen_wo_str}
        - Enviar Screenshot CON UI al BOT: ", {send_screen_wi_str}
        - Salir del test: <esc>
    """
    return intro_message

def on_activate_print_wo():
    click.echo("Envío SIN User Interface")

def on_activate_print_wi():
    click.echo("Envío CON User Interface")

def on_activate_exit():
    click.echo("Test finalizado")
    exit()

def run_defiasmessengerbot_test():

    # Load pickle file:
    with open(get_data_path(), "rb") as f:
        data = pickle.load(f)

    # Load keyboard config from pickle:
    send_screen_wo_str = data["sk_key_wo"]
    send_screen_wi_str = data["sk_key_wi"]

    # Define messages:
    test_intro = create_intro_message(send_screen_wo_str, send_screen_wi_str)

    # Start Bot
    click.echo(test_intro)

    with keyboard.GlobalHotKeys({
            send_screen_wo_str: on_activate_print_wo,
            send_screen_wi_str: on_activate_print_wi,
            "<esc>": on_activate_exit
            }) as listener:
        listener.join()

if __name__ == "__main__":
    run_defiasmessengerbot_test()