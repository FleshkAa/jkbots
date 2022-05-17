import discord

from discord.ext import commands
from discord.utils import get
from Tools.utils import getConfig, getGuildPrefix, guild_owner_only, updateConfig


class onJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        data = getConfig(member.guild.id)

        for i in data["joinroles"]:
            getroles = get(member.guild.roles, id=i)
            await member.add_roles(getroles)


def setup(client):
    client.add_cog(onJoin(client))