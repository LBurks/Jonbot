import os
from random import choice

import discord 
from discord.ext import commands

from dotenv import load_dotenv

from roster import roster


def startup():
    txt = [l[:-1] for l in open('./random.txt')]
    return txt

txt = startup()

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix=os.getenv('PREFIX'))

@bot.command(help='Give a perfectly valid explanation for why you just lost.')
async def john(ctx, test: int = 0):
    if os.getenv('ENV') == 'dev': response = txt[test]
    else: response = choice(txt)
    await ctx.send(response)

@bot.command(help='Lists legal stages')
async def stagelist(ctx):
    await ctx.send("""Starters: PS2, FD, Battlefield, TnC, Smashville\nCounters: Kalos, Small Battlefield\n7 minute timers, 2 bans, Players cannot pick last won stage, and counterpicked stage. (mDSR)""")

bot.run(token)


