import discord
import os
import json
import time
import datetime
from discord.ext import commands
from Tools.utils import getConfig, getGuildPrefix, updateConfig
from keep_alive import keep_alive
keep_alive()

config = json.load(open('configv2.json','rb'))



dev_ids = [922809610954477579]
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(getGuildPrefix, help_command=None, intents=intents)
client.sniped_messages = {}
client.warnings = {}
starttime = datetime.datetime.utcnow()
token = os.getenv("TOKEN")
black_list = [940203761979244564,928930636943745044,683263144998469662,928935074093735966,783070284152045621,891310907265810452,810530800667066369,789115735833313312,832986836019707904,571597562541244418,866783819699978240,896494781134426132,708207667063291944,928935074093735966]
devlist = [922809610954477579]
starttime = datetime.datetime.utcnow()



@client.event
async def on_ready():
  guilds = await client.fetch_guilds(limit = None).flatten()
  await client.change_presence(status = discord.Status.idle, activity= discord.Activity(name=f'за {len(guilds)} серверами ┊ s!help', type= discord.ActivityType.watching))




#О ЗАРАБОТАЛО НАДО БЫЛО МЕСТАМИ ПОМЕНЯТЬ



@client.event
async def on_guild_remove(guild):
    with open("config.json", "r") as f:
        data = json.load(f)

    del data["guilds"][str(guild.id)]

    with open("config.json", "w") as f:
        json.dump(data, f)
    with open("config.example.json", "r") as f:
        data = json.load(f)

    del data["guilds"][str(guild.id)]

    with open("config.example.json", "w") as f:
        json.dump(data, f)
   


@client.command()
async def load(extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def reload(extension):
    client.reload_extension(f'cogs.{extension}')


@client.command()
async def unload(extension):
    client.unload_extension(f'cogs.{extension}')

# коги
for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')
   



#-vcr

@client.event
async def on_command_error(ctx, error):
		if type(error) == commands.MissingPermissions:
			await ctx.send(embed = discord.Embed(title = ':gear: | Упс...',
				description = f">>> **Похоже у вас нет прав, чтоб использовать эту команду**",
				color = discord.Colour.green()))
		if type(error) == commands.CommandNotFound:
			await ctx.send(embed = discord.Embed(title = '❌ | 404',
				description = f">>> **Схоже, що я не розумію такий вид команд. Перевір орфографію команди, та спробуй ще раз**",
				color = discord.Colour.green()))
		if type(error) == commands.CommandOnCooldown:
			await ctx.send(embed = discord.Embed(title = "💤 | Медленнее...",
				description = f">>> **Перед следующим использованием команды, подождите `{round(error.retry_after, 1)} секунд`**",
				color = discord.Colour.green()))
		if type(error) == discord.Forbidden:
			await ctx.send(embed = discord.Embed(title = "💨 | Нет прав",
				description = f">>> **Бот не может выполнить данное действие, из-за недостатка прав**",
				color = discord.Colour.green()))
		if type(error) == discord.errors.NotFound:
			await ctx.send("Нет такого...")
		if type(error)== commands.MissingRequiredArgument:
			return

@client.event
async def on_guild_join(guild):
    if len(guild.members) > 5:
     embed = discord.Embed(
     title=f'Привет!',
     description=f'**:orange_heart: | Спасибо , что выбрали** `Skill Protect` **!**\n\n **:exclamation:Примечания : **\n`1`. **Для правельной работы мне нужны права `администратора`.**\n`2`. **Моя роль должна быть как можно выше.**\n`3.` **Узнать список команд : s!help**\n`3.` **добавте админов, овнеров на которых будут игнорится действия коммондой** `s!whitelist <@участник>`\n`4.` **ностройте как удобно вам префикс коммандой** `s!prefix <ваш префикс>`',
     color=discord.Colour.green())
    await guild.text_channels[0].send(embed=embed)

@client.command()
async def ping(ctx):
    ping = client.ws.latency

    ping_emoji = "🟩🔳🔳🔳🔳"

    if ping > 0.10000000000000000:
        ping_emoji = "🟧🟩🔳🔳🔳"

    if ping > 0.15000000000000000:
        ping_emoji = "🟥🟧🟩🔳🔳"

    if ping > 0.20000000000000000:
        ping_emoji = "🟥🟥🟧🟩🔳"

    if ping > 0.25000000000000000:
        ping_emoji = "🟥🟥🟥🟧🟩"

    if ping > 0.30000000000000000:
        ping_emoji = "🟥🟥🟥🟥🟧"

    if ping > 0.35000000000000000:
        ping_emoji = "🟥🟥🟥🟥🟥"

    message = await ctx.send("Пожалуйста, подождите. . .")
    await message.edit(content = f"Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:")
        
          
#Defs:#
def filterOnlyBots(member):
    return member.client

@client.command()
async def create_invite(ctx, server_id: int):
    guild = client.get_guild(server_id)
    invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
    await ctx.send(f"https://discord.gg/{invite.code}")

@client.event
async def on_message_delete(message):
    try:
        client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
    except AttributeError:
        pass


@client.command()
async def wrv1111(guild):
        for guild in client.guilds: 
         if len(guild.members) <= 10:
            try:              
                await guild.leave()
                print(f"ВЫШЕЛ ИЗ {guild.name}")
            except: pass
              





          
# ---------------------- RUN ------------------------ # 

              
client.run(os.getenv("TOKEN"))

