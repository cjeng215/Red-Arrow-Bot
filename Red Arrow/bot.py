import os
import discord
import platform
import traceback
from time import gmtime, strftime
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord import Intents

# load secrets
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
PREFIX = os.getenv('PREFIX')

client = Bot(command_prefix=PREFIX, intents=Intents().all(), help_command=None)

initial_extensions = (
    'cogs.Giphy',
    'cogs.Ping',
    'cogs.MemberEvents',
    'cogs.Misc',
    'cogs.BotVoice',
)

log_time_format = 'Time: ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime())


@client.event
async def on_ready():
    # Reference: https://discordpy.readthedocs.io/en/latest/api.html#client
    print(f'We have logged in as {client.user}')
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')
    print('-----------------------------')


@client.event
async def on_message(message):
    # prevents conversation capture to itself -- recursion
    if message.author == client.user:
        return

    # logging message
    with open('log.txt', 'a') as f:
        f.write(f'{log_time_format}, From: {message.author}, Message: {message.content}\n')

    await client.process_commands(message)


# load cogs into bot
for extension in initial_extensions:
    try:
        client.load_extension(extension)
    except Exception as e:
        print(f'Failed to load extension: {extension}.')
        traceback.print_exc()

client.run(DISCORD_BOT_TOKEN)
