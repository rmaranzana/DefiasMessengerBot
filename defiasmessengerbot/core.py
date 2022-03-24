
from pynput import keyboard
import time
import pickle
import warnings
import threading
from defiasmessengerbot.key_utils import press_and_release_key
from defiasmessengerbot.discordbot import DiscordBot
from defiasmessengerbot.images_utils import search_for_new_image
from defiasmessengerbot.config import get_data_path
import click
import os
warnings.filterwarnings("ignore")

def read_and_send_images(bot):
    # Wait a sec:
    time.sleep(1)
    
    # Search for new photo:
    new_photo = search_for_new_image(bot.path)
    
    # Send file to channel:
    bot.send_file(new_photo)

def flash_UI_and_send(bot, special_hotkeys, screenshot_key):
    # Deactivate UI:
    press_and_release_key(special_hotkeys) # hide ui
    # Take Screenshot:
    press_and_release_key(screenshot_key)
    time.sleep(0.1)
    # Activate UI:
    press_and_release_key(special_hotkeys) # show ui

    # Read and send:
    read_and_send_images(bot)

def on_activate_print_wo(bot, special_hotkeys, timing):
    MSG = "Envío SIN UI"

    click.echo(MSG)

    # Threadding:
    fun_1 = lambda: flash_UI_and_send(bot, special_hotkeys, timing) 
    t = threading.Thread(target=fun_1)
    t.start()

def on_activate_print_wi(bot):
    MSG = "Envío CON UI"

    click.echo(MSG)

    # Threadding:
    fun_2 = lambda: read_and_send_images(bot) 
    t = threading.Thread(target=fun_2)
    t.start()

def run_defiasmessengerbot():

    with open(get_data_path(), "rb") as f:
        data = pickle.load(f)

    # Get token and channel ID from env variables.
    token = os.environ['DEFIASMESSENGERBOT_TOKEN']
    channel_id = os.environ['DEFIASMESSENGERBOT_CHANNELID']

    # Get configs from pickle file
    path = data["path"]
    special_hotkeys = data["special_hotkeys"]
    username = data["username"]
    send_screen_wo_str = data["sk_key_wo"]
    send_screen_wi_str = data["sk_key_wi"]
    screenshot_key = data["screenshot_key"]

    # Start Discord Client:
    bot = DiscordBot(channel_id, username, path)

    # Configurar on_press dependiendo del sistema:
    on_press_wo = lambda: on_activate_print_wo(bot, special_hotkeys, screenshot_key)
    on_press_wi = lambda: on_activate_print_wi(bot)

    # Start Bot

    ## Prompt messages:
    MSG_INIT = "Iniciando..."
    MSG_SEND_WO = f"Enviar Screenshot SIN UI al BOT: {send_screen_wo_str}"
    MSG_SEND_WI = f"Enviar Screenshot CON UI al BOT: {send_screen_wi_str}"

    click.echo(MSG_INIT)
    click.echo(MSG_SEND_WO)
    click.echo(MSG_SEND_WI)

    ## Listener:
    with keyboard.GlobalHotKeys({
            send_screen_wo_str: on_press_wo,
            send_screen_wi_str: on_press_wi
            }) as listener:
        bot.client.run(token)
        listener.join()

if __name__ == "__main__":
    run_defiasmessengerbot()