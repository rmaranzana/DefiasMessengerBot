import discord, os
import click


class DiscordBot:

    def __init__(self, channel_id, username, path):
        # Client:
        self.client = discord.Client()
        self.channel_id = channel_id
        self.username = username
        self.path = path

        # Discord events:
        self.define_discord_events()

    def send_file(self, new_photo):
        # Send file:
        channel = self.client.get_channel(self.channel_id)
        file = discord.File(open(os.path.join(self.path, new_photo), 'rb'), filename=new_photo)
        self.client.loop.create_task(channel.send(f'New pic from {self.username}!', file=file))

    def define_discord_events(self):
        
        @self.client.event
        async def on_ready():
            MSG = f'DefiasMessengerBot logged as {self.client.user}'

            click.echo()
            click.echo(MSG)