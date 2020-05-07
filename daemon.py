#! /usr/bin/python

import pediscord as discord
import getpass
import os
import asyncio
import time
import json

loop = asyncio.get_event_loop()

# pediscord client initialization
client = discord.Client(loop=loop)

class NewMessageServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        print('Received data: {}'.format(data.decode()))
        self.transport.write(data)

coro = loop.create_server(NewMessageServer, '127.0.0.1', 40404)
server = loop.run_until_complete(coro)
print('Started on {}'.format(server.sockets[0].getsockname()))

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
    startup = ('Logged as ' + str(client.user.name) + '#' + str(client.user.discriminator) + '(' + str(client.user.id) + ')')
    print("=" * len(startup))
    print(startup)
    print("=" * len(startup))
    guilds_json = []
    for guild in client.guilds:
        guild_list.append({"name":guild.name, "id":guild.id, "icon":guild.icon, "description":guild.description})
    guilds_json = json.dumps(guilds_json)

@client.event
async def on_message(message: discord.Message):
    print(server.sockets)
    server.sockets[0].send(message.content.encode())
    pass

client.run(token, bot=False)
