import discord
import random

TOKEN = 'OTc5NDA2OTkwNjc1NzA1ODg2.Gp8SkG.ePrcoP-SjxN5e75kX-J_WA9cWSxUCFckNwX7V0'

client = discord.Client()



@client.event

async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    

    if message.channel.name == '💬-general-chat':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif username.lower() == 'bye':
            await message.channel.send(f'see you later {username}!')
            return







client.run(TOKEN)
