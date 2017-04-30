import discord
from discord.ext.commands import Bot
from os import environ
import logging

try:
    bot_token = environ['DISCORD_BOT_TOKEN']
except KeyError:
    logging.error('DISCORD_BOT_TOKEN environment variable not set.')
    quit()

bot = Bot(command_prefix='!')

