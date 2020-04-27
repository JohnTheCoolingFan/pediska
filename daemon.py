#! /usr/bin/python

import pediscord
import getpass
import os
import asyncio

# ...
class NewMessageServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        print('Received data: {}'.format(data.decode()))
        self.transport.write(data)

loop = asyncio.get_event_loop()
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

# pediscord client initialization
client = pediscord.Client(loop=loop)

# Try to send new messages to client (kinda)
@client.event
async def on_message(message: pediscord.Message):
    print(message.content)

client.run(token, bot=False)
