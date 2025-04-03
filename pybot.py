import discord, random
from discord.ext import commands
from tokin import token
from time import sleep as wait
from bot_logic import *
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)
siono = ["si", "no"]
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def lawawatronix(ctx, amount = 1):
    await ctx.send("O:")
    wait(1)
    for i in range(amount):
        await ctx.send(" la wawa ")
@bot.command()
async def help(ctx):
    await ctx.send("MIS [FUNCIONES] EPICAS:")
    await ctx.send("$lawawatronix N: ")

bot.run(token)