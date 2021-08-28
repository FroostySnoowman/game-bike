import discord
import random
import json
import emoji
import os
import datetime
import asyncio
import pytz
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='~', intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
	activity = discord.Activity(type=discord.ActivityType.listening, name="Version 1.0.3")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	print('Signed in as {0.user}'.format(client))

@tasks.loop(seconds = 15)
async def myLoop():
	await client.wait_until_ready()
	activity = discord.Activity(type=discord.ActivityType.listening, name="Bike Game Smells")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Activity(type=discord.ActivityType.listening, name="HAI OLLIEPOO")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Activity(type=discord.ActivityType.listening, name="Jack Wilder Is The Best!")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Activity(type=discord.ActivityType.listening, name="xD you smell")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Activity(type=discord.ActivityType.listening, name="Phantom's Remix")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Activity(type=discord.ActivityType.listening, name="Kimmy Is Good At Bike Game... jk")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Activity(type=discord.ActivityType.listening, name="BRJ Is Gay")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)
	activity = discord.Activity(type=discord.ActivityType.listening, name="Version 1.0.3")
	await client.change_presence(status=discord.Status.online,
	                             activity=activity)
	await asyncio.sleep(15)

myLoop.start()

@client.event
async def on_member_join(member):
  welcomechannel =  client.get_channel(710999786437738498)
  x = discord.utils.get(member.guild.roles, name='Unverified')
  await member.add_roles(x)
  x = f'{member.mention}'
  embed=discord.Embed(title="Welcome", url="", 
  description="Go to <#772218116830396436> to see the rest of the channels.".format(member.mention), 
  color=discord.Color.green())
  await welcomechannel.send(content=x, embed=embed)
  embed=discord.Embed(title="Welcome", url="", 
  description=f"Welcome to **{member.guild.name}**! \n \nThis server is welcoming to all, from people we have never talked to before to people who know all staff already. Active to semi-active members are highly appreciated and any questions anyone has staff and or members will be open to answer :')".format(member.mention), 
  color=discord.Color.green())
  await member.send(embed=embed)

