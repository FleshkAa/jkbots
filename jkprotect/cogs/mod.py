import disnake

from disnake.ext import commands

import sqlite3

import json

import re 

import datetime

from typing import Union


def timecvtr(time=0):
	tl = re.split('(\d+)', time)
	if tl[2] == 's' or 'с':
		tm = int(tl[1])
	if tl[2] in ['m', 'min', 'м', 'мин']:
		tm = int(tl[1] * 60)
	if tl[2] == 'h' or 'ч':
		tm = int(tl[1] * 3600)
	if tl[2] == 'd' or 'д':
		tm = int(tl[1] * 3600 * 60)
	else:
		tm = ''
	return int(tm)


class Program(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.data = sqlite3.connect('data.sqlite3', timeout=1)
		self.cursor = self.data.cursor()
		self.config = json.load(open('config.json', 'rb'))
		self.color = int(self.config['color'])

	@commands.command(aliases = ['сервер'])
	@commands.cooldown(1, 10, commands.BucketType.default)
	async def server_info(self, ctx):
		embed = disnake.Embed(
			title=f":basketball: | {ctx.guild.name}",
			description=f"""				 
**Название: `{ctx.guild.name}` | `{ctx.guild.id}`
Участников: `{ctx.guild.member_count}`
Каналов: `{len(ctx.guild.channels)}`
Ролей: `{len(ctx.guild.roles)}`
Эмодзи `{len(ctx.guild.emojis)}`
Стикеров: `{len(ctx.guild.stickers)}`
Владелец: `{ctx.guild.owner}` | `{ctx.guild.owner_id}`
Дата создания сервера: `{ctx.guild.created_at.strftime('%d/%m/%y | %H:%M:%S')}` | `{ctx.guild.owner_id}`
Уровень 2х-тапной аунтификации: `{ctx.guild.mfa_level}`
Бустов: `{ctx.guild.premium_subscription_count}`**""",
			timestamp=datetime.datetime.utcnow(),
			color=disnake.Colour(self.color)
		)
		embed.set_thumbnail(url=ctx.guild.icon)
		await ctx.send(
			embed=embed
		)

	@commands.command(aliases = ['ливбан'])
	@commands.cooldown(1, 15, commands.BucketType.default)
	@commands.has_permissions(administrator=True)
	async def leaveban(self, ctx):
		view = disnake.ui.View()
		view.add_item(disnake.ui.Button(label="Включить", emoji="♻", custom_id='toggle', style=disnake.ButtonStyle.green))
		view.add_item(disnake.ui.Button(label="Выключить", emoji="⛔", custom_id='disable', style=disnake.ButtonStyle.danger))
		msg = await ctx.send(
			embed=disnake.Embed(
				title=':gear: | leaveban',
				description=f">>> **Если вы включите данную функцию, то участнику при выходе с сервера выдадут бан.**",
				color=disnake.Colour(self.color)),
			view=view)
		inter = await self.bot.wait_for('button_click', check=lambda i: i.author == ctx.author)
		if inter.component.custom_id == 'toggle':
			await msg.edit(
					embed=disnake.Embed(
							title=f'♻ | Включено',
							description=f">>> **Теперь если пользователь покинет сервер, ему автоматически прилетит `бан`**",
							color=disnake.Colour.green()
						), view=None
					)
			self.cursor.execute(f"DELETE FROM leave_ban WHERE guild_id = {ctx.guild.id}")
			self.cursor.execute(f"INSERT INTO leave_ban VALUES({ctx.guild.id})")
		else:
			await msg.edit(
					embed=disnake.Embed(
							title='⛔ | Выключено',
							description=f">>> Данная функция была выключена",
							color=disnake.Colour.red()
						), view=None
				)
			self.cursor.execute("DELETE FROM leave_ban WHERE guild = ?", ctx.guild.id)
		self.data.commit()
	@commands.command()
	@commands.has_permissions(administrator = True)
	@commands.cooldown(1, 5, commands.BucketType.default)
	async def cooldown(self, ctx, seconds:int = 2):
		await ctx.channel.edit(
					slowmode_delay = seconds
				)
		await ctx.send(
				embed= disnake.Embed(
						title = ":gear: | Задержка",
						description= f">>> **`{ctx.author.name}` изменил задержку чата на `{seconds}` секунд**",
						color = disnake.Colour(self.color)
					)
			)
	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.default)
	@commands.has_permissions(administrator=True)
	async def lock(self, ctx):
		for role in ctx.guild.roles:
			try:
				await ctx.channel.set_permissions(role, send_messages = False)
			except:
				continue
		await ctx.send(
				embed = disnake.Embed(
						title = ":gear: | Чат закрыт",
						description =f">>> *Скрекотание сверчков..",
						color = disnake.Colour(self.color)
					)
			)
	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.default)
	@commands.has_permissions(administrator=True)
	async def unlock(self, ctx):
		for role in ctx.guild.roles:

			try:

				await ctx.channel.set_permissions(role, send_messages = True)

			except:
				continue
		await ctx.send(
				embed = disnake.Embed(
						title = ":gear: | Чат Открыт",
						description =f">>> **Теперь участники сервера имеют право в него писать**",
						color = disnake.Colour(self.color)
					)
			)

	@commands.command(aliases = ['бан'])
	@commands.cooldown(1, 5, commands.BucketType.default)
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: disnake.Member = None, *, reason=None):
		if member:
			if type(member) == disnake.Member and member.top_role.position < ctx.author.top_role.position:
				await ctx.guild.ban(member, reason=reason)
				embed = disnake.Embed(
					title=":hammer: | Banned",
					description=f">>> **Пользователь: `{member}` | `{member.id}`**\n**Причина бана: `{reason}`**",
					color=disnake.Colour(self.color)
				)
				await ctx.message.add_reaction('✅')
				await ctx.send(embed=embed)
			if type(member) == disnake.User:
				await ctx.guild.ban(member, reason=reason)
				embed = disnake.Embed(
					title=":hammer: | Banned",
					description=f">>> **Пользователь: `{member}` | `{member.id}`**\n**Причина бана: `{reason}`**",
					color=disnake.Colour(self.color)
				)
				await ctx.message.add_reaction('✅')
				await ctx.send(embed=embed)

	@commands.command(aliases = ['кик'])
	@commands.cooldown(1, 5, commands.BucketType.default)
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: disnake.Member = None, *, reason=None):
		if member and member.top_role.position < ctx.author.top_role.position:
			await ctx.guild.ban(member, reason=reason)
			embed = disnake.Embed(
					title=":hammer: | Kicked",
					description=f">>> **Имя пользователя: `{member.name}` | `{member.id}`**\n**Причина: `{reason}`**",
					color=disnake.Colour(self.color)
				)
			await ctx.send(embed=embed, delete_after=10)
			await ctx.message.add_reaction('✅')
		else:
			await ctx.send(f"```{ctx.prefix}{ctx.command} <member> [reason]```", delete_after=10)

	@commands.command(aliases = ['разбан'])
	@commands.cooldown(1, 2, commands.BucketType.default)
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, m: disnake.User = None):
		if m:
			try:
				await ctx.guild.unban(m)

				await ctx.message.add_reaction('✅')
			except disnake.NotFound:
				return await ctx.send(
					embed=disnake.Embed(
						title="<:check_red:869597768526729228> | Ошибка",
						description=f">>> **Пользователь не забанен**",
						color=disnake.Colour.red()
					)
				)
			await ctx.send(embed=disnake.Embed(
				title=f":white_check_mark:  | {m.display_name}",
				description=f">>> **Пользователь `{ctx.message.author.name}` | `{ctx.author.id}` разбанил `{m.name}` | `{m.id}`**",
				color=disnake.Colour.green()))
		else:
			await ctx.send(f"```{ctx.prefix}{ctx.command} <member> [reason]```", delete_after=10)

	@commands.command(aliases = ['очистить'])
	@commands.cooldown(1, 3, commands.BucketType.default)
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=1):
		await ctx.channel.purge(limit=amount)
		await ctx.send(embed=disnake.Embed(
			title=":white_check_mark: | Очистить",
			description=f">>> **Очистил `{amount}` сообщений.** ",
			color=disnake.Colour.green()), delete_after=10)


	@commands.command(aliases = ['мут'])
	@commands.cooldown(1, 3, commands.BucketType.default)
	@commands.has_permissions(moderate_members = True)
	async def mute(self, ctx, member: disnake.Member = None, reason=None):
		member = disnake.Object(member) if type(member) != disnake.Member else member
		if member:
			view = disnake.ui.View()
			for a, b, c in zip(['1m', '5m', '10m', 'Hour', 'Day', 'Week'], [1,5,10,60,60 * 24, 60 * 7 * 24],['🕐', '🕞', '🕖', '🕤', '🕥', '🕦']):
				view.add_item(disnake.ui.Button(label=f"{a}", style=disnake.ButtonStyle.blurple, emoji=f'{c}', custom_id = f"{b}"))

			message = await ctx.send(embed=disnake.Embed(description=f">>> **Насколько мне замутить пользователя: **",color = disnake.Colour(self.color)), view = view)
			inter = await self.bot.wait_for('button_click', check=lambda i: i.author == ctx.author)
			time = datetime.timedelta(minutes=int(inter.component.custom_id))
			try:
				await member.timeout(duration=time, reason=reason)
			except disnake.Forbidden:
				return await ctx.send(
					embed=disnake.Embed(
						title="<:check_red:869597768526729228> | Ошибка",
						description=f">>> **Бот не может замутить данного пользователя из-за недостатка прав**",
						color=disnake.Colour.red()
					)
				)

			await message.delete()
			await ctx.send(embed=disnake.Embed(title = '<:check:869597763736862800> | Мут',
					description=f">>> **Пользователь `{ctx.author.name}` замутил `{member.name}` на `{inter.component.label}`**",
					color=disnake.Colour.green()))
		else:
			await ctx.send(f"```{ctx.prefix}{ctx.command} <member>```", delete_after=10)


	@commands.command(aliases = ['размут'])
	@commands.cooldown(1, 3, commands.BucketType.default)
	@commands.has_permissions(manage_messages = True)
	async def unmute(self, ctx, member: disnake.Member = None):
		if member:
			member = disnake.Object(member) if type(member) == int else member
			await member.timeout(until = datetime.datetime.utcnow())
			await ctx.send(embed = disnake.Embed(title='🙊 | Размут',
				description=f">>> **Пользователь `{ctx.author.name}` снял ограничения с `{member.name}`**",
				color=disnake.Colour(self.color)), delete_after=20)


	@commands.command(aliases = ['пред'])
	@commands.cooldown(1, 3, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def warn(self, ctx, member: disnake.User = None, reason=None):
		if member:
			self.cursor.execute(f"INSERT INTO warns VALUES({ctx.guild.id}, {member.id})")
			lol = self.cursor.execute(f"SELECT * FROM warns where mem = {member.id} AND guild = {ctx.guild.id}")
			print(f"Warns: {len(lol.fetchall())}")
			self.data.commit()
			await ctx.send(embed = disnake.Embed(title = f"{member}",
				description = f">>> **Пользователь `{ctx.author.name}` дал предупреждение `{member.name}`**",
				color = disnake.Colour(self.color)
				))


	@commands.command(aliases = ['снять-преды'])
	@commands.cooldown(1, 3, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def unwarns(self, ctx, member: disnake.User = None):
		if member:
			self.cursor.execute('DELETE FROM warns WHERE mem={mid} AND guild = {guild}'.format(mid = member.id, guild = ctx.guild.id))
			self.data.commit()
			await ctx.send(embed = disnake.Embed(title = "Снятие предупреждений",
				description = f">>> **С пользователя `{member.name}` | `{member.id}` сняты все предупреждения.**",
				color = disnake.Colour(self.color)
				),
			delete_after = 15
			)
	@commands.command(aliases = ['преды'])
	@commands.cooldown(1, 3, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def warns(self, ctx, member: disnake.User = None):
		member=ctx.author.id if not member else member.id

		lol = self.cursor.execute(f"SELECT * FROM warns where mem = {member} AND guild = {ctx.guild.id}")
		await ctx.send(embed = disnake.Embed(title = f'{member}',description = f">>> **Пользователь имеет  `{len(lol.fetchall())}` предупреждений**",
			color = disnake.Colour(self.color)))
	@commands.command(aliases = ['автороль'])
	@commands.cooldown(1, 30, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def autorole(self, ctx, role: disnake.Role):
		self.cursor.execute("DELETE FROM autorole WHERE id = ? AND role_id = ?", (ctx.guild.id, role.id))
		self.cursor.execute("INSERT INTO autorole VALUES(?, ?)", (ctx.guild.id, role.id))
		await ctx.send(embed = disnake.Embed(title = f":gear: | Отлично",
			description = f">>> **Теперь каждому новому пользователю, будет выдана роль `{role.name}`**",
			color = disnake.Colour(self.color)))
		self.data.commit()
	@commands.Cog.listener()
	async def on_member_join(self, member):
		try:
			fetch = self.cursor.execute(f"SELECT role_id FROM autorole WHERE id = {member.guild.id}")
			role_id = fetch.fetchall()[0][0]
			role = member.guild.get_role(role_id)
			await member.add_roles(role)
		except IndexError:
			return

	@commands.command(aliases = ['масбан'])
	@commands.cooldown(1, 60, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def massban(self, ctx, mems:commands.Greedy[disnake.User], reason = None): 
		for member in mems:
			await ctx.guild.ban(member,reason = reason)
		await ctx.send(embed = disnake.Embed(description = f">>> **Забанил `{len(mems)}` пользователей**", color = disnake.Colour(self.color)))

	@commands.command(aliases = ['снять-пред'])
	@commands.cooldown(1, 3, commands.BucketType.default)
	@commands.has_permissions(administrator = True)
	async def unwarn(self, ctx,  member: disnake.User):
		if member:
			ifable = self.cursor.execute('SELECT * From warns WHERE mem = {m} AND guild = {guild}'.format(m = member.id, guild = ctx.guild.id))
			if ifable:
				ifable.fetchall()[1] -= 1
				await ctx.message.add_reaction("✅")
			else:
				await ctx.send(embed=disnake.Embed(title = ":gear: | Пред",
					description = f">>> **У `{member.name}` нет предупреждений**", color=disnake.Colour(self.color)))


def setup(bot):
	bot.add_cog(Program(bot))
