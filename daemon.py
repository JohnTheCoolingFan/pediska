#! /usr/bin/python

import pediscord as discord
import getpass
import os
import asyncio
from system.soket_handler import data_socket

loop = asyncio.get_event_loop()
client = discord.Client(loop=loop)

sokt = data_socket(1234)

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
async def on_message(message: discord.Message):
    await sokt.send(message.content)
    print(message.content)
    data = await asyncio.wait_for(sokt.recv())
    print(data)
if __name__ == '__main__':
    client.run(token, bot=False)

