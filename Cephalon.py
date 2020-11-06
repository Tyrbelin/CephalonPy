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
    if message.content.startswith("!몬스터"):
        monster_name = message.content.split(' ')[1]
        req = urllib.request.Request('http://mhw.gamedb.kr/apis/monsters/'+monster_name, headers={'User-Agent': 'Mozilla/5.0'})
        text_data = urllib.request.urlopen(req).read()
        json_data = json.loads(text_data)
        await client.send_message(message.channel, json_data)

token = os.environ["BOT_TOKEN"]
client.run(token)
