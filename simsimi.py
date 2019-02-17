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
    await bot.change_presence(game=discord.Game(name=",sim | ,simsimi | Bot được phát triển bởi Kido, dựa trên ý tưởng của Thịnh. Have fun!"), status=discord.Status('idle'))
    
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Simsimi", description="Có mỗi nhiêu đây lệnh thôi. Kido hứa sẽ update sau", color=0xeee657)
    embed.add_field(name="Urban", value="Gõ ,urban <từ cần tra nghĩa> để tra nghĩa tiếng Anh trên từ điển Urban")
    embed.add_field(name="Hug", value="Gõ ,hug <mention user> để 'ôm' ai đó theo cách riêng của bạn!")
    embed.add_field(name="Sim | Simsimi", value="Gõ ,sim <nội dung> để nói chuyện với Simsimi")
    embed.set_footer(text="Bot được phát triển bởi Kido")
    await bot.say(embed=embed)
    
@bot.command(aliases=['sim'])
async def simsimi(*msg):
    """Nói chuyện với Simsimi."""
    word = ' '.join(msg)
    api = "http://api.vietbot.net/simsimi.php?key=sibendz"
    response = requests.get(api, params=[("text", word)]).json()
    embed = discord.Embed(description="Không kết quả nào được tìm thấy!", colour=0x30d7e9)
    if len(response["messages"]) == 0:
            return await bot.say(embed=embed)
    embed=discord.Embed(title=response['messages'][0]['text'], color=embed.colour)
    embed.set_author(name="Simsimi", url="https://www.facebook.com/Kidokhongbigay", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqSu3M-XrbptMiku7dAIKVQQMb8euR-5osgBLpxXkktdqGBcxu")
    await bot.say(embed=embed)
    
@bot.command(aliases=['ud'])
async def urban(*msg):
    """Tìm từ trong từ điển Urban."""
    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    response = requests.get(api, params=[("term", word)]).json()
    embed = discord.Embed(description="Không kết quả nào được tìm thấy!", colour=0xFF0000)
    if len(response["list"]) == 0:
        return await bot.say(embed=embed)
    embed = discord.Embed(title="Từ cần tra nghĩa", description=word, colour=embed.colour)
    embed.add_field(name="Định nghĩa hàng đầu:", value=response['list'][0]['definition'])
    embed.add_field(name="Ví dụ:", value=response['list'][0]["example"])
    embed.set_footer(text="Thẻ: " + ', '.join(response['tags']))
    await bot.say(embed=embed)
   
@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member = None):
    """Ôm ai đó!"""
    if member is None:
            await bot.say(ctx.message.author.mention + " đã được ôm!")
    else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " đã tự ôm chính mình!")
            else:
                await bot.say(member.mention + " đã được ôm bởi " + ctx.message.author.mention + "!")

bot.run(os.environ['BOT_TOKEN'])
