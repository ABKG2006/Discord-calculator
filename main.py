
import discord 
from discord.ext import commands
from logic import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def calc(ctx, a):
    await ctx.send(calculate(a))
@bot.command()
async def oplist(ctx):
    await ctx.send("Avaliable opperations:\nAdddition(x+y)\nSubtraction(x-y)\nMultiplication(x*y)\nDivision(x/y)\nInteger division(x//y)\nModulo(x%y)\nExponantiation(x**y or x^y)\n\n***Note: All trig functions use radians***\n\nconvert from degrees ( x deg )\nsine( sin(x) )\ncosine( cos(x) )\ntangent( tan(x) )\ncotangent( cot(x) )\nsecant( sec(x) )\ncosecant( cosec(x) )\n\nConstants:\npi=3.141...\ne=2.718...",ephemeral=True)
bot.run("TOKEN buraya/here")