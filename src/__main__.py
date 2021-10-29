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

@bot.command(help='Explain why you\'re better than your opponent')
async def outplayed(ctx, char: str = None):
    character = char.capitalize()
    if character not in roster: character = choice(roster)
    await ctx.send(f"In a game like smash, {character} has to work 10x harder than your average smash character because of his kit. He may seem unfair when fighting him but believe me when I say you're definitely being outplayed especially at high/top level. He's 100% honest as crazy as that sounds.")

bot.run(token)


