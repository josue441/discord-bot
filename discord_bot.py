import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '$' , intents=intents)
token = 'TOKEN' #token

@bot.event
async def on_ready():
    channel = bot.get_channel(1258921236688404533)
    if channel:
        await channel.send("El bot está en línea. Para la ayuda escriba $ayuda")

@bot.command(name='gen_password')
async def password(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(15)}")

@bot.command(name='sumar')
async def sumar(ctx,a,b):
    response = int(a) + int(b)
    await ctx.send(f"la suma de {a} + {b} es: {response}")

@bot.command(name='ayuda')
async def ayuda(ctx):
    await ctx.send("comandos actuales son: $gen_password, $sumar, $repetir y $ayuda")

bot.run(token)
