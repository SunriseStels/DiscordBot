import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json
import random

with open('D:/PythonProjects/Tarkov/base.json', 'r', encoding='utf-8') as response:
    source = response.read()

data = json.loads(source)

words = [":yum:",":relaxed:",":relieved:",":nerd:",":sunglasses:",":smirk:"]

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.startswith('при') | message.content.startswith('При'):
        userName = message.author.name
        await client.send_message(message.channel, "Привет " + userName + " " + random.choice(words))

    if message.content == ('!help'):
        await client.send_message(message.channel, "```some test help text here```")


client.run("token")