import disnake ,re,sqlite3
from disnake.ext import commands
from disnake.ext.commands import Cog


class K(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.data = sqlite3.connect('data.sqlite3', timeout=1)
		self.cursor = self.data.cursor()


	@Cog.listener()
	async def on_message(self, message):
		try:
			link = self.cursor.execute(f"SELECT * FROM antilink WHERE guild = {message.guild.id}")
			guild = link.fetchall()[0][0]
			chan = self.cursor.execute(f"SELECT channel FROM exceptchan WHERE id = {message.guild.id}")
			chan = bool(message.channel.id == chan.fetchall()[0][0])
			if(guild == message.guild.id and not message.author.guild_permissions.administrator and not chan):
				if(re.search("https://", message.content) or re.search("http://", message.content) or re.search("discord.gg/", message.content) ):
					await message.delete()
					await message.author.kick(reason = "Ссылка в чате")
		except IndexError:
			return


def setup(bot):
	bot.add_cog(K(bot))

