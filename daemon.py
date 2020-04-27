#! /usr/bin/python

import pediscord
import getpass
import os

client = pediscord.Client()

token = ''
if os.path.exists('token.txt'):
    with open('token.txt', 'r') as token_file:
        token = token_file.read().rstrip()
else:
    token = getpass.getpass('Enter your token: ')
    with open('token.txt', 'w') as tokenfile:
        tokenfile.write(token)

client.run(token, bot=False)

print('This is daemon')
