import os
import discord
from discord.ext import commands, tasks
from asyncio import sleep
from discord.utils import get
import random
import asyncio
import json
import sys
from discord.utils import find
import datetime
from Tools.utils import getConfig, getGuildPrefix, updateConfig
from Tools.logMessage import sendLogMessage
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.emojis = True
intents.webhooks = True
intents = intents


class AntiNuke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        try:
            data = getConfig(guild.id)
            if data["antinuke"] is True:
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                owner = data["owner"]
                logChannel = data["logChannel"]

                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.ban).flatten()
                logs = logs[0]
                logs.target = member
                reason = "Безопасность сервера Блокировка участника как пользователя, не внесенного в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == owner:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if punishment == "ban":
                    punishment = "banned"
                    try:
                        await logs.user.ban(reason=reason)

                    except:
                        pass
                if punishment == "kick":
                    punishment = "kicked"
                    try:
                        await logs.user.kick(reason=reason)
                    except:
                        pass
                if punishment == "none":
                    return

                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been kicked", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"{reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=member, embed=embed, channel=logChannel)
        except:
            pass


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            data = getConfig(member.guild.id)
            if data["antinuke"] is True:
                guild = member.guild
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                logChannel = data["logChannel"]
                owner = data["owner"]
                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.kick).flatten()
                logs = logs[0]
                reason = "Удаление участника как пользователя, не внесенного в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if logs.user.id == owner:
                    return

                if punishment == 'ban':
                    punishment = "banned"
                    try:
                        await logs.user.ban(reason=f"Безопасность сервера  | {reason}")
                    except:
                        pass
                if punishment == 'kick':
                    punishment = "kicked"
                    try:
                        await logs.user.kick(reason=f"Безопасность сервера| {reason}")
                    except:
                        pass
                if punishment == "none":
                    return
                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been kicked", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"Server Security Anti-Nuke | {reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=member, embed=embed, channel=logChannel)
        except:
            pass

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        try:
            data = getConfig(channel.guild.id)
            if data["antinuke"] is True:
                guild = channel.guild
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                owner = data["owner"]
                logChannel = data["logChannel"]

                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.channel_create).flatten()
                logs = logs[0]
                reason = "Канал создан как пользователь, не внесенный в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == owner:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if punishment == 'ban':
                    punishment = "banned"
                    try:
                        await logs.user.ban(reason=f"Безопасность сервера | {reason}")
                        await channel.delete()
                    except:
                        pass
                if punishment == 'kick':
                    punishment = "kicked"
                    try:
                        await logs.user.kick(reason=f"Безопасность сервера | {reason}")
                        await channel.delete()
                    except:
                        pass
                if punishment == "none":
                    await channel.delete()
                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been {punishment}", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"Server Security Anti-Nuke | {reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=channel, embed=embed, channel=logChannel)
        except:
            pass

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        try:
            data = getConfig(channel.guild.id)
            if data["antinuke"] is True:
                guild = channel.guild
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                owner = data["owner"]
                logChannel = data["logChannel"]

                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.channel_delete).flatten()
                logs = logs[0]
                reason = "Канал удален как пользователь, не внесенный в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if logs.user.id == owner:
                    return

                if punishment == 'ban':
                    punishment = "banned"
                    try:
                        await logs.user.ban(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == 'kick':
                    punishment = "kicked"

                    try:
                        await logs.user.kick(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == "none":
                    return
                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been kicked", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"Server Security Anti-Nuke | {reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=channel, embed=embed, channel=logChannel)
        except:
            pass

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        try:
            data = getConfig(role.guild.id)
            if data["antinuke"] is True:
                guild = role.guild
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                owner = data["owner"]
                logChannel = data["logChannel"]

                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.role_delete).flatten()
                logs = logs[0]
                reason = "Роль удалена как пользователь, не внесенный в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if logs.user.id == owner:
                    return

                if punishment == 'ban':
                    punishment = "banned"

                    try:
                        await logs.user.ban(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == 'kick':
                    punishment = "kicked"

                    try:
                        await logs.user.kick(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == "none":
                    return
                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been {punishment}", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"Server Security Anti-Nuke | {reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=role, embed=embed, channel=logChannel)
        except:
            pass

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        try:
            data = getConfig(role.guild.id)
            if data["antinuke"] is True:
                guild = role.guild
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                owner = data["owner"]
                logChannel = data["logChannel"]

                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.role_create).flatten()
                logs = logs[0]
                reason = "Роль создана как пользователь, не внесенный в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if logs.user.id == owner:
                    return

                if logs.user.bot:
                    return

                if punishment == 'ban':
                    punishment = "banned"
                    try:
                        await logs.user.ban(reason=f"Безопасность сервера | {reason}")
                        await role.delete()
                    except:
                        pass
                if punishment == 'kick':
                    punishment = "kicked"

                    try:
                        await logs.user.kick(reason=f"Безопасность сервера| {reason}")
                        await role.delete()
                    except:
                        pass
                if punishment == "none":
                    await role.delete()
                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been {punishment}", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"Server Security Anti-Nuke | {reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=role, embed=embed, channel=logChannel)
        except:
            pass

 
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        try:
            data = getConfig(channel.guild.id)
            if data["antinuke"] is True:
                guild = channel.guild
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                owner = data["owner"]
                logChannel = data["logChannel"]

                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.webhook_create).flatten()
                logs = logs[0]
                reason = "Создание вебхука от имени пользователя, не внесенного в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if logs.user.id == owner:
                    return

                if punishment == 'ban':
                    punishment = "banned"
                    try:
                        await logs.user.ban(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == 'kick':
                    punishment = "kicked"

                    try:
                        await logs.user.kick(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == "none":
                    return
                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been kicked", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"Server Security Anti-Nuke | {reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=channel, embed=embed, channel=logChannel)
        except:
            pass

    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        try:
            data = getConfig(channel.guild.id)
            if data["antinuke"] is True:
                guild = channel.guild
                data = getConfig(guild.id)
                whitelisted = data["whitelist"]
                punishment = data["punishment"]
                owner = data["owner"]
                logChannel = data["logChannel"]

                logs = await guild.audit_logs(limit=3, action=discord.AuditLogAction.webhook_delete).flatten()
                logs = logs[0]
                reason = "Удалить вебхук как пользователь, не внесенный в белый список"

                if logs.user.id in whitelisted:
                    return

                if logs.user.id == 882901345466724373:
                    return

                if logs.user.id == owner:
                    return

                if punishment == 'ban':
                    punishment = "banned"
                    try:
                        await logs.user.ban(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == 'kick':
                    punishment = "kicked"

                    try:
                        await logs.user.kick(reason=f"Безопасность сервера | {reason}")
                    except:
                        pass
                if punishment == "none":
                    return
                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{logs.user} has been kicked", color=discord.Colour.blue())
                embed.add_field(name="Reason", value=f"Server Security Anti-Nuke | {reason}", inline=False)
                embed.add_field(name="User ID", value=f'{logs.user.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>", inline=False)
                embed.set_thumbnail(url=logs.user.avatar_url)
                await sendLogMessage(self, event=channel, embed=embed, channel=logChannel)
        except:
            pass




def setup(client):
    client.add_cog(AntiNuke(client))