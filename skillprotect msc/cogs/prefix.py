import discord
import json
import requests
import asyncio
import sqlite3
import io
import json
from typing import Union
from discord.ext import commands
import json
from Tools.utils import getConfig, updateConfig, getGuildPrefix
from discord.ext import tasks
import asyncio
import re
import datetime
from discord import *
from discord import Forbidden
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import *



    
class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.data = sqlite3.connect('data.sqlite3', timeout=1)
		   
      


    @commands.command(aliases=['av', 'pfp'])
    async def avatar(self, ctx, txt: str = None):
        if txt:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(txt)
            if not user:
                user = ctx.guild.get_member(int(txt))
            if not user:
                user = ctx.guild.get_user(int(txt))
            if not user:
                await ctx.send('Could not find user.')
                return
        else:
            user = ctx.message.author

        try:
            avi = user.avatar_url.rsplit("?", 1)[0]
        except Exception:
            avi = user.avatar_url_as(static_format='png')
        try:
            em = discord.Embed(colour=0x2c2f33)
            em.set_author(name=f"{user.name}#{user.discriminator}", icon_url=avi)
            em.set_image(url=avi)
            await ctx.send(embed=em)
        except Exception:
            await ctx.send(avi)

    @commands.command(aliases=['mc', 'mcount', 'members'])
    async def membercount(self, ctx):
        membercount = str(ctx.guild.member_count)
        embed = discord.Embed(title="Members", color=0x76D7C4, timestamp=ctx.message.created_at)
        embed.description =membercount
        await ctx.send(embed=embed)

    @commands.command(aliases=['icon', 'serverpfp', 'servericon'])
    async def servergif(self, ctx):
        icon = str(ctx.guild.icon_url)
        name = str(ctx.guild.name)
        embed = discord.Embed(color=0x76D7C4, timestamp=ctx.message.created_at)
        embed.set_author(name=name, icon_url=icon)
        embed.set_image(url=icon)
        await ctx.send(embed=embed)

    @commands.command(aliases=['banner'])
    async def serverbanner(self, ctx):
        banner = str(ctx.guild.banner_url)
        name = str(ctx.guild.name)
        embed = discord.Embed(color=0x76D7C4, timestamp=ctx.message.created_at)
        embed.set_author(name=name, icon_url=banner)
        embed.set_image(url=banner)
        await ctx.send(embed=embed)








    @commands.command(aliases = ['очистить'])
    @commands.cooldown(1, 3, commands.BucketType.default)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
     await ctx.channel.purge(limit=amount)
     await ctx.send(embed=discord.Embed(
      title=":white_check_mark: | Очистить",
			  description=f">>> **Очистил `{amount}` сообщений.** ",
			  color=discord.Colour.green()), delete_after=10)



    @commands.command(aliases = ['масбан'])
    @commands.cooldown(1, 60, commands.BucketType.default)
    @commands.has_permissions(administrator = True)
    async def massban(self, ctx, mems:commands.Greedy[discord.User], reason = None): 
	    for member in mems:
             await ctx.guild.ban(member,reason = reason)
             await ctx.send(embed = discord.Embed(description = f">>> **Забанил `{len(mems)}` пользователей**", color = discord.Colour(self.color)))

	  

  
def setup(client):
    client.add_cog(Prefix(client))