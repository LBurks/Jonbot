import os
from random import choice

import discord 
from discord.ext import commands

from dotenv import load_dotenv


def startup():
    txt = [l[:-1] for l in open('./random.txt')]
    return txt

txt = startup()

bot = commands.Bot(command_prefix='.')

@bot.command(help='Give a perfectly valid explanation for why you just lost.')
async def john(ctx):
    await ctx.send(choice(txt))

load_dotenv()
token = os.getenv('TOKEN')

bot.run(token)


