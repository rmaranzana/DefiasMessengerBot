import time
from defiasmessengerbot.singleton_listener import get_keys_from_user
from defiasmessengerbot.key_utils import convert_keylist2str
import click

def yn_request():

    MSG = "Confirm?"

    return click.confirm(MSG)

def request_input(accion):

    MSG = f"Enter hotkeys for {accion}"

    response = False
    while response != True:
        # Wait for imput
        time.sleep(0.3)

        # Get keys:
        click.echo(MSG)
        keys = get_keys_from_user()

        # Get response from user:
        response = yn_request()

    return keys

def request_input_wo(accion, screenshot):

    MSG = f"Enter hotkeys for {accion}"
    MSG_ERROR = f"Repeat; hotkeys {convert_keylist2str(screenshot)} CANNOT be contained in the current combination."

    response = False
    while response != True:
        # Wait for imput
        time.sleep(0.3)

        # Get keys:
        click.echo(MSG)
        keys = get_keys_from_user()

        # Chequeo de teclas:
        condition_a = set(screenshot).issubset(set(keys))

        if condition_a:
            click.echo(MSG_ERROR)
        else:
            response = yn_request()

    return keys


def request_input_wi(accion, screenshot, check_keys={None}):

    MSG = f"Enter hotkeys for {accion}"
    MSG_ERROR_0 = f"Repeat; cannot set {convert_keylist2str(screenshot)} as unique key, provide a combination."
    MSG_ERROR_A = f"Repeat; the key combination {convert_keylist2str(screenshot)} MUST CONTAIN the actual combination."
    MSG_ERROR_B = f"Repeat; the key combination {convert_keylist2str(check_keys)} CANNOT CONTAIN the actual combination."

    response = False
    while response != True:
        # Wait for imput
        time.sleep(0.3)

        # Get keys:
        click.echo(MSG)
        keys = get_keys_from_user()

        # Chequeo de teclas:
        condition_0 = screenshot == keys
        condition_a = not set(screenshot).issubset(set(keys))
        condition_b = any([set(keys).issubset(set(check_keys)), set(check_keys).issubset(set(keys))]) if check_keys !=None else False

        if condition_0:
            click.echo(MSG_ERROR_0)
        elif condition_a:
            click.echo(MSG_ERROR_A)
        elif condition_b:
            click.echo(MSG_ERROR_B)
        else:
            response = yn_request()

    return keys
