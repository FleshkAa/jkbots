import discord
import json
import asyncio
import platform
import random
import pytz
import time
import humanfriendly
from Tools.utils import getConfig, getGuildPrefix, guild_owner_only, updateConfig
from config import EMOJIS, MAIN_COLOR, WEBSITE_LINK, SUPPORT_SERVER_LINK, CREDITS_CONTRIBUTORS, start_time, SUGGESTION_CHANNEL, BUG_REPORT_CHANNEL
from discord.ext import commands
from discord.utils import get
from discord import Client
from datetime import datetime
from datetime import date
import functools
from discord.ext import commands
from config import (
    EMOJIS, PINK_COLOR_2, MAIN_COLOR
)
wiggle_concurrency = []

class RoleManagement(commands.Cog):
    def __init__(self, client):
        self.client = client
    async def get_img_from_api(self, embed_stuff, api_url, thingy):
        e = discord.Embed(
            title=embed_stuff[0],
            color=embed_stuff[1]
        )
        async with self.client.session.get(api_url) as r:
            j = await r.json()
            e.set_image(url=j[thingy])
        return e

    @commands.command(aliases=["jr"])
    @commands.has_permissions(administrator=True)
    async def joinrole(self, ctx, addORremove=None, role: discord.Role = None):

        data = getConfig(ctx.guild.id)

        if addORremove == "?add":
            if role == None:
                return await ctx.send("Укажите роль")

            if role.id in data["joinroles"]:
                return await ctx.send("Эта роль уже назначена")

            else:
                data["joinrole"] = True
                data["joinroles"].append(role.id)

                updateConfig(ctx.guild.id, data)
                prefix = data["prefix"]
                embed = discord.Embed(title="Роль при заходе",
                                      description=f"`{prefix}jr ?add <роль>` - выдать всем роль\n"
                                                  f"`{prefix}jr ?remove <роль>` - забрать роль",
                                      colour=discord.Colour.blue())
                rolesinjoinroles = data["joinroles"]

                result = ' '
                for i in rolesinjoinroles:
                    role2 = get(ctx.guild.roles, id=i)
                    if role2 == None:
                        role3 = '*Не удалось получить ник*'
                    else:
                        role3 = role2.mention
                    result += f"{role3} ||`{i}`||\n"

                embed.add_field(name="Роли",
                                value=f"Каждому пользователю, присоединяющемуся к этому серверу, будут добавлены следующие роли: \n"
                                      f"{result}")
                await ctx.send(embed=embed)

        if addORremove == "?remove":
            if role == None:
                return await ctx.send("укажите роль")

            if role.id not in data["joinroles"]:
                return await ctx.send("Эта роль не задана как роль присоединения")

            else:
                data["joinroles"].remove(role.id)
                if data["joinroles"] == []:
                    data["joinrole"] = False

                updateConfig(ctx.guild.id, data)
                prefix = data["prefix"]
                embed = discord.Embed(title="роль при заходе",
                                      description=f"`{prefix}jr ?add <роль>` - выдать всем роль\n"
                                                  f"`{prefix}jr ?remove <роль>` - забрать роль",
                                      colour=discord.Colour.blue())
                rolesinjoinroles = data["joinroles"]

                result = ' '
                for i in rolesinjoinroles:
                    role2 = get(ctx.guild.roles, id=i)
                    if role2 == None:
                        role3 = '*Не удалось получить ник*'
                    else:
                        role3 = role2.mention
                    result += f"{role3} ||`{i}`||\n"

                embed.add_field(name="Roles",
                                value=f"Каждому пользователю, присоединяющемуся к этому серверу, будут добавлены следующие роли: \n"
                                      f"{result}")

                await ctx.send(embed=embed)

        if addORremove == None:
            data = getConfig(ctx.guild.id)
            prefix = data["prefix"]
            embed = discord.Embed(title="Join Roles",
                                  description=f"`{prefix}jr ?add <роль>` - выдаёт роль всем\n"
                                              f"`{prefix}jr ?remove <роль>` - заберает роль",
                                  colour=discord.Colour.blue())
            rolesinjoinroles = data["joinroles"]
            result = ' '
            for i in rolesinjoinroles:
                role2 = get(ctx.guild.roles, id=i)
                if role2 == None:
                    role3 = '*Не удалось получить ник*'
                else:
                    role3 = role2.mention
                result += f"{role3} ||`{i}`||\n"

            if data["joinroles"] == []:
                embed.add_field(name="Роли",
                                value=f"Каждому пользователю, присоединяющемуся к этому серверу, будут добавлены следующие роли: \n"
                                      f"*None*")
            else:
                embed.add_field(name="Роли",
                                value=f"Каждому пользователю, присоединяющемуся к этому серверу, будут добавлены следующие роли: \n"
                                      f"{result}")

            await ctx.send(embed=embed)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(name='rps', aliases=['rockpaperscissors'], help="Play Rock, Paper, Scissors game")
    async def rps(self, ctx):
        def check_win(p, b):
            if p == '🌑':
                return False if b == '📄' else True
            if p == '📄':
                return False if b == '✂' else True
            # p=='✂'
            return False if b == '🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send("**Камень ножницы Бумага**\nВыберите свою форму:", delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != self.client.user and user == ctx.author and (str(reaction.emoji) == '🌑' or '📄' or '✂')
        try:
            reaction, _ = await self.client.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Время вышло!  :stopwatch:")
        else:
            await ctx.send(f"**Твой выбор:\t{reaction.emoji}\nМой выбор:\t{bot_emoji}**")
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**Это галстук :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):
                await ctx.send("**Ты победил :sparkles:**")
            else:
                await ctx.send("**я выигрываю :robot:**")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(category="images", help="Get a random anime image.")
    async def anime(self, ctx):
        await ctx.message.reply(embed=await self.get_img_from_api(["uwu", PINK_COLOR_2], "https://shiro.gg/api/images/neko", 'url'))

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(category="images", aliases=['meow', 'cats'], help="Gives a random cute cat picture.")
    async def cat(self, ctx):
        await ctx.message.reply(embed=await self.get_img_from_api(["Meow!", MAIN_COLOR], "http://aws.random.cat/meow", 'file'))

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(category="images", aliases=['dogs'], help="Gives a random cute dog picture.")
    async def dog(self, ctx):
        await ctx.message.reply(embed=await self.get_img_from_api(["Woof!", MAIN_COLOR], "https://some-random-api.ml/img/dog", 'link'))

  

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(category="images", help="Gives a random panda picture.")
    async def panda(self, ctx):
        await ctx.message.reply(embed=await self.get_img_from_api(["Panda!", MAIN_COLOR], "https://some-random-api.ml/img/panda", 'link'))

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(category="images", help="Gives a random redpanda picture.")
    async def redpanda(self, ctx):
        await ctx.message.reply(embed=await self.get_img_from_api(["Panda but red!", MAIN_COLOR], "https://some-random-api.ml/img/red_panda", 'link'))

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(category="images", aliases=['pika'], help="Gives a random pikachu picture.")
    async def pikachu(self, ctx):
        await ctx.message.reply(embed=await self.get_img_from_api(["Pika!", MAIN_COLOR], "https://some-random-api.ml/img/pikachu", 'link'))


    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command(category="In", help="Invite")
    async def invite(self, ctx):
        await ctx.message.reply(embed=discord.Embed(
            title="Invite Skill Protect \💖",
            description="Большое спасибо!",
            color=MAIN_COLOR,
            url=f"https://discord.com/oauth2/authorize?client_id={self.client.user.id}&permissions=8&scope=bot%20applications.commands"
        ).set_footer(text="ПУК)"))


def setup(client):
    client.add_cog(RoleManagement(client))