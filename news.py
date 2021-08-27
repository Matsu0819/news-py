import discord
import requests
import sys
sys.path.append("lib.bs4")
from bs4 import BeautifulSoup
import re


token='KEY'

client = discord.Client()

url = "https://www.yahoo.co.jp/"

@client.event
async def on_message(message):

    game = discord.Game("/news")
    await client.change_presence(status=discord.Status.online, activity=game)

    if message.content.startswith("/news"):
        await message.channel.send("https://news.yahoo.co.jp/")
        r = requests.get(url)
        a = BeautifulSoup(r.text, 'html.parser')
        b = a.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
        for e in b:
            await message.channel.send(e.getText())


    else:
        pass

client.run(token)