@client.event
async def on_message(message, reason=None):
  if not message.guild:
    return
  if "game" in message.content.lower() and (message.author.id == 180046139402354690):
    await message.delete()
  if "bike" in message.content.lower() and (message.author.id == 180046139402354690):
    await message.delete()
  member_role = discord.utils.get(message.guild.roles, name='Members')
  if "pls rob" in message.content.lower() and len(message.author.roles) == 2 and member_role in message.author.roles:
    await message.delete()
    await message.author.send('Lol imagine trying to join and rob random servers. Dumbass.')
    await message.author.ban(reason="TRYING TO STEAL, YOU THINK YOU CAN GET AWAY, NAH, YOU'RE GETTING BANNED, GG")
  if "game bike" in message.content.lower() and (message.author.id == 180046139402354690):
    await message.delete()
  if "gamebike" in message.content.lower() and (message.author.id == 180046139402354690):
    await message.delete()
  if "bike game" in message.content.lower() and (message.author.id == 180046139402354690):
    await message.delete()
  if "bike game" in message.content.lower() and (message.author.id == 180046139402354690):
    await message.delete()
  if "hoe" in message.content.lower() and (message.author.id == 180046139402354690):
    await message.delete()
  rolechannel = client.get_channel(790725436748464169)
  verifychannel = client.get_channel(772218116830396436)
  role1 = discord.utils.get(message.guild.roles, name='Members')
  role = discord.utils.get(message.guild.roles, name='Unverified')
  bikerace = discord.utils.get(message.guild.roles, name='Bike Race')
  offtopic = discord.utils.get(message.guild.roles, name='Off-Topic')
  games = discord.utils.get(message.guild.roles, name='Gamers')
  black = discord.utils.get(message.guild.roles, name='Black')
  green = discord.utils.get(message.guild.roles, name='Green')
  lime = discord.utils.get(message.guild.roles, name='Lime')
  dblue = discord.utils.get(message.guild.roles, name='Dark Blue')
  maroon = discord.utils.get(message.guild.roles, name='Maroon')
  purple = discord.utils.get(message.guild.roles, name='Purple')
  white = discord.utils.get(message.guild.roles, name='White')
  grey = discord.utils.get(message.guild.roles, name='Grey')
  gold = discord.utils.get(message.guild.roles, name='Gold')
  salmon = discord.utils.get(message.guild.roles, name='Salmon')
  brown = discord.utils.get(message.guild.roles, name='Brown')
  orange = discord.utils.get(message.guild.roles, name='Orange')
  red = discord.utils.get(message.guild.roles, name='Red')
  yellow = discord.utils.get(message.guild.roles, name='Yellow')
  lblue = discord.utils.get(message.guild.roles, name='Light Blue')
  pink = discord.utils.get(message.guild.roles, name='Pink')
  coquelicot = discord.utils.get(message.guild.roles,name='Coquelicot')
  if message.content not in ("!bikerace", "!games", "!offtopic", "!unbikerace", "!ungames", "!unofftopic", "!pink", "!lblue", "!yellow", "!red", "!orange", "!brown", "!salmon", "!gold", "!grey", "!white", "!purple", "!maroon", "!dblue", "!lime", "!green", "!black", "!unpink", "!unlblue", "!unyellow", "!unred", "!unorange", "!unbrown", "!unsalmon", "!ungold", "!ungrey", "!unwhite", "!unpurple", "!unmaroon", "!undblue", "!unlime", "!ungreen", "!unblack", "!coquelicot", "!uncoquelicot") and (message.channel == rolechannel) and (message.author.id != 503641822141349888) and (message.author.id != 820228188100886529) and (message.author.id != 728008705651638321) and (message.author.id != 541216254845779982):
    await message.delete()
    embed=discord.Embed(title="Role Error", url="", 
    description="Hey! You cannot send that message here. Check back on the **Available Roles** embed to see what commands you can run.", 
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content != '.verify' and (message.channel == verifychannel) and (message.author.id != 503641822141349888) and (message.author.id != 820228188100886529) and (message.author.id != 728008705651638321) and (message.author.id != 541216254845779982):
    await message.delete()
    embed=discord.Embed(title="Verification Error", url="", 
    description="Hey! You cannot send that message here. Please type `.verify` in <#772218116830396436> to gain access to the rest of the server.", 
    color=discord.Color.red())
    await message.channel.send(embed=embed, delete_after=10)
  if message.content == '.verify' and (message.channel == verifychannel):
    await message.delete()
    embed=discord.Embed(title="Verification Passed", url="", 
    description="You are now successfully verified, thanks!", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
    await message.author.add_roles(role1)
    await message.author.remove_roles(role)
  if message.content == '!bikerace' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(bikerace)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Bike Race` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!games' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(games)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Gamer` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!offtopic' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(offtopic)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Off-Topic` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!unbikerace' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(bikerace)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have successfully been removed from the `Bike Race` role.", 
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!ungames' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(games)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Gamers` role.", 
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unofftopic' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(offtopic)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Off-Topic` role.", 
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!black' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(black)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Black` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!green' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(green)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Green` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!lime' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(lime)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Lime` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!dblue' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(dblue)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Dark Blue` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!maroon' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(maroon)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Maroon` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!purple' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(purple)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Purple` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!white' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(white)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `White` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!grey' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(grey)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Grey` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!gold' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(gold)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Gold` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!salmon' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(salmon)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Salmon` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!brown' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(brown)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Brown` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!orange' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(orange)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Orange` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!red' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(red)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Red` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!yellow' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(yellow)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Yellow` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!lblue' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(lblue)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Light Blue` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!pink' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(pink)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Pink` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  if message.content == '!unblack' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(black)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Black` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!ungreen' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(green)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Green` role.", 
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unlime' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(lime)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Lime` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!undblue' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(dblue)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Dark Blue` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unmaroon' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(maroon)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Maroon` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unpurple' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(purple)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Purple` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unwhite' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(white)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `White` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!ungrey' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(grey)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Grey` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!ungold' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(gold)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Gold` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unsalmon' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(salmon)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Salmon` role.", 
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unbrown' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(brown)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Brown` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unorange' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(orange)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Orange` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unred' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(red)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Red` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unyellow' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(yellow)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Yellow` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unlblue' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(lblue)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Light Blue` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!unpink' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(pink)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Pink` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!uncoquelicot' and (message.channel == rolechannel):
    await message.delete()
    await message.author.remove_roles(coquelicot)
    embed=discord.Embed(title="Roles Removal", url="", 
    description="You have sucessfully been removed from the `Coquelicot` role.",
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '!coquelicot' and (message.channel == rolechannel):
    await message.delete()
    await message.author.add_roles(coquelicot)
    embed=discord.Embed(title="Roles Success", url="", 
    description="You have successfully gotten the `Coquelicot` role.", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
  await client.process_commands(message)

@client.command()
async def enlarge(ctx, emoji: discord.PartialEmoji = None):
    if not emoji:
        await ctx.send("You need to provide an emoji!")
    else:
        await ctx.send(emoji.url)

@client.command()
async def roles(ctx):
  embed = discord.Embed(title="Available Roles",
  url ="",
  description="**__Color Roles__** \n \n**Black** ➳ Use `!black` To Get The Role. \n**Green** ➳ Use `!green` To Get The Role. \n**Lime** ➳ Use `!lime` To Get The Role. \n**Dark Blue** ➳ Use `!darkblue` To Get The Role. \n**Maroon** ➳ Use `!maroon` To Get The Role. \n**Purple** ➳ Use `!purple` To Get The Role. \n**White** ➳ Use `!white` To Get The Role. \n**Grey** ➳ Use `!grey` To Get The Role. \n**Gold** ➳ Use `!gold` To Get The Role. \n**Salmon** ➳ Use `!salmon` To Get The Role. \n**Brown** ➳ Use `!brown` To Get The Role. \n**Orange** ➳ Use `!orange` To Get The Role. \n**Red** ➳ Use `!red` To Get The Role. \n**Yellow** ➳ Use `!yellow` To Get The Role. \n**Light Blue** ➳ Use `lblue` To Get The Role. \n**Pink** ➳ Use `!pink` To Get The Role. \n**Coquelicot** ➳ Use `!coquelicot To Get The Role. \n \n**__Channel Roles__** \n \n**Bike Race** ➳ Use `!bikerace` To Get The Role.",
  color=discord.Color.green())
  await ctx.message.delete()
  await ctx.send(embed=embed)

@client.command()
async def roles2(ctx):
  embed = discord.Embed(title="Available Roles",
  url ="",
  description="**__Channel Roles__** \n \n__Adding__ \n \n**Bike Race** ➳ Use `!bikerace` To Get The Role. \n**Gamers** ➳ Use `!games` To Get The Role. \n**Off Topic** ➳ Use `!offtopic` To Get The Role. \n \n__Removing__ \n \n**Bike Race** ➳ Use `!unbikerace` To Remove The Role. \n**Gamers** ➳ Use `!ungames` To Remove The Role. \n**Off Topic** ➳ Use `!unofftopic` To Remove The Role. \n \n**__Color Roles__** \n \n__Adding__ \n \n**Black** ➳ Use `!black` To Get The Role. \n**Green** ➳ Use `!green` To Get The Role. \n**Lime** ➳ Use `!lime` To Get The Role. \n**Dark Blue** ➳ Use `!dblue` To Get The Role. \n**Maroon** ➳ Use `!maroon` To Get The Role. \n**Purple** ➳ Use `!purple` To Get The Role. \n**White** ➳ Use `!white` To Get The Role. \n**Grey** ➳ Use `!grey` To Get The Role. \n**Gold** ➳ Use `!gold` To Get The Role. \n**Salmon** ➳ Use `!salmon` To Get The Role. \n**Brown** ➳ Use `!brown` To Get The Role. \n**Orange** ➳ Use `!orange` To Get The Role. \n**Red** ➳ Use `!red` To Get The Role. \n**Yellow** ➳ Use `!yellow` To Get The Role. \n**Light Blue** ➳ Use `!lblue` To Get The Role. \n**Pink** ➳ Use `!pink` To Get The Role. \n**Coquelicot** ➳ Use `!coquelicot` To Get The Role. \n \n__Removing__ \n \n**Black** ➳ Use `!unblack` To Remove The Role. \n**Green** ➳ Use `!ungreen` To Remove The Role. \n**Lime** ➳ Use `!lime` To Get The Role. \n**Dark Blue** ➳ Use `!undblue` To Remove The Role. \n**Maroon** ➳ Use `!unmaroon` To Remove The Role. \n**Purple** ➳ Use `!unpurple` To Remove The Role. \n**White** ➳ Use `!unwhite` To Remove The Role. \n**Grey** ➳ Use `!ungrey` To Remove The Role. \n**Gold** ➳ Use `!ungold` To Remove The Role. \n**Salmon** ➳ Use `!unsalmon` To Remove The Role. \n**Brown** ➳ Use `!unbrown` To Remove The Role. \n**Orange** ➳ Use `!unorange` To Remove The Role. \n**Red** ➳ Use `!unred` To Remove The Role. \n**Yellow** ➳ Use `!unyellow` To Remove The Role. \n**Light Blue** ➳ Use `!unlblue` To Remove The Role. \n**Pink** ➳ Use `!unpink` To Remove The Role. \n**Coquelicot** ➳ Use `!uncoquelicot` To Remove The Role.",
  color=discord.Color.green())
  await ctx.message.delete()
  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
	await ctx.channel.purge(limit=limit + 1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)


@clean.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You cannot do that!")

@client.command()
@commands.has_permissions(administrator=True)
async def promote(ctx, member: discord.Member, prom = None):
  helper = discord.utils.get(ctx.guild.roles, name='Helper')
  mod = discord.utils.get(ctx.guild.roles, name='Mod')
  srmod = discord.utils.get(ctx.guild.roles, name='Sr. Mod')
  admin = discord.utils.get(ctx.guild.roles, name='Admin')
  sradmin = discord.utils.get(ctx.guild.roles, name='Sr. Admin')
  stafflogs = client.get_channel(711298161171234816)

  if prom == 'helper' :
    await member.add_roles(helper) 
    embed=discord.Embed(title="Staff Promotion", url="", 
    description=f"GG {member.mention} on the promotion to **Helper**!", 
    color=discord.Color.green())
    embed.set_footer(text = f"Promoter: {ctx.author}")
    await stafflogs.send(embed=embed)

  elif prom == 'mod' :
    await member.add_roles(mod) 
    embed=discord.Embed(title="Staff Promotion", url="", 
    description=f"GG {member.mention} on the promotion to **Mod**!", 
    color=discord.Color.green())
    embed.set_footer(text = f"Promoter: {ctx.author}")
    await stafflogs.send(embed=embed)
  
  elif prom == 'srmod' :
    await member.add_roles(srmod)
    embed=discord.Embed(title="Staff Promotion", url="", 
    description=f"GG {member.mention} on the promotion to **Sr. Mod**!", 
    color=discord.Color.green())
    embed.set_footer(text = f"Promoter: {ctx.author}")
    await stafflogs.send(embed=embed)
  
  elif prom == 'admin' :
    await member.add_roles(admin)
    embed=discord.Embed(title="Staff Promotion", url="", 
    description=f"GG {member.mention} on the promotion to **Admin**!", 
    color=discord.Color.green())
    embed.set_footer(text = f"Promoter: {ctx.author}")
    await stafflogs.send(embed=embed)

  elif prom == 'sradmin' :
    await member.add_roles(sradmin)
    embed=discord.Embed(title="Staff Promotion", url="", 
    description=f"GG {member.mention} on the promotion to **Sr. Admin**!", 
    color=discord.Color.green())
    embed.set_footer(text = f"Promoter: {ctx.author}")
    await stafflogs.send(embed=embed)

  await ctx.message.delete()

@client.command()
async def staff(ctx):
    embed=discord.Embed(title="Game Bike Staff", url="", 
    description="**__Owner__** » <@188411871487852544> \n \n**__Creator__** <@353180945702191106> \n \n**__Developer__** » <@541216254845779982> \n**__Developer__** » <@728008705651638321> \n \n**__Manager__** » <@503641822141349888> \n \n**__Sr. Admin__** » <@498710556438560778> \n \n**__Admin__** » <@561652984791171083> \n**__Admin__** » <@649332947530547236> \n**__Admin__** » <@712425663168249886> \n \n**__Sr. Mod__** » <@249257480117288960> \n \n**__Mod__** » N/A \n \n**__Helper__** » <@490443459434512385> \n**__Helper__** » <@383692150354870272> \n \nApply For Staff At <#778889049602523147>", 
    color=discord.Color.green())
    embed.set_footer(text = "Bot Developer » Someone#0171")
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def info(ctx):
    embed=discord.Embed(title="Game Bike Info", url="", 
    description="**__Discord Knowledge__** \n \nLuis - SirKnight - NotCrunchy \n \nLuis - Custard \n \nLiam - HotDog \n \nLiv - Olivia - notsur3rightnow - infinityflame11 \n \nAlex - Alex4259 \n \nMatt - akup6 - aeiou \n \nEric - ehaxxl \n \nBrian - itzzzzzzzbrian - BryanNotBrian \n \nLinus - Horny Ostrich - Ostrich Official \n \nWorld Dom - Team of good players \n \nPat - PatInTheHat - Confused Crunchy \n \nJake - JakiePoo - Froosty \n \n**__Memes__** \n \nTypical Pat - Pat is usually confused and we use say `Typical Pat` to make fun of people that are confused. \n \n:ok::up::six: - akup6 hates this name and we once again make fun of him by using it. \n \n__**Bike Race General**__ \n \nBike Race was a kids game and died many years ago the players that play now used to play in their childhood, but many people have quit since. \n \nTurbos - You get turbos by entering special tournaments every Saturday for 10 gas per tournament. There are 4 tournaments that happen every 6 hours.", 
    color=discord.Color.green())
    embed.set_footer(text = "Bot Developer » Someone#0171")
    await ctx.channel.send(embed=embed)
    embed=discord.Embed(title="Game Bike Info", url="", 
    description="This server is mainly for the game of bike race, but it's for general chatting. Lately the server has lacking in activity due to the final and previous drama, but we are slowly coming out of that and we will eventually get back on your feet. If you manage to invite 100+ people I'll personally give you discord nitro, but all 100 people must stay. That should be all the information you need.", 
    color=discord.Color.green())
    embed.set_footer(text = "Bot Developer » Someone#0171")
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()

@client.command()
@commands.has_permissions(administrator=True)
async def pp2(ctx, role: discord.Role, pos: int):
    x = discord.utils.get(ctx.guild.roles, name='Manager')
    try:
        await role.edit(position=pos)
        await ctx.send("Role moved.")
    except discord.Forbidden:
        await ctx.send("You do not have permission to do that")
    except discord.HTTPException:
        await ctx.send("Failed to move role")
    except discord.InvalidArgument:
        await ctx.send("Invalid argument")

client.run('')
