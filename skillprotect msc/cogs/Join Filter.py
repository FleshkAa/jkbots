import discord
from discord.ext import commands
from Tools.utils import getConfig, getGuildPrefix, updateConfig
from datetime import datetime
from Tools.logMessage import sendLogMessage


class AntiRaid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        data = getConfig(member.guild.id)
        punishment = data["punishment"]
        logChannel = data["logChannel"]
        if data["joinfilter"] is True:
            if data["botfilter"] is True:
                if member.bot:
                    if punishment == "kick":
                        punishment = "kicked"
                        await member.kick(reason=f"Фильтр присоединения безопасности сервера | Бот присоединился к серверу")

                    if punishment == "ban":
                        punishment = "banned"
                        await member.ban(reason=f"Фильтр присоединения безопасности сервера | Бот присоединился к серверу")

                    if punishment == "none":
                        pass

                    time = datetime.datetime.now()
                    now = round(time.timestamp())
                    embed = discord.Embed(title=f"{member} был {punishment}", color=discord.Colour.blue())
                    embed.add_field(name="причина", value=f"Фильтр присоединения безопасности сервера | Бот присоединился к серверу", inline=False)
                    embed.add_field(name="Дата", value=f"<t:{now}:F>\n", inline=False)
                    embed.set_thumbnail(url=member.avatar_url)
                    await sendLogMessage(self, event=member, embed=embed, channel=logChannel)

                else:
                    pass

            if data["avatarfilter"] is True:
                if member.avatar == None:
                    if punishment == "kick":
                        punishment = "kicked"
                        await member.kick(reason="Фильтр присоединения безопасности сервера | У пользователя нет собственного аватара")
                        try:
                            await member.send("Фильтр присоединения безопасности сервера | Вам нужно собственное изображение профиля, чтобы присоединиться к серверу!")
                        except discord.errors.Forbidden:
                            return
                    if punishment == "ban":
                        punishment = "banned"
                        await member.ban(reason="Фильтр присоединения безопасности сервера | У пользователя нет собственного аватара")
                        try:
                            await member.send("Фильтр присоединения безопасности сервера | Вам нужно собственное изображение профиля, чтобы присоединиться к серверу!")
                        except discord.errors.Forbidden:
                            return
                    if punishment == "none":
                        pass

                    time = datetime.datetime.now()
                    now = round(time.timestamp())
                    embed = discord.Embed(title=f"{member} БЫЛ {punishment}", color=discord.Colour.blue())
                    embed.add_field(name="ПРИЧИНА", value=f"Фильтр присоединения безопасности сервера | У пользователя нет собственного аватара", inline=False)
                    embed.add_field(name="ДАТА", value=f"<t:{now}:F>\n", inline=False)
                    embed.set_thumbnail(url=member.avatar_url)
                    await sendLogMessage(self, event=member, embed=embed, channel=logChannel)
                else:
                    pass

            if data["autoban"] is True:
                await member.ban(reason="Безопасность сервера | Автобан")

                time = datetime.datetime.now()
                now = round(time.timestamp())
                embed = discord.Embed(title=f"{member} был забанен", color=discord.Colour.blue())
                embed.add_field(name="причина", value=f"Фильтр присоединения безопасности сервера | Автобан",
                                inline=False)
                embed.add_field(name="дата", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                await sendLogMessage(self, event=member, embed=embed, channel=logChannel)

            if data["checknew"] is True:
                maxpoints = data["points"]
                points = 0
                member_days = (datetime.utcnow() - member.created_at).days
                if member_days <= 5:
                    points += 30
                elif member_days <= 15:
                    points += 20
                elif member_days <= 30:
                    points += 10
                elif member_days <= 80:
                    points += 5
                url = member.avatar_url
                if "/embed/" in str(url).lower():
                    points += 15
                if "gg/" in member.name:
                    points += 30
                if points >= int(maxpoints):
                    if punishment == 'kick':
                        punishment = 'kicked'
                        await member.kick(reason="Фильтр присоединения безопасности сервера | Этот пользователь набрал минимальное количество баллов и был выкинут с сервера.")

                        time = datetime.utcnow()
                        now = round(time.timestamp())
                        embed = discord.Embed(title=f"{member} был {punishment}", color=discord.Colour.blue())
                        embed.add_field(name="Reason", value=f"Фильтр присоединения безопасности сервера | Этот пользователь набрал минимальное количество зпходов",
                                        inline=False)
                        embed.add_field(name="макс присоединений", value=f"{maxpoints}", inline=False)
                        embed.add_field(name="присоединений", value=f"{points}", inline=False)
                        embed.add_field(name="дата", value=f"<t:{now}:F>\n", inline=False)
                        embed.set_thumbnail(url=member.avatar_url)
                        await sendLogMessage(self, event=member, embed=embed, channel=logChannel)

                    if punishment == 'ban':
                        punishment = 'banned'
                        await member.ban(reason="Фильтр присоединения безопасности сервера | Этот пользователь набрал минимальное количество присоединений и был забанен на сервере.")

                        time = datetime.utcnow()
                        now = round(time.timestamp())
                        embed = discord.Embed(title=f"{member} был {punishment}", color=discord.Colour.blue())
                        embed.add_field(name="причина",
                                        value=f"Фильтр присоединения безопасности сервера | Этот пользователь набрал минимальное количество присоединений и был забанен на сервере.",
                                        inline=False)
                        embed.add_field(name="макс пресоединений", value=f"{maxpoints}", inline=False)
                        embed.add_field(name="присоединений", value=f"{points}", inline=False)
                        embed.add_field(name="дата", value=f"<t:{now}:F>\n", inline=False)
                        embed.set_thumbnail(url=member.avatar_url)
                        await sendLogMessage(self, event=member, embed=embed, channel=logChannel)

                    if punishment == 'none':
                        punishment = 'kicked'
                        await member.kick(reason="Фильтр присоединения безопасности сервера | Этот пользователь набрал минимальное количество присоединений и был забанен на сервере")

                        time = datetime.datetime.now()
                        now = round(time.timestamp())
                        embed = discord.Embed(title=f"{member} has been {punishment}", color=discord.Colour.blue())
                        embed.add_field(name="Reason",
                                        value=f"Фильтр присоединения безопасности сервера | Этот пользователь набрал минимальное количество присоединений и был забанен на сервере.",
                                        inline=False)
                        embed.add_field(name="Maximal Points", value=f"{maxpoints}", inline=False)
                        embed.add_field(name="Points", value=f"{points}", inline=False)
                        embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                        embed.set_thumbnail(url=member.avatar_url)
                        await sendLogMessage(self, event=member, embed=embed, channel=logChannel)










def setup(client):
    client.add_cog(AntiRaid(client))