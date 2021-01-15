import sys
import traceback

from discord.ext import commands


class MusicBot(commands.Bot):
    initial_extensions = ['cogs.playcommand']

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await self.process_commands(message)
         



######################################################

client = MusicBot(command_prefix=commands.when_mentioned_or('+'))

if __name__ == '__main__':
    for extension in client.initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

client.run('Nzk5NDYwMjY3MjYzOTE4MDkx.YAD5ZA.nVp51fkNwI_G2DwLbg63RT9dhHw')
