#! /usr/bin/python

import pediscord as discord
import getpass
import os
import asyncio
import time
import json
import socket
from  system.soket_handler import data_socket

host = 'localhost'
port = 9527
loop = asyncio.get_event_loop()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(False)
s.bind((host, port))
s.listen(10)



# pediscord client initialization
client = discord.Client(loop=loop)


scdt = data_socket(loop)

# pediscord client initialization

# Retrieve token
token = ''
if os.path.exists('token.txt'):
    with open('token.txt', 'r') as token_file:
        token = token_file.read().rstrip()
else:
    token = getpass.getpass('Enter your token: ')
    with open('token.txt', 'w') as tokenfile:
        tokenfile.write(token)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_error(err):
    print(err)

print(client.is_ready())
loop.create_task(scdt.server(s))
#loop.create_task(test_read())
client.run(token, bot=False)











#@client.event
# async def on_ready():
#     startup = ('Logged as ' + str(client.user.name) + '#' + str(client.user.discriminator) + '(' + str(client.user.id) + ')')
#     print("=" * len(startup))
#     print(startup)
#     print("=" * len(startup))
#     guilds_json = []
#     for guild in client.guilds:
#         guild_list.append({"name":guild.name, "id":guild.id, "icon":guild.icon, "description":guild.description, "larfe_guild":guild.large})
#         guild_channels = []
#         for channel in guild.text_channels:
#             guild_channels.append({
#                 "name":channel.name, "id":channel.id,
#                 "topic":channel.topic, "slowmode_delay":channel.slowmode_delay,
#                 "nsfw":channel.nsfw(), "news":channel.is_news(),
#                 "members":channel.members, "type":channel.type,
#                 "category":channel.category, "pos":channel.position
#             })
#         for channel in guild.voice_channels:
#             guild_channels.append({
#                 "name":channel.name, "id":channel.id,
#                 "user_limit":channel.user_limit, "members":channel.members,
#                 "type":channel.type, "category":channel.category,
#                 "pos":channel.position
#             })
#         for category in guild.categories:
#             guild_channels.append({
#                 "name":category.name, "id":channel.id,
#                 "nsfw":category.nsfw(),
#                 "txt_ch":category.text_channels, "voice_ch":category.voice_channels,
#                 "type":category.type, "pos":category.position
#             })
#         guild_list[len(guild_list) - 1]["channels"] = guild_channels
#     guilds_json = json.dumps(guilds_json)