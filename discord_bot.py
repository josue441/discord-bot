import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '$' , intents=intents)
token = 'TOKEN' #token

@bot.event
async def on_ready():
    channel = bot.get_channel(ID CHANNEL) #id del canal donde el bot escribira "El bot está en línea." 
    if channel:
        await channel.send("El bot está en línea.")

#generador de contraseñas simple
@bot.command(name='gen_password')
async def gen_password(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(15)}")

#calculadora que solo suma ejemplo: $suma 10 10 el bot dira: la suma de 10 + 10 es: 20
@bot.command(name='sumar')
async def sumar(ctx,a,b):
    response = int(a) + int(b)
    await ctx.send(f"la suma de {a} + {b} es: {response}")

bot.run(token)
