import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
import json
import idioticapi
from discord.ext import commands


class fun:
    def __init__(self, bot):
        self.bot = bot
        with open('data/apikeys.json') as f:
            lol = json.load(f)
            self.client = lol.get("idioticapi")


    def format_avatar(self, avatar_url):
        if avatar_url.endswith(".gif"):
            return avatar_url + "?size=2048"
        return avatar_url.replace("webp","png")
        
        
        
        
        
        
    @commands.command()
    async def annoy(self, ctx, user: discord.Member):
        """ping someone"""
        msg = await ctx.send(f"rip {user}")
        await asyncio.sleep(2)
        await msg.edit(content="{user.mention}")
        await asyncio.sleep(2)
        await msg.edit(content="{user.mention}")
        await asyncio.sleep(2)
        await msg.edit(content="{user.mention}")
        await asyncio.sleep(2)
        await msg.edit(content="{user.mention}")
        await asyncio.sleep(2)
        await msg.edit(content="{user.mention}")
        await asyncio.sleep(3)
        await msg.edit(content="{user.mention}")
        await asyncio.sleep(3)
        await msg.edit(content="{user.mention}")
        await asyncio.sleep(4)
        await msg.edit(content=f"{user.mention} {user.mention} {user.mention} {user.mention} {user.mention} {user.mention} rip")   
        
        
       
        
def setup(bot):
    bot.add_cog(fun(bot))
