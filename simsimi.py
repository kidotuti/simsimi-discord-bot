import asyncio
import discord
from discord.ext import commands
import requests
import json
import os

def get_prefix(bot, msg):
    prefixes = [',']
    me=['.']
    if msg.author.id == '321586138932445184':
        return commands.when_mentioned_or(*me)(bot, msg)
    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot = commands.Bot(command_prefix=get_prefix,description='A music bot for discord, developed by Kido')

@bot.event
async def on_ready():
    print(bot.user.name)
    print("Connecting...")
    await bot.change_presence(game=discord.Game(name=",sim | ,simsimi | Bot được phát triển bởi Kido"), status=discord.Status('idle'))
    
@bot.command(aliases=['sim'])
async def simsimi(*msg):
    """Nói chuyện với Simsimi."""
    word = ' '.join(msg)
    api = "http://api.vietbot.net/simsimi.php?key=sibendz"
    response = requests.get(api, params=[("text", word)]).json()
    embed = discord.Embed(description="Không kết quả nào được tìm thấy!", colour=0x30d7e9)
    if len(response["messages"]) == 0:
            return await client.say(embed=embed)
    embed=discord.Embed(title=response['messages'][0]['text'], color=embed.colour)
    embed.set_author(name="Simsimi", url="https://www.facebook.com/Kidokhongbigay", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqSu3M-XrbptMiku7dAIKVQQMb8euR-5osgBLpxXkktdqGBcxu")
    Channel = message.channel
    await self.bot.send_typing(Channel)
    await bot.say(embed=embed);
   

bot.run(os.environ['BOT_TOKEN'])
