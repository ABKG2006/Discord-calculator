import os
import random
import discord 
from discord.ext import commands
from logic import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='//', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def calc(ctx, a):
    await ctx.send(calculate(a))
@bot.command()
async def oplist(ctx):
    await ctx.send("Avaliable opperations:\nAdddition(x+y)\nSubtraction(x-y)\nMultiplication(x*y)\nDivision(x/y)\nInteger division(x//y)\nModulo(x%y)\nExponantiation(x**y or x^y)\nSquare root(sqrt(x))\n\n***Note: All trig functions use radians***\n\nconvert from degrees ( x deg )\nsine( sin(x) )\ncosine( cos(x) )\ntangent( tan(x) )\ncotangent( cot(x) )\nsecant( sec(x) )\ncosecant( cosec(x) )\n\nConstants:\npi=3.141...\ne=2.718...\ni=sqrt(-1)",ephemeral=True)
@bot.command()
async def mem(ctx):
    try:
        image=random.choice(os.listdir('images'))
        with open(f'images/{image}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except:
        await ctx.send("Unable to get memes at the moment,sorry")    
@bot.command()
async def fox(ctx):
    image_url = get_foxxo()
    await ctx.send(image_url)
bot.run("token go here")

