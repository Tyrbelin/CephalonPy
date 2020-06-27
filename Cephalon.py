import discord
import os
import urllib.request
import json

client = discord.Client()

@client.event
async def on_ready():
    print ("봇 시작")

@client.event
async def on_message(message):
    if message.content.startswith("!시터스"):
        req = urllib.request.Request('https://api.warframestat.us/pc/cetusCycle', headers={'User-Agent': 'Mozilla/5.0'})
        text_data = urllib.request.urlopen(req).read()
        json_data = json.loads(text_data)
        await message.channel.send(message.channel, json_data.get("shortString").replace("Day","낮").replace("Night","밤").replace("h","시간").replace("m","분").replace("s","초").replace("to","후"))

token = os.environ["BOT_TOKEN"]
client.run(token)
