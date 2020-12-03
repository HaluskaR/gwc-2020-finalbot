import random

import discord
from discord.ext import commands

screeches = ["AAAAAAAA", "OH NO OH NO", "HHOOOOAAAOAOAA", "EEEEEEEEAA", "YAAAAARGH", "OH GOSH OH GEEZ OH MAN", "OH FRICK OH HECK", "AAAA", "AAAAAAAAAAAAA", "[nonsensical shrieking]", "[high-pitched yelling]", "[upset walrus noise]", "[wilhelm scream]", "SCREEEEEEEE", "OH MAN OOOOOH MAAAAAN", "SNAKE? SNAAAAAKE!?", "YOOOOAAA", "[shrill ululation]", "YEEEEEEEBRBRBBRBRBRB"]

bot = commands.Bot(command_prefix='!')

#@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        await message.channel.send("***{}***".format(random.choice(screeches)))


# Becky Haluska
@bot.command(name="roll")
async def roll(ctx, number_to_roll=20):
    await ctx.send("You called 'roll' to roll {}".format(number_to_roll))
    
    

# Becky: I'd like to make a dice-rolling feature for the bot. It'd take a number and produce a random number between 1 and the number selected, and "roll" 20 if no number is provided.

# Autumn: A bot that tries to get people to respond to 'oh, did you hear what joe did the other day' and 'I am just really in to updogg' in humerous (spelling is hard) ways by sending out either of those messages (or messages similar to it) and then sending another message ('I dunno dogg, what's up with you').
@bot.command(name="troll")
async def troll(ctx, message="whos joe"):
 
    await ctx.send("Looks like you're going to the Shadow Realm, Jimbo.")
    


#Gina: Since it's just going to be for me, I really like formula one and maybe what I can do is Enter a drivers name and the software changes it to the team in which they drive for or maybe a picture of the driver 
@bot.command(name="driver")
async def driver(ctx, driver=20):
 
    await ctx.send("You called 'a driver in formula one")

# Willis: when certain Star Wars phrases/words are entered, a "Yoda" picture is displayed
@bot.command(name="yoda")
async def yoda(ctx, yodaPic=1):
 
    await ctx.send("Yoda picture to be displayed!")

# Prisha: I think it would be cool if the bot had riddles and then you could ask it to tell you a riddle. It would ask the question, and then you can try to guess the answer. If you can't guess the answer you could say something like "no answer" and then the bot will give you the answer. If you have an answer you could say something like "the answer is: answer" and then it could say correct or wrong
@bot.command(name="riddle")
async def riddle(ctx, message = "I request a riddle"):
 
    await ctx.send("I see you have called for a riddle")

# Clarissa: bot where if someone types your name in the chat, the bot could @you or something, i often miss my friend's conversations sometimes in discord so this could be helpful if they don't directly @me
@bot.command(name="clynae")
async def call(ctx, n="clarissa"):

    await ctx.send("Calling ' n!'")

#Larisa: When someone put "", a funny imagen of the player appers
@bot.command(name="x")
async def xroll(ctx, x=20):
 
    await ctx.send("Oh,nooo!")

with open("secret.txt","r") as secret_file:
    bot.run(secret_file.readline()[:-1])
