import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('_'),description="TheEmperor™'s Discord bot.\n\nHelp Commands",owner_id=250674147980607488)


startup_extensions = [

    'cogs.fun'

]


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    while True:
        await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers boi!"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="_help"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="V 0.1.0"))
        await asyncio.sleep(10)

	
@bot.event
async def on_guild_join(guild):
    logChannel = bot.get_channel(417460269313425409)
    em = discord.Embed(color=discord.Color(value=0xffffff))
    em.title = "L3NNY has arrived in a new server!"
    em.description = f"Server: {guild}"
    await logChannel.send(embed=em)
    
	
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)
	
	
@bot.event
async def on_guild_remove(guild):
    logChannel = bot.get_channel(417460269313425409)
    em = discord.Embed(color=discord.Color(value=0xf44242))
    em.title = "L3NNY has left a server."
    em.description = f"Server: {guild}"
    await logChannel.send(embed=em)


@bot.command()
async def support(ctx):
    """Join the support server!"""
    color = discord.Color(value=0xffffff)
    em = discord.Embed(color=color, title='Help out in the development!')
    em.description = f"Link: https://discord.gg/zzzJAKM"
    await ctx.send(embed=em)

@bot.command()
async def ping(ctx):
    """Get the bot's Websocket latency."""
    color = discord.Color(value=0xffffff)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)


@bot.command()
async def invite(ctx):
    """lets me join ur club"""
    await ctx.send ("Lemme join dat club: https://discordapp.com/api/oauth2/authorize?client_id=414456650519412747&permissions=0&scope=bot")

    
@bot.command()
async def upvote(ctx):
    """Upvote me!"""
    await ctx.send ("Upvote me here! https://discordbots.org/bot/414456650519412747") 
   

@bot.command()
async def expose(ctx):
    """someone got expose"""
    await ctx.send ("Shut up {user.mentiom}! Stop lying! I **know** that you have been cheating on Venessia and dating Charlie's girlfriend! ~~even saw you and Charlie's girlfriend h00king uP in a BARN~~ So, {user.mention}, STOP LYING TO CHARLIE OR HE WILL SUE YOU FOR SEXUAL ALLIGATIONS FOR DATING HIS GIRL! ~~not even sure if yu can do that tho~~") 
	

@bot.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, num: int = None):
	"""Deletes messages. _purge [number].""" 
	try: 
	    if num is None:
	        await ctx.send("How many messages would you like me to delete? Usage: _purge [number]")
	    else:
	        try:
	            float(num)
	        except ValueError:
	            return await ctx.send("The number is invalid. Make sure it is a number...")
	        await ctx.channel.purge(limit=num+1)
	        msg = await ctx.send(f"Done ( ͡° ͜ʖ ͡°)")
	        await asyncio.sleep(3)
	        await msg.delete()
	except discord.Forbidden:
	    await ctx.send("OoF! I don't have **Manage Messages** permission.")
	
               
@bot.command()
async def say(ctx, *, message:str):
    """Speak as me!"""
    await ctx.message.delete()
    await ctx.send(message)      

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user: discord.Member = None):
	"""Kicks a member from the server."""
	if user is None:
		await ctx.send("Please tag the rebel to kick them!")
	else:
		try:
			await user.kick()
			await ctx.send(f"The administrator is putting on his boot. He kicks {user.mention} in the rear end. {user.mention} got kicked!.")
		except discord.Forbidden:
			await ctx.send("OoF! I'm missing **kick** permmision.")
	
	
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member = None):
	"""Bans a member from the server."""
	if user is None:
		await ctx.send("Please tag that **intense** rebel to ban!")
	else:
		try:
			await user.ban()
			await ctx.send(f"The administrator is getting the ban hammer out of the case. He swings it at {user.mention}. Ouch! {user.mention} has been banned.")
		except discord.Forbidden:
			await ctx.send("OOOOF! You didn't give me the **ban** permission.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, user: discord.Member = None):
    '''Mutes a user'''
    if user is None:
    	return await ctx.send("Please tag that annoying user to mute them!")
    try:
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send(f"{user.mention} has been muted. FINALLY!")
    except discord.Forbidden:
        return await ctx.send(":x: I don't have **Manage Channel** permmition.")  


@bot.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, user: discord.Member = None):
	'''Un-mutes a user'''
	if user is None:
		return await ctx.send("Please tag a uesr to unmute them!")
	try:
		await ctx.channel.set_permissions(user, send_messages=True)
		await ctx.send(f"{user.mention} is now unmuted. Hope they learned their lesson.")
	except discord.Forbidden:
		await ctx.send(":x: Couldn't unmute the user. I need the **Manage Channels** permission.")
  
@bot.command()
async def github(ctx):
    """Get my github link"""
    await ctx.send("Here is my github: http://bit.ly/2ogUv2T")

@bot.command()
async def lit(ctx):
    """You lit? Use this command!"""
    await ctx.send("**Only the lit people can listen to this! http://bit.ly/2r3aFyX**")	
	
	
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded extension: {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

if not os.environ.get('TOKEN'):
   print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
