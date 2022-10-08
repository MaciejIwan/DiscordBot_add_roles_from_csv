# This example requires the 'message_content' intent.

import discord
from src.CSV import CSV

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$install'):
        await message.channel.send('wczytaj liste studentów z CSV!')

        students: CSV = CSV("../lista.csv")
        students.load_data_from_file()
        for row in students.data:
            try:
                # check if role exists

                wanted_role_name = row[0]
                wanted_user_id = row[4]

                roles = await message.guild.fetch_roles()
                if not wanted_role_name in set(p.name for p in roles):
                    role = await message.guild.create_role(name=wanted_role_name, colour=discord.Colour(0xffffff))
                else:
                    role = next(filter(lambda x: x.name == wanted_role_name, roles))

                user: discord.Member = await message.guild.fetch_member(wanted_user_id)
                await user.add_roles(role)
            except Exception as e:
                print(e)
            finally:
                continue
        await message.channel.send('robota skonczona, grupy rodzielone')


client.run('')
