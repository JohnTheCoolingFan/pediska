#! /usr/bin/python
import asyncio
import pediscord as discord
import getpass
import os
from  system.soket_handler import data_socket


# pediscord client initialization


loop = asyncio.get_event_loop()
client = discord.Client(loop=loop)
scdt = data_socket(loop)


# pediscord client initialization

# Retrieve token
# TODO в другое место может это переложить?
# Это будет потом в другом месте и вообще по-другому работать. Временное решение.
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

@client.event
async def on_message(message):
    print("discord mes", message.content)
    await scdt.send(message.content)

if __name__ == "__main__":
    scdt.set_socket("localhost", 8888)
    loop.create_task(scdt.start_socket_handler())
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
