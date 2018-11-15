import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
 bot = discord.Client()
bot_prefix = "_"
bot = commands.Bot(command_prefix = bot_prefix)
 @bot.event
async def on_ready() :
    print("BOT ÇALIŞIYOR")
    await bot.change_presence(game = discord.Game(name='Şeker, Baharat ve İyi Olan Her Şey'))
 @bot.command(pass_context = True)
async def sa(ctx) :
    await bot.say("as mardeşim!")
 @bot.command(pass_context=True)
async def davet(ctx, member:discord.Member) :
    urll = ["" , "" , ""]
    embed = discord.Embed(title=ctx.message.author.name + " ,sizi oyuna davet ediyor" + member.name)
    embed.set_image(url=random.choice(urll))
    await bot.say(embed=embed)
 @bot.command(pass_context=True)
async def sil(ctx, number):
    abc= []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit=number):
        abc.append(x)
    await bot.delete_messages(abc)
 @bot.command(pass_context=True)
async def s(ctx):
    abc=ctx.message.content.split("1")
    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.channel , abc)
 bot.run("NTExNTU4MTM4ODkwMjg5MTc4.DsyIxw.27jqZg4iPWreKPJ_UzJbTkYIbwk")
