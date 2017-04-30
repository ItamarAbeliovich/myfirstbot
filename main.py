import discord
from discord.ext.commands import Bot
from os import environ
import logging
import logutil

logger = logutil.get_logger(__name__, 'log.txt')

try:
    bot_token = environ['DISCORD_BOT_TOKEN']
except KeyError:
    logger.critical('DISCORD_BOT_TOKEN environment variable not set.')
    quit()

bot = Bot(command_prefix='!')


@bot.event
async def on_read():
    logger.info('Client logged in!')


@bot.command()
async def hello(*args):
    return await bot.say('Hello world!')


@bot.command()
async def echo(*args):
    if not len(args):
        return await bot.say('Usage: `!echo <message>`')
    return await bot.say(args[0])

bot.run(bot_token)