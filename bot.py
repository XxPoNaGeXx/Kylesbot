import discord
import random
from discord.ext import commands

'''Setup bot'''

description='Just testing'
bot_prefix ='>'


client = commands.Bot(description=description, command_prefix=bot_prefix)
client.remove_command("help")

'''Embeds setup'''

embed=discord.Embed(title="Pong!", description="I have received your command.", color=0xff80ff)
embed.set_author(name="Kyle's  Bot", icon_url='https://pbs.twimg.com/profile_images/881587329542082565/AXKXs4K8_400x400.jpg')
embed.set_thumbnail(url='http://www.pngall.com/wp-content/uploads/2016/05/Ping-Pong-Download-PNG.png')
embed.add_field(name="More coming soon!", value="👌", inline=True)
embed.set_footer(text="Made with 💖 by @Kyle#9494")


embed_help=discord.Embed(title="Commands:", description="- >help \n - >ping \n - >insult", color=0xff80ff)
embed_help.set_author(name="Kyle's  Bot", icon_url='https://pbs.twimg.com/profile_images/881587329542082565/AXKXs4K8_400x400.jpg')
embed_help.set_thumbnail(url='http://et-38d7.kxcdn.com/emojione-512/2753.png')
embed_help.set_footer(text="Made with 💖 by @Kyle#9494")

embed_info=discord.Embed(title="Opensource - Github 💖", url='http://googlc.eom', color=0xff80ff)
embed_info.set_author(name="Kyle's  Bot", icon_url='https://pbs.twimg.com/profile_images/881587329542082565/AXKXs4K8_400x400.jpg')
embed_info.set_thumbnail(url='https://emojipedia-us.s3.amazonaws.com/thumbs/160/emoji-one/104/victory-hand_270c.png')
embed_info.add_field(name="Libary:", value="Discord.py", inline=True)
embed_info.add_field(name="Owner:", value="Kyle#9494", inline=True)
embed_info.add_field(name="Commands:", value=">help", inline=True)
embed_info.add_field(name="Version", value="0.1", inline=True)
embed_info.add_field(name="Credits", value="Desiree#3658 - Helped fixed reactions.", inline=False)
embed_info.set_footer(text="Made with 💖 by @Kyle#9494")


@client.event
async def on_ready():
    print('Logged in to Discord')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))



'''Ping command'''

@client.command(pass_context=True)
async def ping(ctx):
    await client.say(embed=embed)

'''Help command'''

@client.command(pass_context=True)
async def help(ctx):
    await client.say(embed=embed_help)

'''Info command'''

@client.command(pass_context=True)
async def info(ctx):
    await client.say(embed=embed_info)


'''Set up insults'''


insults = ['cunt', 'fuck boy', 'gay boy', 'faggot', 'sam']


@client.command(pass_context=True)
async def insult(ctx):
    author = ctx.message.author.mention
    insult_send = str(author + " you are a " + str(random.choice(insults)))
    await client.say(insult_send)

'''Reactions'''

react_strings = ['test', 'testing']

@client.event
async def on_message (message):
    await client.process_commands(message)
    if message.content in react_strings:
        await client.add_reaction(message, '💖')


client.run('MzMxNDc1OTI2OTI5ODk5NTIy.DDwGhw.tJPiuQ4C9SdAJMMSMLqAP2Ki5xw')



