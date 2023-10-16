import os
import random
import discord 
from discord.ext import commands
from logic import *
count=0
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='//', intents=intents)


@bot.event
async def on_ready():
    print('hello world')


@bot.command()
async def calc(ctx, a):
    await ctx.send(calculate(a))
@bot.command()
async def oplist(ctx):
    await ctx.send("Avaliable opperations:\nAdddition(x+y)\nSubtraction(x-y)\nMultiplication(x*y)\nDivision(x/y)\nInteger division(x//y)\nModulo(x%y)\nExponantiation(x**y or x^y)\nSquare root(sqrt(x))\n\n***Note: All trig functions use radians***\n\nconvert from degrees ( x deg )\nsine( sin(x) )\ncosine( cos(x) )\ntangent( tan(x) )\ncotangent( cot(x) )\nsecant( sec(x) )\ncosecant( cosec(x) )\n\nConstants:\npi=3.141...\ne=2.718...\ni=sqrt(-1)",ephemeral=True)
@bot.command()
async def mem(ctx):
    try:
        randomFileSelectArray = random.choices(os.listdir('images') , weights=(10,40,20,20,20) , k=1)
        
        image=random.choice(randomFileSelectArray)
        with open(f'images/{image}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        
    except:
        await ctx.send("Unable to get memes at the moment,sorry")    
@bot.command()
async def fox(ctx):
    image = get_foxxo()
    channel = bot.get_channel(a)#replace a with the channel id of the channel you want to send the images to leave as is to send to the channel the command was sent from
    try:
        await channel.send(image)
    except:
        await ctx.send(image)
@bot.command()
async def incrementor(ctx, a):
    try:
        a=int(a)
        a+=1
        await ctx.send(a)
    except:
        await ctx.send("Invalid input")
@bot.command()
async def decrementor(ctx, a):
    try:
        a=int(a)
        a-=1
        await ctx.send(a)
    except:
        await ctx.send("Invalid input")
bot.run("Token goes here")

