import random

import discord
from discord.ext import commands

screeches = ["AAAAAAAA", "OH NO OH NO", "HHOOOOAAAOAOAA", "EEEEEEEEAA", "YAAAAARGH", "OH GOSH OH GEEZ OH MAN", "OH FRICK OH HECK", "AAAA", "AAAAAAAAAAAAA", "[nonsensical shrieking]", "[high-pitched yelling]", "[upset walrus noise]", "[wilhelm scream]", "SCREEEEEEEE", "OH MAN OOOOOH MAAAAAN", "SNAKE? SNAAAAAKE!?", "YOOOOAAA", "[shrill ululation]", "YEEEEEEEBRBRBBRBRBRB"]
most_recent_screech = "AAAAAAAA"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        # Here, we tell Python we want to use a variable outside this function--this has to do with "scope", a more advanced topic.
        # Basically, we're just telling Python "hey, you see that thing on line 8? Write to it instead of making your own that only exists in on_message!"
        global most_recent_screech
        if random.randint(1,10)==9:
            chosen_screech = random.choice(screeches)
            while chosen_screech == most_recent_screech:
                chosen_screech = random.choice(screeches)
            most_recent_screech = chosen_screech
            await message.channel.send("***{}***".format(chosen_screech))
        await bot.process_commands(message)


# Becky Haluska
# Tip: So we need to create a random number and return it--and we already programmed the bot to scream with a 1:10 chance!
@bot.command(name="roll")
async def roll(ctx, number_to_roll=20):
    await ctx.send("You called 'roll' to roll {}".format(number_to_roll))


@bot.command(name="mock")
async def mock(ctx, *words):
    # A special bit of Python--this will get all the words following !mock as a single sentence!
    original_message = ' '.join(words)
    mock_message = []
    # We go through every character in that sentence and randomly capitalize or lower each
    for character in original_message:
        if random.randint(1,10)>6:
            mock_message.append(character.upper())
        else:
            mock_message.append(character.lower())
    # Then we join them all together in a new sentence
    await ctx.send(''.join(mock_message))



# Autumn: A bot that tries to get people to respond to 'oh, did you hear what joe did the other day' and 'I am just really in to updogg' in humerous (spelling is hard) ways by sending out either of those messages (or messages similar to it) and then sending another message ('I dunno dogg, what's up with you').
# Tip: The bot's original "test functionality", where it screamed every time a message was sent, required it to look at every message (see line 12)
@bot.command(name="troll")
async def troll(ctx, message="whos joe"):

    await ctx.send("Looks like you're going to the Shadow Realm, Jimbo.")



#Gina: Since it's just going to be for me, I really like formula one and maybe what I can do is Enter a drivers name and the software changes it to the team in which they drive for or maybe a picture of the driver
# Tip: The easiest way to implement this would be to store the driver's name, then the thing that should be sent when the name is said. Similar to the choose-your-own-adventure...
@bot.command(name="driver")
async def driver(ctx, driver=20):

    await ctx.send("You called 'a driver in formula one")

# Willis: when certain Star Wars phrases/words are entered, a "Yoda" picture is displayed
# Tip: The "mock" command shows how to get an entire phrase instead of just one word
@bot.command(name="yoda")
async def yoda(ctx, yodaPic=1):

    await ctx.send("Yoda picture to be displayed!")

# Prisha: I think it would be cool if the bot had riddles and then you could ask it to tell you a riddle. It would ask the question, and then you can try to guess the answer. If you can't guess the answer you could say something like "no answer" and then the bot will give you the answer. If you have an answer you could say something like "the answer is: answer" and then it could say correct or wrong
# Tip: There'll be a few moving parts here: one, you'll need a list of riddles and some way to choose from them. Two, you'll need a way to submit an answer, and three, a way to check the answer against the most recent riddle. What might that look like?
# Saving the most recent riddle between calls might be tricky; a slightly awkward (but readable!) way to do this is shown on line 18.
@bot.command(name="riddle")
async def riddle(ctx, message = "I request a riddle"):

    await ctx.send("I see you have called for a riddle")

# Clarissa: bot where if someone types your name in the chat, the bot could @you or something, i often miss my friend's conversations sometimes in discord so this could be helpful if they don't directly @me
# Tip: Line 12 might help this one out, too!
@bot.command(name="clynae")
async def call(ctx, n="clarissa"):

    await ctx.send("Calling ' n!'")

#Larisa: When someone put "", a funny imagen of the player appers
# Tip: In this case, finding a good image might be the tricky part! If it's the same image each time the command is used, maybe you could store it at the top of the file, so you could always change it easily?
# Take a look how "screeches" on line 6 is used!
@bot.command(name="x")
async def xroll(ctx, x=20):

    await ctx.send("Oh,nooo!")

with open("secret.txt","r") as secret_file:
    bot.run(secret_file.readline()[:-1])
