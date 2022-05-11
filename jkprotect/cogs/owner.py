import disnake as discord
import sqlite3, json
from disnake.ext import commands


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = json.load(open('config.json','rb'))
		self.color = self.config['color']

	@commands.command(aliases = ['удал-спам-роли'])
	@commands.has_permissions(administrator = True)
	async def delspamroles(self, ctx):
		if int(ctx.author.id == ctx.guild.owner_id):
			list = []
			for channel in ctx.guild.roles:
				if channel.name in list:
					await channel.delete()
				else:
					list.append(channel.name)
			await ctx.send(embed = discord.Embed(description = ">>> **Выполнено**", color = discord.Colour(self.color)))
	@commands.command(aliases = ['удал-спам-каналы'])
	@commands.cooldown(1, 30, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def delspamchannels(self, ctx):
		list = []
		if int(ctx.author.id == ctx.guild.owner_id):
			for channel in ctx.guild.channels:
				if channel.name in list:
					await channel.delete()
				else:
					list.append(channel.name)
			await ctx.send(embed = discord.Embed(description = ">>> **Выполнено**", color = discord.Colour(self.color)))

def setup(bot):
	bot.add_cog(Owner(bot))
