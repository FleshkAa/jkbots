import disnake, sqlite3, json
from disnake.ext import commands



class Dev(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.data = sqlite3.connect('data.sqlite3', timeout=1)
		self.cursor = self.data.cursor()
		self.config = json.load(open('config.json','rb'))
		self.color = self.config['color']


	@commands.command()
	@commands.is_owner()
	async def addcrasher(self, ctx, member:disnake.User = None, *, reason = "Крашер"):
		msg = await ctx.send("Проверка личности...")
		self.cursor.execute(f"DELETE FROM blacklist WHERE id = {member.id}")
		self.cursor.execute("INSERT INTO blacklist VALUES(?, ?)", (member.id, reason))
		self.data.commit()
		await msg.edit(content = 'Успешно')

	@commands.command()
	@commands.is_owner()
	async def remcrasher(self, ctx, member:disnake.User = None):
		self.cursor.execute("DELETE FROM blacklist WHERE id = ?", member.id)
		await ctx.send(embed = disnake.Embed(description = f">>> **Пользователь `{member.name}` убран с блеклиста**",
						color = disnake.Colour(self.color)))
		self.data.commit()

	

def setup(bot):
	bot.add_cog(Dev(bot))