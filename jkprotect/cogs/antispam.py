import disnake ,re,sqlite3, asyncio,json
from datetime import datetime
from disnake.ext import commands


class Worker(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.data = sqlite3.connect('data.sqlite3', timeout=1)
		self.cursor = self.data.cursor()
		self.config = json.load(open('config.json','rb'))
		self.color = self.config['color']

	@commands.command(aliases = ['игнорируемый-канал'])
	@commands.cooldown(1, 10, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def ignore_channel(self, ctx, channel:disnake.TextChannel):
		self.cursor.execute(f"DELETE FROM exceptchan WHERE channel = {channel.id}")
		self.cursor.execute("INSERT INTO exceptchan VALUES(?, ?)", (ctx.guild.id, channel.id))
		self.data.commit()
		await ctx.send(embed =disnake.Embed(title = f":gear: | Игнорируемый канал",
			description = f">>> **Теперь постинг ссылок доступны в `{channel.id}`**",
			color = disnake.Colour(self.color)))

	@commands.command(aliases = ['белый-лист'])
	@commands.cooldown(1, 30, commands.BucketType.default)
	@commands.has_permissions(send_messages = True)
	async def whitelisted(self, ctx):
		users = self.cursor.execute(f"SELECT id FROM wl WHERE guild = {ctx.guild.id}").fetchall()
		await ctx.send(
				embed = disnake.Embed(
						title = ":gear: | Пользователи в вайтлисте",
						description = f" ".join(f'> **<@{i[0]}> | `{i[0]}`**\n' for i in users), 
						color = self.color
					)
			)


	@commands.command(aliases = ['запрет-ссылок'])
	@commands.cooldown(1, 30, commands.BucketType.default)
	@commands.has_permissions(send_messages = True)
	async def antilink(self, ctx):
		buttonTrue = disnake.ui.Button(label = "Хочу включить", style = disnake.ButtonStyle.blurple, emoji = '♻', custom_id = 'toggle')
		buttonFalse = disnake.ui.Button(label = "Хочу выключить", style = disnake.ButtonStyle.danger, emoji = '⛔', custom_id = 'disable')
		view = disnake.ui.View()
		view.add_item(buttonTrue)
		view.add_item(buttonFalse)
		await ctx.send(embed = disnake.Embed(title = ":gear: | Запрет ссылок",
			description = f">>> **Данная функция не позволит обычным пользователям публиковать ссылки в чат**",
			color = disnake.Colour(self.color)), view = view)
		inter = await self.bot.wait_for('button_click', check = lambda i: i.author == ctx.author)
		if inter.component.custom_id == 'toggle':
			self.cursor.execute(f"DELETE FROM antilink WHERE guild = {inter.guild.id}")
			self.cursor.execute(f"INSERT INTO antilink VALUES({inter.guild.id})")
			await inter.response.edit_message(embed = disnake.Embed(title = f"{inter.component.emoji} | Включено",
			description = f">>> **Включено. **", color = disnake.Colour(self.color)), view = None)
			self.data.commit()
		else:
			self.cursor.execute(f"DELETE FROM antilink WHERE guild = {inter.guild.id}")
			await inter.response.edit_message(embed = disnake.Embed(title = f"{inter.component.emoji} | Выключено",
			description = f">>> **Выключено. **", color = disnake.Color.red()), view = None)
			self.data.commit()

	@commands.command(aliases = ['бан-новых-пользователей'])
	@commands.cooldown(1, 30, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def auto_reg_ban(self, ctx, days:int = 30):
		self.cursor.execute(f"DELETE FROM new_users WHERE guild_id = {ctx.guild.id}")
		self.cursor.execute("INSERT INTO new_users VALUES(?, ?)", (ctx.guild.id, days))
		await ctx.send(embed = disnake.Embed(title = ":gear: | Включено",
			description = f'>>> **Функция включена. Теперь если на ваш сервер зайдёт пользователь, регистрация которого меньше `{days}` дней получит бан**',
			color = disnake.Colour(self.color)))
		self.data.commit()

	@commands.Cog.listener()
	async def on_member_join(self, member):
		try:
			fetch = self.cursor.execute(f"SELECT days FROM new_users WHERE guild_id = {member.guild.id}")
			if fetch:
				days = fetch.fetchone()[0]
				if time.time() - member.created_at.timestamp() < 3600 * 24 * days:
					await member.ban(reason = f'Пользователь зарегистрирован {round(int(member.created_at.timestamp() / 3600 /24))} дней. А требуется {days}')
		except IndexError:
			return




def setup(bot):
	bot.add_cog(Worker(bot))

