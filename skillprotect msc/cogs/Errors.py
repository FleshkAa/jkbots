import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CommandNotFound, BotMissingPermissions, MissingRequiredArgument
from Tools.utils import getGuildPrefix


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        prefix = await getGuildPrefix(self.client, ctx)
        if isinstance(error, commands.CommandOnCooldown):
            minute = round(error.retry_after)
            if minute > 0:
                await ctx.send("Перезарядка команды: {0} секунд!".format(minute))

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=" :x: Неправильное использование",
                                  description=f"`{prefix}{ctx.command.name} {ctx.command.usage}`", colour=discord.Colour.Red())
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            emote = (":x:")
            await ctx.send(f"У вас должна быть более высокая роль, чтобы использовать эту команду {emote}")

        if isinstance(error, commands.MemberNotFound):
            emote = (":x:")
            await ctx.send(f"Участник не найден {emote}")

        if isinstance(error, commands.RoleNotFound):
            emote = (":x:")
            await ctx.send(f"Роль не найдена {emote}")

        if isinstance(error, commands.BotMissingPermissions):
            emote = (":x:")
            await ctx.send(f"Отсутствуют некоторые важные разрешения, проверьте, есть ли у Skill Protect права администратора {emote}")




def setup(client):
    client.add_cog(Errors(client))