import random

import discord
from discord.ext import commands

screeches = ["AAAAAAAA", "OH NO OH NO", "HHOOOOAAAOAOAA", "EEEEEEEEAA", "YAAAAARGH", "OH GOSH OH GEEZ OH MAN", "OH FRICK OH HECK", "AAAA", "AAAAAAAAAAAAA", "[nonsensical shrieking]", "[high-pitched yelling]", "[upset walrus noise]", "[wilhelm scream]", "SCREEEEEEEE", "OH MAN OOOOOH MAAAAAN", "SNAKE? SNAAAAAKE!?", "YOOOOAAA", "[shrill ululation]", "YEEEEEEEBRBRBBRBRBRB"]

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        await message.channel.send("***{}***".format(random.choice(screeches)))

with open("secret.txt","r") as secret_file:
    bot.run(secret_file.readline()[:-1])
