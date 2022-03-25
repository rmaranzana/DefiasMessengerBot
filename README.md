# DefiasMessengerBot
## Description
DefiasMessengerBot is a Python module for World of Warcraft that let you post your in-game screenshots on a Discord Channel.
Furthermore, this module is able to take screenshots with or without the user interface printed on the image. 

## Requirements
Python >= 3.8
World of Warcraft Classic or The Burning Crusade Classic.
A Discord Bot with read/post and channel visualization permissions.

## Configuration steps
1) Download the [latest release of DefiasMessengerBot](https://github.com/rmaranzana/DefiasMessengerBot/releases/latest).
2) Open a command prompt and do a pip install of the .whl file.
3) Configure the DefiasMessengerBot running the command:
```shell script
python -m defiasmessengerbot.config`
```
And follow the instructions.
4) Add two environment variables:
```shell script
export DEFIASMESSENGERBOT_CHANNELID=<Discord Channel ID>
export DEFIASMESSENGERBOT_TOKEN=<Discord Bot Token>
```
Replace <Discord Channel ID> with the Channel ID to which your Bot will post, and the <Discord Bot Token> with the key from the Discord Developer Portal.

## Testing
Run the following line on a command prompt:
```shell script
python -m defiasmessengerbot.test
```
You will be able to test both screenshot hotkeys.

## Execution
Run the following command:
```shell script
python -m defiasmessengerbot.run
```

If everything has been set up properly, the DefiasMessengerBot should now be able to connect to your Discord Bot.

Finally, use the same hotkeys to take and share your screenshots with your friends!
