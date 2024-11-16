import discord
from discord.ext import commands
permisos = discord.Intents.default()
permisos.message_content =  True
alex= commands.Bot(command_prefix="alex ",intents=permisos)
@alex.event
async def on_ready():
    print ("iniciado")
@alex.command()
async def hola(ctx):
    await ctx.send("hola viendenido como estas alex")
@alex.command()
async def meme1(ctx):
    imagen = open("prueba\imagenes\m1.jpeg","rb")
    await ctx.send(file=discord.File(imagen,"meme.jpeg"))
    imagen.close()
@alex.command()
async def meme2(ctx):
    imagen = open("prueba\imagenes\m2.jpeg","rb")
    await ctx.send(file=discord.File(imagen,"meme.jpeg"))
    imagen.close()
@alex.command()
async def meme3(ctx):
    imagen = open("prueba\imagenes\m3.jpeg","rb")
    await ctx.send(file=discord.File(imagen,"meme.jpeg"))
    imagen.close()
    
alex.run("")
