import discord, os, random
from discord.ext import commands
from bot_logic import gen_pass, imagenes_de_perros, get_duck, videos_choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '$' , intents=intents)
token = 'TOKEN_AQUI' #token

@bot.event
async def on_ready():
    channel = bot.get_channel(ID_DEL_CANAL)
    if channel:
        await channel.send("El bot está en línea.")

#comandos
@bot.command(name='gen_password')
async def password(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(15)}")
@bot.command(name='sumar')

async def sumar(ctx,a,b):
    response = int(a) + int(b)
    await ctx.send(f"la suma de {a} + {b} es: {response}")

#commando que busca los memes de la carpeta "memes" y selecciona de forma aleatoria y los envia
@bot.command(name = "momos")
async def memes(ctx):
    img_mem = random.choice(os.listdir("img/memes"))
    with open(f"img/memes/{img_mem}","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

#imagenes de perros aleatorios gracias a una api
@bot.command(name="perros")
async def duck(ctx):
    image_url = imagenes_de_perros()
    await ctx.send(f"imagenes de perros: {image_url}")

#comando que envia imagenes de animales.
#Las imagenes son de la carpeta llamada "animales" y se seleccionan de manera aleatoria
@bot.command(name="animales")
async def animales(ctx):
    img_animales = random.choice(os.listdir("img/meme/animales"))
    with open(f"img/animales/{img_animales}","rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command(name = "patos")
async def duck(ctx):
    img = get_duck()
    await ctx.send(f"imagenes de patos: {img}")

@bot.command(name='contaminacion_auditiva')
async def videos_de_contaminacion(ctx):
    video = videos_choice()
    await ctx.send(f"aqui hay unos videos que hablan sobre la contaminacion auditiva: {video}")

bot.run(token)
