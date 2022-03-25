import os
import pickle
import defiasmessengerbot
from defiasmessengerbot.config_utils import request_input, request_input_wo, request_input_wi
from defiasmessengerbot.key_utils import convert_keylist2str
import click

def get_data_path():

    return os.path.join(defiasmessengerbot.__path__[0], "data.pickle")

def get_dict_struct(path, screenshot_key, special_hotkeys, username, sk_key_wo, sk_key_wi):

    return {
        "path": path,
        "special_hotkeys": special_hotkeys,
        "username": username,
        "sk_key_wo": sk_key_wo,
        "sk_key_wi": sk_key_wi,
        "screenshot_key": screenshot_key
    }

def create_success_msg(screenshot_key, special_hotkeys):

    msg = \
    f"""
    ******************** Archivo de configuración .pickle creado ***********************
    *                                                                                  *
    * - IMPORTANTE: En el juego WoW hay que settear el botón de Screenshot como:       *
    *   {convert_keylist2str(screenshot_key)},                                         *
    *   Además, settear el botón ocultar/mostrar UI como:                              *
    *   {convert_keylist2str(special_hotkeys)}                                         *
    *                                                                                  *
    * - IMPORTANTE: Algunas combinaciones de telcas están reservadas y no funcionan.   *
    *   Primero ejecutar el test del Bot para asegurarse que las combinaciones elegidas*
    *   funcionan con el comando:                                                      *
    *        python -m defiasmessengerbot.test                                         *
    *                                                                                  *
    ************************************************************************************
    """

    return msg

def create_config_file(wow_path, screenshot_key, special_hotkeys, username, 
    sk_key_wo, sk_key_wi):
    
    # Get data path
    mod_path = get_data_path()

    # Create file
    data = get_dict_struct(
        wow_path, screenshot_key, special_hotkeys, username, 
        sk_key_wo, sk_key_wi
    )
    
    try:
        with open(mod_path, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

            click.echo(create_success_msg(screenshot_key, special_hotkeys))
            
    except:
        raise Exception("Error creating config file.")

def create_screenshot_message_wo(screenshot_key):
    MSG = f"take a Screenshot without UI using DefiasMessengerBot (CANNOT CONTAIN {convert_keylist2str(screenshot_key)})"

    return MSG

def create_screenshot_message_wi(screenshot_key):
    MSG = f"take a Screenshot with UI using DefiasMessengerBot (more than one key, MUST CONTAIN {convert_keylist2str(screenshot_key)})"

    return MSG

def input_n_complete():
    # Messages, WoW
    MSG_TITLE_WOW = "** SETTINGS - WORLD OF WARCRAFT **"
    MSG_WOW_PATH = "Enter the path where the Screenshots are saved in the WoW directory."
    MSG_SCREENSHOT = "take a Screenshot within the game"
    MSG_UI = "toggle the UI within WoW"

    # Mesages, Discord
    MSG_TITLE_DISCORD = "** SETTINGS - DISCORD **"
    MSG_USER = "Enter your username to identify who's sending the picture to Discord."

    # Inputs:

    ## WoW
    click.echo(MSG_TITLE_WOW)
    click.echo()
    wow_path = click.prompt(MSG_WOW_PATH, type=str)
    click.echo()
    screenshot_key = request_input(MSG_SCREENSHOT)
    click.echo()
    special_hotkeys = request_input(MSG_UI)
    click.echo()
    MSG_SCREEN_WO = create_screenshot_message_wo(screenshot_key)
    sk_key_wo = request_input_wo(MSG_SCREEN_WO, screenshot_key)
    click.echo()
    MSG_SCREEN_WI = create_screenshot_message_wi(screenshot_key)
    sk_key_wi = request_input_wi(MSG_SCREEN_WI, screenshot_key, sk_key_wo)
    click.echo()

    ## Discord
    click.echo(MSG_TITLE_DISCORD)
    click.echo()
    username = click.prompt(MSG_USER)
    click.echo()

    # Convert hotkeys to str:
    send_screen_wo_str = convert_keylist2str(sk_key_wo)
    send_screen_wi_str = convert_keylist2str(sk_key_wi)

    # Create file:
    create_config_file(
        wow_path, screenshot_key, special_hotkeys, username, 
        send_screen_wo_str, send_screen_wi_str
    )

if __name__ == "__main__":
    # Crear archivo
    input_n_complete()
