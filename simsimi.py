import asyncio
import discord
from discord.ext import commands
import requests
import json
import os

def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
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
    try:
        word = ' '.join(msg)
        api = "http://api.vietbot.net/simsimi.php?key=sibendz&text="
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="Không kết quả nào được tìm thấy!", colour=0xFF0000)
        embed = discord.Embed(title="Simsimi BOT", colour=embed.colour)
        embed.set_footer(text="Created by Kido. Have a great time!")
        await bot.say(embed=embed)
   
bot.run(os.environ['BOT_TOKEN'])
