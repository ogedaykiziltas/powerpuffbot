import discord
from discord.ext import commands
import random
import asyncio
import os
if not discord.opus.is_loaded():
    discord.opus.load_opus("opus")

startup_extensions = ["Music"]

TOKEN = "NTExNTU4MTM4ODkwMjg5MTc4.Ds3FoA.5hONJtRuSmcVvtqahfoFzvdH8_Q"
client = commands.Bot(command_prefix = "_")



@client.event
async def on_ready() :
    print("BOT ÇALIŞIYOR")
    await client.change_presence(game = discord.Game(name='Şeker, Baharat ve İyi Olan Her Şey'))

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = " {}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()






@client.command(pass_context = True)
async def sa(ctx) :
    await client.say("as mardeşim!")

@client.command(pass_context=True)
async def sil(ctx, number):
    abc= []
    number = int(number)
    async for x in client.logs_from(ctx.message.channel, limit=number):
        abc.append(x)
    await client.delete_messages(abc)




client.run(TOKEN)
