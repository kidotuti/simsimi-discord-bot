import asyncio
import discord
from discord.ext import commands
import requests
import json
import os

def get_prefix(bot, msg):
    prefixes = [',']
    me=['kido.']
    if msg.author.id == '321586138932445184':
        return commands.when_mentioned_or(*me)(bot, msg)
    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot = commands.Bot(command_prefix=get_prefix,description='A music bot for discord, developed by Kido')

@bot.event
async def on_ready():
    print(bot.user.name)
    print("Connecting...")
    
@bot.command(aliases=['sim'])
async def simsimi(*msg):
    """Nói chuyện với Simsimi."""
    word = ' '.join(msg)
    api = "http://api.vietbot.net/simsimi.php?key=sibendz&text="
    response = requests.get(api, params=[("term", word)]).json()
    embed = discord.Embed(description="Không kết quả nào được tìm thấy!", colour=0xFF0000)
    if len(response["text"]) == 0:
            return await client.say(embed=embed)
    embed = discord.Embed(title="Simsimi BOT", description=word, colour=embed.colour)
    embed.add_field(name="Trả lời:", value=response['text'])
    embed.set_footer(text="Created by Kido. Have a great time!")
    await bot.say(embed=embed);

bot.run('NDQyMjA2NDcwMTYzOTIyOTU1.D0qdeQ._TpJNPkXbtGGluwoiwEttqbRoIo')
