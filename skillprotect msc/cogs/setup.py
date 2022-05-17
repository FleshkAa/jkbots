import discord
from discord.ext import commands
import re
from Tools.utils import getConfig, getGuildPrefix, updateConfig
import asyncio
import json
from discord.utils import get


class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(usage="<kick/ban/none>",
                      name="punishment",
                      description="Устанавливает краш ботам наказание")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    @commands.guild_only()
    async def punishment(self, ctx, kickOrBan):
        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        admin = data["administrator"]
        if ctx.author.id == owner or admin:

            kickOrBan = kickOrBan.lower()

            if kickOrBan == "kick":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "kick"

                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**Наказание:** `{kickOrBan}`''',
                 color=discord.Colour.green()))

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "ban":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "ban"

                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**Наказание:** `{kickOrBan}`''',
                 color=discord.Colour.green()))

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "none":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "none"

                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**Наказание:** `{kickOrBan}`''',
                 color=discord.Colour.green()))

                updateConfig(ctx.guild.id, data)

        else:
            await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")

    @commands.command(usage="<member>",
                      name="whitelist",
                      description="Adds member to the server whitelist")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    @commands.guild_only()
    async def whitelist(self, ctx, member: discord.Member = None):
        try:
            data = getConfig(ctx.guild.id)
            owner = data["owner"]
            admin = data["administrator"]
            if ctx.author.id == owner or admin:
                if member == None:
                    return await ctx.send("УКАЖИТЕ УЧАСТНИКА НА КОТОРОГО БУДУТ ИГНОРИТЬСЯ ДЕЙСТВИЯ")
                if member.id == 882901345466724373:
                    return await ctx.send("ВЫ НЕ МОЖИТЕ УКАЗАТЬ МЕНЯ")
                else:
                    data = getConfig(ctx.guild.id)
                    whitelisted = data["whitelist"]
                    if member.id in whitelisted:
                        return await ctx.send("на этого пользователя уже игноряться действия")
                    else:
                        data = getConfig(ctx.guild.id)
                        data["whitelist"].append(member.id)
                        await ctx.send(
                        embed = discord.Embed(
                         title = 'УСПЕШНО!',
                         description = F'''ТЕПЕРЬ ИГНОРЯТСЯ ДЕЙСТВИЯ НА `{member.mention}`''',
                         color=discord.Colour.green()))
                        updateConfig(ctx.guild.id, data)
            else:
                await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")
        except:
            pass

    @commands.command(usage="<member>",
                      name="unwhitelist",
                      description="Удаляет участника из белого списка сервера")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    @commands.guild_only()
    async def unwhitelist(self, ctx, member: discord.Member = None):
        try:
            data = getConfig(ctx.guild.id)
            owner = data["owner"]
            admin = data["administrator"]
            if ctx.author.id == owner or admin:
                if member == None:
                    return await ctx.send("УКАЖИТЕ ПОЛЬЗОВАТЕЛЯ НА КОТОРОГО ПЕРЕСТАНУТ ИГНОРИРОВАТЬСЯ ДЕЙСТВИЯ")
                if member.id == 882901345466724373:
                    return await ctx.send("ВЫ НЕ МОЖИТЕ УКАЗАТЬ МЕНЯ")
                else:
                    data = getConfig(ctx.guild.id)
                    whitelisted = data["whitelist"]
                    if member.id not in whitelisted:
                        return await ctx.send("НА ЭТОГО ПОЛЬЗОВАТЕЛЯ НЕ ИГНОРЯТСЯ ДЕЙСТВИЯ")
                    else:
                        data = getConfig(ctx.guild.id)
                        data["whitelist"].remove(member.id)
                        await ctx.send(
                        embed = discord.Embed(
                         title = 'УСПЕШНО!',
                         description = F'''ТЕПЕРЬ НЕ ИГНОРЯТСЯ ДЕЙСТВИЯ НА: `{member.mention}`''',
                         color=discord.Colour.green()))
                        updateConfig(ctx.guild.id, data)
            else:
                await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")
        except:
            pass

    @commands.command(name="whitelisted",
                      description="Показывает текущий белый список серверов")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    @commands.guild_only()
    async def whitelisted(self, ctx):
        prefix = await getGuildPrefix(self.client, ctx)
        try:
            data = getConfig(ctx.guild.id)
            whitelisted = data["whitelist"]
            owner = data["owner"]
            admin = data["administrator"]
            if ctx.author.id in whitelisted or owner or admin:
                loading = await ctx.send("Searching...")
                result = ' '
                data = getConfig(ctx.guild.id)
                userinwhitelist = data["whitelist"]
                for i in userinwhitelist:
                    user2 = self.client.get_user(i)
                    if user2 == None:
                        user = 'Не удалось получить имя'
                    else:
                        user = user2.mention
                    result += f"{user}: {i}\n"
                await loading.delete()
                if data["whitelist"] == []:
                    return await ctx.send(f"На этом сервере нет пользователей на которых игнорятся действия, введите `{prefix}whitelist <user>`, чтобы на пользователя игнорились действия")
                else:
                    embed = discord.Embed(title=f'Пользователи из белого списка для {ctx.guild.name}', description=result,
                                          color=discord.Colour.green())
                    await ctx.send(embed=embed)

            else:
                return await ctx.send("Только владелец сервера или пользователь из белого списка может использовать эту команду!")
        except:
            pass

    @commands.command(name="verifiedrole",
                      description="Changes/Sets the Verified Role ")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    @commands.guild_only()
    async def verifiedrole(self, ctx, roleId):
        try:
            data = getConfig(ctx.guild.id)
            owner = data["owner"]
            admin = data["administrator"]
            if ctx.author.id == owner or admin:
                roleId = int(roleId)
                data = getConfig(ctx.guild.id)
                data["roleGivenAfterCaptcha"] = roleId

                updateConfig(ctx.guild.id, data)

                await ctx.send("<@&{0}> will be given after that the captcha be passed.".format(roleId))

            else:
                await ctx.send("Only the owner or a selected administrator can use this command!")

        except Exception:
            pass
            data = getConfig(ctx.guild.id)
            owner = data["owner"]
            admin = data["administrator"]
            if ctx.author.id == owner or admin:
                roleId = roleId.lower()
                if roleId == "off":
                    data = getConfig(ctx.guild.id)
                    roleGivenAfterCaptcha = get(ctx.guild.roles, id=data["roleGivenAfterCaptcha"])
                    await roleGivenAfterCaptcha.delete()
                    data["roleGivenAfterCaptcha"] = False

                    updateConfig(ctx.guild.id, data)
                    await ctx.send("The captcha role has been successfully reset")

            else:
                await ctx.send("Only the owner or a selected administrator can use this command!")

    @commands.group(invoke_without_command=True,
                    description="Показывает модули настройки")
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):

        perms = ctx.me.guild_permissions
        if not (perms.administrator):
            return await ctx.send("Извините, но для продолжения мне потребуются права администратора!")

        emote = ("<:rightArrow:904016483108143115>")
        alarm = ("🚨")
        shild = ("🛡️")
        filter = ("🚫")
        verify = ("📝")
        auto = ("🤖")
        raid = ("🔒")
        data = getConfig(ctx.guild.id)
        prefix = data["prefix"]
        embed = discord.Embed(title=f"Setup {self.client.user.name}",
                              description=f"Убедитесь, что бот имеет максимально возможную роль на вашем сервере. Переместите созданную им роль выше! Также бот не будет работать без прав администратора.",
                              colour=discord.Colour.green())
        embed.add_field(name=f"{shild} Setup Anti-Nuke", value=f"{emote} `{prefix}setup antinuke`")
        embed.add_field(name=f"{filter} Setup Join-Filter", value=f"{emote} `{prefix}setup joinfilter`")
        embed.add_field(name=f"{auto} Setup Auto-Moderation", value=f"{emote} `{prefix}automoderation`")
        embed.add_field(name=f"{alarm} Enable Panic-Mode", value=f"{emote} `{prefix}panicmode <on>`")
        embed.add_field(name=f"{raid} Enable Raid-Mode", value=f"{emote} `{prefix}raidmode <on>`")
        await ctx.send(embed=embed)


    @setup.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def antinuke(self, ctx):

        perms = ctx.me.guild_permissions
        if not (perms.administrator):
            return await ctx.send("Извините, но для продолжения мне потребуются права администратора!")

        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]
        if ctx.author.id == owner or administrator:
            loading = await ctx.send("Настройка защиты...")
            data = getConfig(ctx.guild.id)
            data["antinuke"] = True

            if data["logChannel"] is False:
                logChannel = await ctx.guild.create_text_channel(f"{self.client.user.name}-logs")

                perms = logChannel.overwrites_for(ctx.guild.default_role)
                perms.read_messages = False
                await logChannel.set_permissions(ctx.guild.default_role, overwrite=perms)

                data["logChannel"] = logChannel.id

                updateConfig(ctx.guild.id, data)
                await loading.delete()

                prefix = await getGuildPrefix(self.client, ctx)
                embed = discord.Embed(title=f"Настройка выполнена успешно", description=f"Я успешно настроил функцию Anti-Nuke.\n\n"
                                                                               f"**Белый список:**\nВам следует добавить некоторых участников в белый список. `{prefix}whitelist <user>`", colour=discord.Colour.blue())
                await ctx.send(embed=embed)

        else:
            await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")

    @commands.command(name="antinuke",
                      description="Disables the Anti-Nuke feature")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def _antinuke(self, ctx, off):
        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            if off == "off":
                loading = await ctx.channel.send("Удаление защиты...")
                data = getConfig(ctx.guild.id)
                data["antinuke"] = False
                if data["joinfilter"] is False:
                    if data["panicmode"] is False:
                        if data["panicmode"] is False:
                            logChannel = self.client.get_channel(data["logChannel"])
                            await logChannel.delete()

                            data["logChannel"] = False

                updateConfig(ctx.guild.id, data)
                await loading.delete()
                await ctx.send("Защита отключена!")

        else:
            await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")

    @setup.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def joinfilter(self, ctx):

        perms = ctx.me.guild_permissions
        if not (perms.administrator):
            return await ctx.send("Извините, но для продолжения мне потребуются права администратора!")

        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            loading = await ctx.send("Настройка фильтра присоединения...")

            data = getConfig(ctx.guild.id)
            data["joinfilter"] = True
            data["botfilter"] = True
            data["avatarfilter"] = True
            data["checknew"] = True

            if data["logChannel"] is False:
                logChannel = await ctx.guild.create_text_channel(f"{self.client.user.name}-logs")

                perms = logChannel.overwrites_for(ctx.guild.default_role)
                perms.read_messages = False
                await logChannel.set_permissions(ctx.guild.default_role, overwrite=perms)

                data["logChannel"] = logChannel.id


            updateConfig(ctx.guild.id, data)
            await loading.delete()

            embed = discord.Embed(title="Настройка выполнена успешно", description=f"Я успешно настроил функцию\n\n"
                                                                          f"**Note:**\nустановлено на 25", colour=discord.Colour.blue())
            await ctx.send(embed=embed)
        else:
            await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")

    @commands.command(name="joinfilter",
                      description="Отключает функцию объединения фильтров")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def _joinfilter(self, ctx, off):
        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            if off == "off":
                loading = await ctx.send("Удаление фильтра объединения...")

                data = getConfig(ctx.guild.id)
                data["joinfilter"] = False
                data["botfilter"] = False
                data["avatarfilter"] = False
                data["checknew"] = False

                if data["antinuke"] is False:
                    if data["panicmode"] is False:
                        if data["panicmode"] is False:
                            logChannel = self.client.get_channel(data["logChannel"])
                            await logChannel.delete()

                            data["logChannel"] = False

                updateConfig(ctx.guild.id, data)

                await loading.delete()
                await ctx.send("Объединение-Фильтр отключен!")

        else:
            await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")

    @setup.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def automoderation(self, ctx):

        perms = ctx.me.guild_permissions
        if not (perms.administrator):
            return await ctx.send("Извините, но для продолжения мне потребуются права администратора!")

        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            loading = await ctx.send("Настройка автоматической модерации...")
            data = getConfig(ctx.guild.id)
            data["automoderation"] = True
            data["antiSpam"] = True
            data["antiWord"] = True
            data["antiLink"] = True
            data["antighost"] = True

            updateConfig(ctx.guild.id, data)
            await loading.delete()

            embed = discord.Embed(title=f"Настройка выполнена успешно", description=f"Я успешно настроил функцию автоматической модерации.", colour=discord.Colour.blue())
            await ctx.send(embed=embed)

        else:
            await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")

    @commands.command(name="automoderation",
                      description="Отключает функцию автоматической модерации")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def _automoderation(self, ctx, off):
        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            if off == "off":
                loading = await ctx.send("Удаление системы автомодерации..")
                data = getConfig(ctx.guild.id)
                data["automoderation"] = False
                data["antiSpam"] = False
                data["antiWord"] = False
                data["antiLink"] = False
                data["antighost"] = False

                await loading.delete()
                await ctx.send("Автомодерация отключена!")
                updateConfig(ctx.guild.id, data)

        else:
            await ctx.send("Только владелец или выбранный администратор может использовать эту команду!")

    @commands.command(description="Включает или отключает модуль фильтра ботов")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def botfilter(self, ctx, onOroff):
        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:

            onOroff = onOroff.lower()

            if onOroff == "on":
                if data["botfilter"] == True:
                    await ctx.send(
                    embed = discord.Embed(
                     title = 'ОШИБКА!',
                     description = F'''**БОТ ФИЛЬТЕР УЖЕ БЫЛ ВКЛЮЧЁН**''',
                     color=discord.Colour.blue()))
                    data = getConfig(ctx.guild.id)
                    data["botfilter"] = True
                else:
                    data["botfilter"] = True
                    if data["joinfilter"] is not True:
                        data["joinfilter"] = True

                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**БОТ ФИЛЬТЕР ВКЛЮЧЁН**''',
                 color=discord.Colour.blue()))

                updateConfig(ctx.guild.id, data)


            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["botfilter"] = False
                if data["avatarfilter"] is False:
                    if data["autoban"] is False:
                        if data["checknew"] is False:
                            data["joinfilter"] = False

                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**БОТ ФИЛЬТЕР ВЫКЛЮЧЕН**''',
                 color=discord.Colour.blue()))

                updateConfig(ctx.guild.id, data)

        else:
            await ctx.send(
            embed = discord.Embed(
              title = 'ОШИБКА!',
              description = F'''**НЕТ ПРАВ НА КОММАНДУ**''',
              color=discord.Colour.blue()))



    @commands.command(name="antispam",
                      description="Включает или отключает модуль защиты от спама.")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def antispam(self, ctx, onOroff):

        onOroff = onOroff.lower()

        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            if onOroff == "on":
                if data["antiSpam"] is True:
                    await ctx.send(
                    embed = discord.Embed(
                     title = 'ОШИБКА!',
                     description = F'''**АНТИ СПАМ УЖЕ ВКЛЮЧЁН**''',
                     color=discord.Colour.blue()))
                else:
                    data["antiSpam"] = True
                    if data["automoderation"] is not True:
                        data["automoderation"] = True

                    updateConfig(ctx.guild.id, data)
                    await ctx.send(
                    embed = discord.Embed(
                     title = 'УСПЕШНО!',
                     description = F'''**АНТИ СПАМ ВКЛЮЧЁН**''',
                     color=discord.Colour.blue()))

            if onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiSpam"] = False
                if data["antiWord"] is False:
                    if data["antiLink"] is False:
                        if data["antighost"] is False:
                            data["automoderation"] = False

                updateConfig(ctx.guild.id, data)
                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**БОТ ФИЛЬТЕР ВЫКЛЮЧЕН**''',
                 color=discord.Colour.blue()))

        else:
            await ctx.send(
            embed = discord.Embed(
             title = 'ОШИБКА!',
             description = F'''**НЕТ ПРАВ НА КОММАНДУ**''',
             color=discord.Colour.blue()))



    @commands.command(name="antilink",
                      description="Включает или отключает модуль Anti Link")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def antilink(self, ctx, onOroff):

        onOroff = onOroff.lower()

        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            if onOroff == "on":
                if data["antiLink"] is True:
                    await ctx.send(
                    embed = discord.Embed(
                     title = 'ОШИБКА!',
                     description = F'''**АНТИ ССЫЛКИ УЖЕ БЫЛИ ВКЛЮЧЕНЫ**''',
                     color=discord.Colour.blue()))
                else:
                    data["antiLink"] = True
                    if data["automoderation"] is not True:
                        data["automoderation"] = True

                updateConfig(ctx.guild.id, data)
                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**АНТИ ССЫЛКИ ВКЛЮЧЕНЫ**''',
                 color=discord.Colour.blue()))

            if onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiLink"] = False
                if data["antiSpam"] is False:
                    if data["antiWord"] is False:
                        if data["antighost"] is False:
                            data["automoderation"] = False

                updateConfig(ctx.guild.id, data)
                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**АНТИ ССЫЛКИ ВЫКЛЮЧЕНЫ**''',
                 color=discord.Colour.blue()))

        else:
            await ctx.send(  
            embed = discord.Embed(
             title = 'ОШИБКА!',
             description = F'''**НЕТ ПРАВ НА КОММАНДУ**''',
             color=discord.Colour.blue()))

    @commands.command(name="antighost",
                      description="анти пинг")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def antighost(self, ctx, onOroff):

        onOroff = onOroff.lower()

        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:
            if onOroff == "on":
                if data["antighost"] is True:
                    await ctx.send(
                    embed = discord.Embed(
                     title = 'ОШИБКА!',
                     description = F'''**АНТИ ПИНГ УЖЕ БЫЛ ВКЛЮЧЁН**''',
                     color=discord.Colour.blue()))
                else:
                    data["antighost"] = True
                    if data["automoderation"] is not True:
                        data["automoderation"] = True

                updateConfig(ctx.guild.id, data)
                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**АНТИ ПИНГ ВКЛЮЧЁН**''',
                 color=discord.Colour.blue()))

            if onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antighost"] = False
                if data["antiSpam"] is False:
                    if data["antiWord"] is False:
                        if data["antiLink"] is False:
                            data["automoderation"] = False

                updateConfig(ctx.guild.id, data)
                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**АНТИ ПИНГ ВЫКЛЮЧЕН**''',
                 color=discord.Colour.blue()))

        else:
            await ctx.send(
            embed = discord.Embed(
             title = 'ОШИБКА!',
             description = F'''**НЕТ ПРАВ НА КОММАНДУ**''',
             color=discord.Colour.blue()))



    @commands.command(description="Устанавливает администратора, который может использовать все мои команды")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def administrator(self, ctx, member: discord.Member = None):
        try:
            data = getConfig(ctx.guild.id)
            owner = data["owner"]
            if ctx.author.id == owner:
                if member == None:
                    return await ctx.send("Упомяните участника!")
                else:
                    data = getConfig(ctx.guild.id)
                    data["administrator"] = member.id
                    await ctx.send(f"{member.mention} теперь может использовать все мои команды!")
                    updateConfig(ctx.guild.id, data)

            else:
                await ctx.send("Только владелец может использовать эту команду!")

        except:
            pass

    @commands.command(description="Сбросить администратора, который может использовать все мои команды")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def unadministrator(self, ctx, member: discord.Member = None):
        try:
            data = getConfig(ctx.guild.id)
            owner = data["owner"]
            if ctx.author.id == owner:
                if member == None:
                    return await ctx.send("Упомяните участника!")
                else:
                    data = getConfig(ctx.guild.id)
                    data["administrator"] = False
                    await ctx.send(f"Теперь {member.mention} больше не может использовать какие-либо команды настройки и т. д..")
                    updateConfig(ctx.guild.id, data)

            else:
                await ctx.send("Только владелец может использовать эту команду!")
        except:
            pass

    @commands.command(description="Включает или отключает модуль автобана")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def autoban(self, ctx, onOroff):

        onOroff = onOroff.lower()

        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        if ctx.author.id == owner:
            if onOroff == 'on':
                if data["autoban"] is True:
                    await ctx.send(
                    embed = discord.Embed(
                     title = 'ОШИБКА!',
                     description = F'''**АВТО БАН УЖЕ БЫЛ ВКЛЮЧЁН**''',
                     color=discord.Colour.blue()))
                else:
                    embed = discord.Embed(title="Функция автобана безопасности сервера",
                                          description=f"Вы уверены, что хотите включить функцию автобана? **Рекомендую активировать только в экстренных ситуациях!**\n\n"
                                                      f'Если вы хотите включить его, напишите **"да"**, иначе **"нет"**', colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

                    def check(message):
                        if message.author == ctx.author and message.content in ["да", "нет"]:
                            return message.content

                    try:
                        msg = await self.client.wait_for('message', timeout=30.0, check=check)
                        if msg.content == "нет":
                            await ctx.send(
                            embed = discord.Embed(
                             title = 'УСПЕШНО!',
                             description = F'''**АВТО БАН ОТМЕНЁН**''',
                             color=discord.Colour.blue()))
                        else:
                            data = getConfig(ctx.guild.id)
                            data["autoban"] = True
                            if data["joinfilter"] is not True:
                                data["joinfilter"] = True

                            if data["logChannel"] is False:
                                logChannel = await ctx.guild.create_text_channel(f"{self.client.user.name}-logs")

                                perms = logChannel.overwrites_for(ctx.guild.default_role)
                                perms.read_messages = False
                                await logChannel.set_permissions(ctx.guild.default_role, overwrite=perms)

                                data["logChannel"] = logChannel.id

                            updateConfig(ctx.guild.id, data)
                            embed = discord.Embed(title="Активировано успешно", description=f"Я успешно включил функцию автобана.", colour=discord.Colour.blue())
                            await ctx.send(embed=embed)

                    except(asyncio.TimeoutError):
                        await ctx.send("Тайм-аут! (30s)")

            if onOroff == 'off':
                data = getConfig(ctx.guild.id)
                data["autoban"] = False
                if data["avatarfilter"] is False:
                    if data["botfilter"] is False:
                        if data["checknew"] is False:
                            data["joinfilter"] = False

                updateConfig(ctx.guild.id, data)
                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**АВТО БАН ВЫКЛЮЧЕН**''',
                 color=discord.Colour.blue()))



    @commands.command()
    async def raidmode(self, ctx, onORoff):

        onORoff = onORoff.lower()

        if onORoff == "on":
            data = getConfig(ctx.guild.id)
            data["raid"] = True
            data["automoderation"] = True
            data["antiSpam"] = True
            data["antiWord"] = True
            data["antiLink"] = True
            data["joinfilter"] = True
            data["checknew"] = True

            updateConfig(ctx.guild.id, data)
            await ctx.guild.edit(verification_level=discord.VerificationLevel.very_high)
            embed = discord.Embed(title="Активировано успешно",
                                  description=f"Я успешно включил функцию Raid Mode.",
                                  colour=discord.Colour.blue())
            await ctx.send(embed=embed)

        if onORoff == "off":
            data = getConfig(ctx.guild.id)
            data["raid"] = False
            if data["antighost"] is False:
                data["automoderation"] = False
                data["antiSpam"] = False
                data["antiLink"] = False
                data["antiWord"] = False
                data["checknew"] = False
            if data["botfilter"] is False:
                if data["avatarfilter"] is False:
                    if data["autoban"] is False:
                        data["joinfilter"] = False

            updateConfig(ctx.guild.id, data)
            await ctx.guild.edit(verification_level=discord.VerificationLevel.low)
            await ctx.send("Рейд-режим отключен!")


    @commands.command(description="Включает или отключает модуль фильтра аватаров.")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def avatarfilter(self, ctx, onOroff):
        data = getConfig(ctx.guild.id)
        owner = data["owner"]
        administrator = data["administrator"]

        if ctx.author.id == owner or administrator:

            onOroff = onOroff.lower()

            if onOroff == "on":
                if data["avatarfilter"] == True:
                    await ctx.send(
                    embed = discord.Embed(
                     title = 'ОШИБКА!',
                     description = F'''**АВАТАР ФИЛЬТЕР УЖЕ БЫЛ ВКЛЮЧЁН**''',
                     color=discord.Colour.blue()))
                    data = getConfig(ctx.guild.id)
                    data["avatarfilter"] = True
                else:
                    data["avatarfilter"] = True
                    if data["joinfilter"] is not True:
                        data["joinfilter"] = True

                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**АВАТАР ФИЛЬТЕР ВКЛЮЧЁН**''',
                 color=discord.Colour.blue()))

                updateConfig(ctx.guild.id, data)


            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["avatarfilter"] = False
                if data["botfilter"] is False:
                    if data["autoban"] is False:
                        if data["checknew"] is False:
                            data["joinfilter"] = False

                await ctx.send(
                embed = discord.Embed(
                 title = 'УСПЕШНО!',
                 description = F'''**АВАТАР ВИЛЬТЕР ВЫКЛЮЧЕН**''',
                 color=discord.Colour.blue()))

                updateConfig(ctx.guild.id, data)

        else:
            await ctx.send(
            embed = discord.Embed(
             title = 'ОШИБКА!',
             description = F'''**НЕТ ПРАВ НА КОММАНДУ**''',
             color=discord.Colour.blue()))

def setup(client):
    client.add_cog(Setup(client))
