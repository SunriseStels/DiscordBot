import discord
from discord.ext import commands
import youtube_dl
import safygiphy
import requests
import io
import random

songs = {"https://www.youtube.com/watch?v=N5rus7Dhpzs", "https://www.youtube.com/watch?v=XtsmIy1njjM"}

g = safygiphy.Giphy()
Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.content == '!music':
        channel = message.author.voice.voice_channel
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player("https://www.youtube.com/watch?v=N5rus7Dhpzs")
        player.start()

    if message.content.startswith('!help'):
        await client.send_message(message.channel, "```!gif название гифки - позволяет загурзить рандомную гиф в чат из сервиса Giphy```")

    if message.content.startswith('!gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

client.run("token")