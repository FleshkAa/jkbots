import discord
from discord.ext import commands
import platform
from Tools.utils import getGuildPrefix, getConfig
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from reactionmenu import ReactionMenu, Button, ButtonType
from discord import *
import datetime
import time
from datetime import datetime
import os
import reactionmenu
from reactionmenu import ButtonsMenu, ComponentsButton


class General(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.counter = 0

    @commands.command(description="Показывает информацию о безопасности сервера")
    async def about(self, ctx):
        emote = (":white_small_square:")
        dpyVersion = discord.__version__
        serverCount = len(self.client.guilds)
        about = discord.Embed(colour=0x2f3136, title=f"О `{self.client.user.name}`")
        about.add_field(name="Общая информация: ",
                        value=f"**Имя:** `{self.client.user.name}`\n"
                              f"{emote}**Тег:** `{self.client.user}`\n"
                              f"{emote}**Ай ди:** `{self.client.user.id}`\n"
                              f"{emote}**Пинг:** `{self.client.user.mention}`\n"
                              f"**Создан:** `<t:{round(self.client.user.created_at.timestamp())}:R>`\n"
                              f"**Версия:** `{dpyVersion}`\n"
                              f"**Пинг:** `{round(self.client.latency * 1000)}ms`\n"
                              f"**Серверов:** `{serverCount}`\n"
                              f"{emote}**Всего участников:** `{len(set(self.client.get_all_members()))}`")
        about.add_field(name="**――――――――――**", value=f"[АВАТАРКА]({self.client.user.avatar_url})", inline=False)
        about.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=about)

  

    @commands.command(description="Shows information about this server")
    async def serverinfo(self, ctx):
        emote = (":white_small_square:")
        guild_roles = len(ctx.guild.roles)
        guild_members = len(ctx.guild.members)
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        channels = text_channels + voice_channels

        result = ' '
        data = getConfig(ctx.guild.id)
        userinwhitelist = data["whitelist"]
        for i in userinwhitelist:
            user2 = self.client.get_user(i)
            if user2 == None:
                user = 'Unable to Fetch Name'
            else:
                user = user2.mention
            result += f"{user}\n"

        serverinfo = discord.Embed(colour=0x2f3136, title="Информация о СЕРВЕРЕ")
        serverinfo.add_field(name="Общая информация:",
                             value=f"**Имя:** `{ctx.guild.name}`\n"
                                   f"{emote}**ID:** `{ctx.guild.id}`\n"
                                   f"{emote}**Страна:** `{ctx.guild.region}`\n"
                                   f"**Овнер:** `{ctx.guild.owner.name}`\n"
                                   f"{emote}**ID:** `{ctx.guild.owner.id}`\n"
                                   f"{emote}**Пинг:** `{ctx.guild.owner.mention}`\n"
                                   f"**Создан:** `<t:{round(ctx.guild.created_at.timestamp())}:R>`\n"
                                   f"**Всего участников:** `{guild_members}`\n"
                                   f"**Ролей:** `{guild_roles}`\n"
                                   f"**Каналов:** `{channels}`\n"
                                   f"{emote}**Текстовых:** `{text_channels}`\n"
                                   f"{emote}**Воисы:** `{voice_channels}`", inline=False)
        if data["whitelist"] == []:
            serverinfo.add_field(name="Безопасность сервера: ", value=f"Белый список: -")
        else:
            serverinfo.add_field(name="Безопасность сервера: ", value=f"**Белый список:** \n{result}")
        serverinfo.set_thumbnail(url=ctx.guild.icon_url)
        serverinfo.add_field(name="**――――――――――**", value=f"[АВАТАРКА]({ctx.guild.icon_url})", inline=False)
        serverinfo.set_image(url=ctx.guild.banner_url)
        await ctx.send(embed=serverinfo)

 






def setup(client):
    client.add_cog(General(client))