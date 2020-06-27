import asyncio, discord
import os
import urllib.request
import json
from discord.ext import commands

token = os.environ["BOT_TOKEN"]
game = discord.Game("")
bot = commands.Bot(command_prefix='!',status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
    print ("봇 시작")

@bot.command()
async def 명령어(ctx):
    await ctx.send("도움말")

@bot.command()
async def 시터스(ctx):
    req = urllib.request.Request('https://api.warframestat.us/pc/cetusCycle', headers={'User-Agent': 'Mozilla/5.0'})
    text_data = urllib.request.urlopen(req).read()
    json_data = json.loads(text_data)
    await ctx.send(json_data.get("shortString").replace("Day","낮").replace("Night","밤").replace("h","시간").replace("m","분").replace("s","초").replace("to","후"))

bot.run(token)
