import disnake ,sqlite3, json
from disnake.ext import commands

class ButtonNator(disnake.ui.View):
	def __init__(self):
		super().__init__()
		self.data = sqlite3.connect('data.sqlite3', timeout=1)
		self.cursor = self.data.cursor()
		self.config = json.load(open('config.json','rb'))
		self.color = int(self.config['color'])
	@disnake.ui.button(label = "Включить", style = disnake.ButtonStyle.blurple, emoji = '♻')
	async def toggle(self, button, inter):
		self.cursor.execute(f"DELETE FROM antibot WHERE guild = {inter.guild.id}")
		self.cursor.execute(f"INSERT INTO antibot VALUES({inter.guild.id})")
		await inter.response.edit_message(embed = disnake.Embed(
				title  = f"{button.emoji} | Включено",
				description = f">>> **Теперь никто из ваших администратор не сможет добавить не верифицированого бота.**",
				color = disnake.Colour.dark_green()
			), view = None)
		self.data.commit()
		button.disabled = True
	@disnake.ui.button(label = "Выключить", style = disnake.ButtonStyle.danger, emoji = '⛔')
	async def disable(self, button, inter):
		print(inter.guild.id)
		self.cursor.execute(f"DELETE FROM antibot WHERE guild = {inter.guild.id}")
		await inter.response.edit_message(embed = disnake.Embed(
				title  = f"{button.emoji} | Выключено",
				description = f">>> **Данная функция больше не будет работат на вашем сервере, пока вы ее не включите.**",
				color = disnake.Colour.dark_green()
			), view = None)
		self.data.commit()
		button.disabled = True


class AntiBot(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 
		self.data = sqlite3.connect('data.sqlite3')
		self.cursor = self.data.cursor()
		self.config = json.load(open('config.json','rb'))
		self.color = self.config['color']
	@commands.Cog.listener()
	async def on_member_join(self, member):
		try:
			check = self.cursor.execute(f"SELECT * FROM antibot WHERE guild = {member.guild.id}")
			entry = await member.guild.audit_logs(action = disnake.AuditLogAction.bot_add, limit = 1).get()
			vv = check.fetchall()[0][0]

			if member.bot and not member.public_flags.verified_bot and entry.user.id != member.guild.owner_id and vv == member.guild.id:
				try:
					await member.ban(reason = 'Подозрительный бот')
				except:
					pass
		except IndexError:
			return


	@commands.Cog.listener()
	async def on_member_remove(self, member):
		try:
			fetch = self.cursor.execute(f"SELECT guild_id FROM leave_ban WHERE guild_id = {member.guild.id}")
			if fetch.fetchone():
				await member.ban(reason = "Покинул сервер")
		except IndexError:
			print(f"Обработчик ошибок: {member.guild.id} ")

	@commands.command(aliases = ['антибот'])
	@commands.cooldown(1, 30, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def antibot(self, ctx):
		buttonTrue = disnake.ui.Button(label = "Включить", style = disnake.ButtonStyle.blurple, emoji = '♻', custom_id = 'toggle')
		buttonFalse = disnake.ui.Button(label = "Выключить", style = disnake.ButtonStyle.danger, emoji = '⛔', custom_id = 'disable')
		view = disnake.ui.View()
		view.add_item(buttonTrue)
		view.add_item(buttonFalse)
		await ctx.send(embed = disnake.Embed(title = ":gear: | AntiBot ",
			description = f">>> `Вы точно хотите включить/выключить данную функцию?` ",
			color = disnake.Colour(self.color)), view = view)
		inter = await self.bot.wait_for('button_click', check = lambda i: i.author == ctx.author)
		if inter.component.custom_id == 'toggle':
			self.cursor.execute(f"DELETE FROM antibot WHERE guild = {inter.guild.id}")
			self.cursor.execute(f"INSERT INTO antibot VALUES({inter.guild.id})")
			await inter.response.edit_message(embed = disnake.Embed(
				title  = f"{inter.component.emoji} | {inter.component.label}",
				description = f">>> **Теперь никто из ваших администраторов не сможет добавить неверифицированного бота.**",
				color = disnake.Colour(self.color)
			), view = None)
			self.data.commit()
		else:
			self.cursor.execute(f"DELETE FROM antibot WHERE guild = {inter.guild.id}")
			await inter.response.edit_message(embed = disnake.Embed(
				title  = f"{inter.component.emoji} | Выключено",
				description = f">>> **Данная функция больше не будет работать на вашем сервере, пока вы ее не включите.**",
				color = disnake.Colour.red()
			), view = None)
			self.data.commit()
			

def setup(bot):
	bot.add_cog(AntiBot(bot))
