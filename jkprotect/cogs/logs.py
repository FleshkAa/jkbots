import sqlite3
import disnake as disnake
from datetime import datetime

from disnake import Embed
from disnake.ext.commands import Cog
from disnake.ext.commands import command


class Log(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.data = sqlite3.connect('data.sqlite3', timeout=1)
		self.cursor = self.data.cursor()
		self.color = 0x71368a
  

	async def logsend(self,guild,embed):
		log_channel = self.cursor.execute("SELECT id FROM channel WHERE guild = {}".format(guild))
		log_channel = log_channel.fetchall()
		try:
			await self.bot.get_channel(log_channel[0][0]).send(embed=embed)
		except:
			pass


	@Cog.listener()
	async def on_member_update(self, before, after):
		if before.display_name != after.display_name:
			embed = Embed(
						  colour=disnake.Colour.blue(),
						  timestamp=datetime.utcnow())
			embed.set_author(
				name = f"Пользователь изменил ник на сервере",
				icon_url='https://media.discordapp.net/attachments/686585233339842572/708784107458396210/member_gray_plus_green.png'
			)
			embed.add_field(
				name = f"Старый ник",
				value = f">>> `{before.display_name}`",
				inline = False
			)
			embed.add_field(
				name = f"Новый ник",
				value = f">>> `{after.display_name}`",
				inline = False
			)
			await self.logsend(after.guild.id,embed)

		elif before.roles != after.roles:
			embed = Embed(
						  timestamp=datetime.utcnow())
			title = ""
			url = ""
			text = ''
			if len(before.roles) < len(after.roles):
				embed.colour = disnake.Colour.green()
				title = f"Участнику выдали роль"
				url ="https://media.discordapp.net/attachments/686585233339842572/708784127486328923/member_gray_role_green.png"
				text = f"{[role.mention for role in after.roles if role not in before.roles][0]}"
			else:
				embed.colour = disnake.Colour.red()
				title = f"С Участника сняли роль"
				url ="https://media.discordapp.net/attachments/686585233339842572/708784133111021739/member_gray_role_red.png"
				text =f"{[role.mention for role in before.roles if not role in after.roles][0]}"
			embed.set_author(
				name = title,
				icon_url = url
			)
			embed.add_field(
				name = f"Пользователь",
				value = f"{after.mention} | `{after.id}`",
				inline = True
			)
			embed.add_field(
				name = f"Роль",
				value = text,
				inline = True
			)

			await self.logsend(after.guild.id,embed)

	@Cog.listener()
	async def on_message_edit(self, before, after):
		if not after.author.bot:
			if before.content != after.content:
				embed = Embed(
							  colour=disnake.Colour.yellow(),
							  timestamp=datetime.utcnow())
				embed.set_author(
					name=f"Сообщение изменено",
					icon_url='https://media.discordapp.net/attachments/686585233339842572/708866326713598033/message_gray_update_yellow.png'
				)
				embed.add_field(
					name=f"Пользователь",
					value=f"{after.author.mention} **| `{after.author.id}`**",
					inline=True
				)
				embed.add_field(
					name=f"Канал",
					value=f"{after.channel.mention} | `{after.channel.id}`",
					inline=True
				)
				embed.add_field(
					name=f"Сообщение",
					value=f"[Перейти](https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id})",
					inline=True
				)
				embed.add_field(
					name = f"Сообщение до",
					value = f">>> **`{before.content}`**",
					inline = False
				)
				embed.add_field(
					name = f"Сообщение после",
					value = f">>> **`{after.content}`**",
					inline = False
				)
				await self.logsend(after.guild.id,embed)

	@Cog.listener()
	async def on_message_delete(self, message):
		if not message.author.bot:
			embed = Embed(
						  colour=disnake.Colour.red(),
						  timestamp=datetime.utcnow())
			embed.set_author(
				name = f"Сообщение было удалено",
				icon_url = 'https://media.discordapp.net/attachments/686585233339842572/708784170729472080/message_gray_minus_red.png'
			)
			embed.add_field(
				name = f"Автор",
				value = f"{message.author.mention} **| `{message.author.id}`**",
				inline = True
			)
			embed.add_field(
				name = f"Канал",
				value = f"{message.channel.mention} | `{message.channel.id}`",
				inline = True
			)

			embed.add_field(
				name = f"Содержимое",
				value = f'>>> **`{message.content}`**',
				inline = False
			)
			await self.logsend(message.guild.id,embed)
	@Cog.listener()
	async def on_guild_channel_create(self, channel):
		entry = await channel.guild.audit_logs(action  = disnake.AuditLogAction.channel_create, limit = 1).get()
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.green()
			)
		embed.set_author(
			name = f" Был создан канал",
			icon_url ="https://media.discordapp.net/attachments/686585233339842572/708784667989377174/text_gray_plus_green.png"
		)
		embed.add_field(
			name = f"Канал",
			value = f"{channel.mention} | `{channel.id}`",
			inline = True
		)
		embed.add_field(
			name = f"Создал",
			value = f"`{entry.user.name}` | `{entry.user.id}`",
			inline = True
		)
		await self.logsend(channel.guild.id,embed)
	@Cog.listener()
	async def on_guild_channel_delete(self, channel):
		entry = await channel.guild.audit_logs(action  = disnake.AuditLogAction.channel_delete, limit = 1).get()
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.red())
		embed.set_author(
			name = f"Удален канал",
			icon_url = 'https://media.discordapp.net/attachments/686585233339842572/708784664210309141/text_gray_minus_red.png'
		)
		embed.add_field(
			name = f"Канал",
			value = f"**`{channel.name}` | `{channel.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Дата создания",
			value =f"**`{channel.created_at.strftime('%d/%m/%y | %H:%M:%S')}`**",
			inline = True
		)
		embed.add_field(
			name = f"Удалил",
			value = f">>> **`{entry.user.name}` | `{entry.user.id}`**",
			inline = False
		)
		await self.logsend(channel.guild.id,embed)
	@Cog.listener()
	async def on_guild_role_create(self, role):

		entry = await role.guild.audit_logs(action  = disnake.AuditLogAction.role_create, limit = 1).get()
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.green())
		embed.set_author(
			name = f"Создана роль",
			icon_url ="https://media.discordapp.net/attachments/686585233339842572/708784588100600008/role_gray_plus_green.png"
		)
		embed.add_field(
			name = f"Роль",
			value = f"{role.mention} | `{role.id}`",
			inline = True
		)
		embed.add_field(
			name = f"Создал",
			value = f"**`{entry.user.name}` | `{entry.user.id}`**",
			inline = True
		)
		await self.logsend(role.guild.id,embed)
	@Cog.listener()
	async def on_guild_role_delete(self, role):
		entry = await role.guild.audit_logs(action=disnake.AuditLogAction.role_delete, limit=1).get()
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.red())
		embed.set_author(
			name = f"Роль была удалена",
			icon_url = 'https://media.discordapp.net/attachments/886599188459167815/951272214945210408/red.png?width=442&height=442'
		)
		embed.add_field(
			name = f"Удалил",
			value = f"**`{entry.user.name}` | `{entry.user.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Роль",
			value = f"**`{role.name}` | `{role.colour}`**",
			inline = True
		)
		embed.add_field(
			name = f"Дата создания",
			value = f">>> **`{role.created_at.strftime('%m/%d/%y | %H:%M:%S')}`**",
			inline = False
		)
		await self.logsend(role.guild.id, embed)

	@Cog.listener()
	async def on_member_ban(self,guild,member):
		
		entry = await guild.audit_logs(action  = disnake.AuditLogAction.ban, limit = 1).get()
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.red())
		embed.set_author(
			name = f"Пользователь был  забанен",
			icon_url = "https://media.discordapp.net/attachments/686585233339842572/708784100999299100/member_gray_minus_red.png"
		)
		embed.add_field(
			name = f"Пользователь",
			value = f"**`{member.name}` | `{member.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Администратор",
			value = f"**`{entry.user.name}` | `{entry.user.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Причина",
			value = f">>> {entry.reason}",
			inline= False
		)
		await self.logsend(guild.id,embed)
	@Cog.listener()
	async def on_member_remove(self,member):
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.red())
		embed.set_author(
			name = f"Пользователь покинул сервер",
			icon_url = 'https://media.discordapp.net/attachments/686585233339842572/708784100999299100/member_gray_minus_red.png'
		)
		embed.add_field(
			name = f"Пользователь",
			value = f"**`{member.name}` | `{member.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Присоединился",
			value = f"`{member.joined_at.strftime('%m/%d/%y | %H:%M:%S')}`",
			inline = True
		)
		await self.logsend(member.guild.id,embed)

	@Cog.listener()
	async def on_member_unban(self,guild,member):
		entry = await guild.audit_logs(action  = disnake.AuditLogAction.unban, limit = 1).get()
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.green())
		embed.set_author(
			name = f"Пользователь был  разбанен",
			icon_url = "https://media.discordapp.net/attachments/686585233339842572/708784127486328923/member_gray_role_green.png"
		)
		embed.add_field(
			name = f"Пользователь",
			value = f"**`{member.name}` | `{member.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Разбанил",
			value = f"**{entry.user.mention} | `{entry.user.id}`**",
			inline = True
		)


		await self.logsend(guild.id,embed)

	@Cog.listener()
	async def on_member_kick(self, member):
		entry = await member.guild.audit_logs(action  = disnake.AuditLogAction.kick, limit = 1).get()
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.red())
		embed.set_author(name = f"Пользователь был кикнут", icon_url ="https://media.discordapp.net/attachments/686585233339842572/708784100999299100/member_gray_minus_red.png")
		embed.add_field(
			name = f"Пользователь",
			value = f"**`{member.name}{member.discriminator}` | `{member.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Администратор",
			value = f"**`{entry.user.name}{entry.user.discriminator}` | `{entry.user.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Причина",
			value = f">>> {entry.reason}",
			inline = False
		)
		await self.logsend(member.guild.id,embed)

	@Cog.listener()
	async def on_member_join(self, member):
		embed = disnake.Embed(
			timestamp = datetime.utcnow(),
			color = disnake.Colour.green())
		embed.set_author(name = f"Пользователь зашел на сервер", icon_url = "https://media.discordapp.net/attachments/686585233339842572/708784127486328923/member_gray_role_green.png")
		embed.add_field(name = f"Юзер", value = f"**`{member.name}{member.discriminator}` | `{member.id}`**",inline = True)
		embed.add_field(name = f"Дата создания", value = f">>> **`{member.created_at.strftime('%m/%d/%y | %H:%M:%S')}`**",inline = False)
		await self.logsend(member.guild.id,embed)

	@Cog.listener()
	async def on_thread_join(self,thread):
		entry = await thread.guild.audit_logs(action  = disnake.AuditLogAction.thread_create, limit = 1).get()
		embed = disnake.Embed(
				timestamp = datetime.utcnow(),
				color = disnake.Colour.green()
			)
		embed.set_author(
			name = f"Пользователь создал ветку",
			icon_url ='https://media.discordapp.net/attachments/886599188459167815/951287503573377085/next.png?width=442&height=442'
		)
		embed.add_field(
			name = f"Ветка",
			value = f"**`{thread.name}` | `{thread.id}`**",
			inline = False
		)
		embed.add_field(
			name = f"Дата создания",
			value = f"**`{entry.user.name}` | `{entry.user.id}`**",
			inline = False
		)
		await self.logsend(thread.guild.id,embed)

	@Cog.listener()
	async def on_thread_delete(self, thread):
		entry = await thread.guild.audit_logs(action  = disnake.AuditLogAction.thread_create, limit = 1).get()
		embed = disnake.Embed(
				timestamp = datetime.utcnow(),
				color = disnake.Colour.red()
			)
		embed.set_author(
			name = f"Ветка удалена",
			icon_url = 'https://media.discordapp.net/attachments/886599188459167815/951289888010018846/xd.png?width=442&height=442'
		)
		embed.add_field(
			name = f"Ветка",
			value = f"**`{thread.name}` | `{thread.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Дата создания",
			value = f"`{thread.created_at.strftime('%m/%d/%y | %H:%M:%S')}`",
			inline = True
		)
		embed.add_field(
			name = f"Создал",
			value = f"**`{thread.owner}` | `{thread.owner_id}`**",
			inline = False
		)
		await self.logsend(thread.guild.id,embed)

	@Cog.listener()
	async def on_thread_member_join(self, member):
		embed = disnake.Embed(
				timestamp = datetime.utcnow(),
				color = disnake.Colour.green()
			)
		embed.set_author(
			name = f"Пользователь присоединился к ветке",
			icon_url ="https://media.discordapp.net/attachments/886599188459167815/951289097127858247/xz.png?width=442&height=442"
		)
		embed.add_field(
			name = f"Пользователь",
			value = f"**`{member}` | `{member.id}`**",
			inline = False
		)
		embed.add_field(
			name = f"Ветка",
			value = f"**`{member.thread}` | `{member.thread.id}`**",
			inline = False
		)
		await self.logsend(member.guild.id,embed)

	@Cog.listener()
	async def on_thread_member_remove(self, member):
		embed = disnake.Embed(
				timestamp = datetime.utcnow(),
				color = disnake.Colour.red()
			)
		embed.set_author(
			name = f"Пользователь покинул ветку",
			icon_url = 'https://media.discordapp.net/attachments/886599188459167815/951291237187588236/zxxx.png?width=442&height=442'
		)
		embed.add_field(
			name = f"Пользователь",
			value = f"**`{member.name}` | `{member.id}`**",
			inline = True
		)
		embed.add_field(
			name = f"Bеткa",
			value = f"**`{member.thread.name}` | `{member.thread.id}`**",
			inline = True
		)
		await self.logsend(member.guild.id,embed)

	@Cog.listener()
	async def on_thread_update(self, before, after):
		if before.name != after.name:
			embed = disnake.Embed(
					timestamp = datetime.utcnow(),
					color = disnake.Colour.blue()
				)
			embed.set_author(
				name = f"Пользователь обновил ветку",
				icon_url ='https://media.discordapp.net/attachments/686585233339842572/708866410457071636/text_gray_update_yellow.png'
			)

			embed.add_field(name = f"Старое название", value = f">>> **`{before.name}`**",inline= False)
			embed.add_field(name = f"Новое название", value = f">>> **`{after.name}`**", inline=False)
			await self.logsend(after.guild.id,embed)

	@Cog.listener()
	async def on_guild_emojis_update(self, guild, before, after):
		print(before)
		print(after)
		if len(before) > len(after):
			entry = await guild.audit_logs(action = disnake.AuditLogAction.emoji_update, limit = 1).get()
			embed = disnake.Embed(
					timestamp=datetime.utcnow(),
					color = disnake.Colour.blue()
				)
			embed.set_author(
				name = f"Добавлен новый эмоджи",
				icon_url = 'https://media.discordapp.net/attachments/686585233339842572/708866322934792213/emoji_gray_update_yellow.png'
			)
			await self.logsend(guild.id, embed)
	@Cog.listener()
	async def on_guild_scheduled_event_create(self, event):
		entry = await event.guild.audit_logs(action = disnake.AuditLogAction.guild_scheduled_event_create, limit = 1).get()
		embed = disnake.Embed(
				timestamp = datetime.utcnow(),
				color = disnake.Colour.green()
			)
		embed.set_author(
			name = "Создано событие",
			icon_url = "https://media.discordapp.net/attachments/886599188459167815/951493288165269504/eventplus1.png?width=442&height=442"
		)
		embed.add_field(name = '**Создал: **',value = f">>> **`{event.creator.name}` | `{event.creator_id}`**",inline= True)
		embed.add_field(name ='**Канал: **',value = f"**`{event.channel.name}` | `{event.channel_id}`**",inline= True)
		embed.add_field(name ='**Описание | Название: **',value = f">>> **`{event.name}`\n`{event.description}`**",inline= False)
		embed.add_field(name ='**Дата: **', value =f"**`{event.scheduled_end_time} - {event.scheduled_end_time}`**",inline= True)
		await self.logsend(event.guild.id,embed)

	@Cog.listener()
	async def on_guild_scheduled_event_delete(self, event):
		entry = await event.guild.audit_logs(action = disnake.AuditLogAction.guild_scheduled_event_delete, limit = 1).get()
		embed = disnake.Embed(
				timestamp = datetime.utcnow(),
				color = disnake.Colour.red()
			)
		embed.set_author(
			name = "Событие удалено",
			icon_url = 'https://media.discordapp.net/attachments/886599188459167815/951494059426447360/eventps.png?width=442&height=442'
		)
		embed.add_field(
			name = "Ивент",
			value = f"**`{event.name}` | `{event.id}`**",
			inline = True
		)
		embed.add_field(
			name = "Дата создания",
			value = f"**`{event.created_at.strftime('%d/%m/%y | %H:%M:%S')}`**",
			inline = True
		)
		embed.add_field(
			name = "Удалил",
			value = f"**`{entry.user.name}` | `{entry.user.id}`**",
			inline = False
		)
		await self.logsend(event.guild.id,embed)

	@Cog.listener()
	async def on_guild_scheduled_event_subscribe(self, event, user):
		embed = disnake.Embed(
				color = disnake.Colour.green()
			)
		embed.set_author(
			name = "Пользователь подписался на событие",
			icon_url = "https://media.discordapp.net/attachments/886599188459167815/951497087172874250/subscribber.png?width=442&height=442"
		)
		embed.add_field(
			name = "Пользователь",
			value = f"**`{user.name}` | `{user.id}`**",
			inline = True
		)
		embed.add_field(
			name = "Событие",
			value = f"**`{event.name}` | `{event.id}`**",
			inline = True
		)
		await self.logsend(event.guild.id,embed)
	@Cog.listener()
	async def on_guild_scheduled_event_unsubscribe(self, event, user):
		embed = disnake.Embed(
				timestamp = datetime.utcnow(),
				color = disnake.Colour.red()
			)

		embed.set_author(name = "Участник отписался от события",
						 icon_url = "https://media.discordapp.net/attachments/948338622472552470/951498817159725176/unsub.png?width=442&height=442")
		embed.add_field(name = '**Событие:**', value = f"`{event.name}`", inline = True)
		embed.add_field(name = '**Участник:**', value = f"`{user.name}` | `{user.id}`", inline = True)
		await self.logsend(event.guild.id,embed)

	@Cog.listener()
	async def on_guild_channel_update(self, before, after):
		entry = await after.guild.audit_logs(action=disnake.AuditLogAction.channel_update, limit=1).get()
		if before.name != after.name:
			embed = Embed(color = disnake.Colour.yellow(),timestamp=datetime.utcnow())
			embed.set_author(name="Название канала изменено",
							 icon_url="https://media.discordapp.net/attachments/686585233339842572/708866410457071636/text_gray_update_yellow.png")
			embed.add_field(name = "**До изменения: **", value = f"`{before.name}`", inline = True)
			embed.add_field(name = "**После изменения: **", value = f"`{after.name}`", inline = True)
			embed.add_field(name = "**Изменил**", value = f">>> **`{entry.user.name}` | `{entry.user.id}`**", inline = False)
			await self.logsend(after.guild.id,embed)
	@Cog.listener()
	async def on_invite_create(self, invite):
		embed = disnake.Embed(
					title = f':recycle: | Создана ссылка приглашения',
					description =f">>> **Создал: `{invite.inviter.name}` | `{invite.inviter.id}`\nСсылка: `discord.gg/{invite.code}`**",
					timestamp = datetime.utcnow(),
					color = disnake.Colour.green()
				)
		await self.logsend(invite.guild.id,embed)

	@Cog.listener()
	async def on_invite_delete(self, invite):
		entry = await invite.guild.audit_logs(action = disnake.AuditLogAction.invite_delete, limit = 1).get()
		embed = disnake.Embed(
					title = f':no_entry: | Удалена ссылка приглашения',
					description =f">>> **Ссылка: `discord.gg/{invite.code}`\nУдалил: `{entry.user.name}` | `{entry.user.id}`**",
					timestamp = datetime.utcnow(),
					color = disnake.Colour.red()
				)
		await self.logsend(invite.guild.id,embed)
	@Cog.listener()
	async def on_guild_update(self, before, after):
		entry = await after.audit_logs(action = disnake.AuditLogAction.guild_update, limit = 1).get()
		if before.name != after.name:
			embed = disnake.Embed(
					title = f":recycle: | Название сервера было изменено",
					description = f">>> **Изменил: **`{entry.user.name}` | `{entry.user.id}`",
					timestamp = datetime.utcnow(),
					color = disnake.Colour.green()
				)
			fields = [(">>> **Before: **", '`'+before.name+'`', False),
						  (">>> **After: **", '`'+after.name+'`', False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			await self.logsend(after.id,embed)
		if before.afk_channel != after.afk_channel:
			embed = disnake.Embed(
					title = f":recycle: | Афк канал изменён",
					description = f">>> **Изменил: **`{entry.user.name}` | `{after.user.id}`",
					timestamp = datetime.utcnow(),
					color = disnake.Colour.green()
				)
			fields = [(">>> **Старое содержимое: **", '`'+before.afk_channel+'`', False),
						  (">>> **Новое содержимое: **", '`'+after.afk_channel+'`', False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			await self.logsend(after.id,embed)
		if before.afk_timeout != after.afk_timeout:
			embed = disnake.Embed(
					title = f":recycle: | Афк таймаут изменён",
					description = f">>> **Изменил: **`{entry.user.name}` | `{after.user.id}`",
					timestamp = datetime.utcnow(),
					color = disnake.Colour.green()
				)
			fields = [(">>> **Старое содержимое: **", '`'+before.afk_timeout+'`', False),
						  (">>> **Новое содержимое: **", '`'+after.afk_timeout+'`', False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			await self.logsend(after.id,embed)
		if before.icon != after.icon and before.icon and after.icon:
			embed = Embed(title=":recycle: | Аватарка сервера изменена:",
						  description=">>> **Новое изображение внизу, старое справа.**",
						  colour=disnake.Colour.green(),
						  timestamp=datetime.utcnow())

			embed.set_thumbnail(url=before.icon)
			embed.set_image(url=after.icon)

			await self.logsend(after.id,embed)




def setup(bot):
	bot.add_cog(Log(bot))