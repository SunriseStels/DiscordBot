import discord
from discord.ext import commands
import json
import safygiphy
import requests
import io
import random

# with open('D:/PythonProjects/MyBotProject/music.json', 'r', encoding='utf-8') as responce:
#     source = responce.read()
#
# data = json.load(source)

songs = ["https://www.youtube.com/watch?v=N5rus7Dhpzs", "https://www.youtube.com/watch?v=XtsmIy1njjM"]
words = [":yum:",":relaxed:",":relieved:",":nerd:",":sunglasses:",":smirk:"]

players = {}

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

    #---------------Музыкальная часть---------------

    if message.content == '!music':
        channel = message.author.voice.voice_channel
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player(random.choice(songs))
        players[message.server.id] = player
        player.start()

    if message.content == '!stop':
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "На данный момент я подключена.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Error: ```{haus}```".format(haus=Hugo))

    if message.content == '!pause':
        try:
            players[message.server.id].pause()
        except:
            pass

    if message.content == '!resume':
        try:
            players[message.server.id].resume()
        except:
            pass

    # ---------------Музыкальная часть окончена---------------

    if message.content.startswith('при') | message.content.startswith('При'):
        userName = message.author.name
        await client.send_message(message.channel, 'Доброго времени суток ' + userName + " " + random.choice(words))

    if message.content.startswith('!help'):
        await client.send_message(message.channel,
                                  "```!gif название гифки - позволяет загурзить рандомную гиф в чат из сервиса Giphy\n"
                                  "!music - позволяет воспроизвести рандомную композицию\n"
                                  "!pause - позволяет приостановть воспроизведённую композицию\n"
                                  "!resume - позволяет продолжить прослущивание приостановленной композиции\n"
                                  "!stop - пот покинет голосовой чат```\n"
                                  )

    if message.content.startswith('!gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

client.run("token")