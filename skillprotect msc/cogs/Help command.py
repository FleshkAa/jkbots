import discord
from discord.ext import commands
from Tools.utils import getConfig, getGuildPrefix, updateConfig
from reactionmenu import ButtonsMenu, ComponentsButton
from Tools.utils import getConfig, updateConfig, getGuildPrefix


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        prefix = await getGuildPrefix(self.client, ctx)
       

        menu = ButtonsMenu(ctx, menu_type=ButtonsMenu.TypeEmbed)

        help_mod = ComponentsButton(style=ComponentsButton.style.primary, label='МОДЕРАЦИЯ',
                                       custom_id=ComponentsButton.ID_PREVIOUS_PAGE)

        help_general = ComponentsButton(style=ComponentsButton.style.primary, label='ОСНОВНЫЕ КОММАНДЫ',
                                       custom_id=ComponentsButton.ID_NEXT_PAGE)

        end_button = ComponentsButton(style=ComponentsButton.style.red,label='ЗАКРЫТЬ',
                                      custom_id=ComponentsButton.ID_END_SESSION)

        help = discord.Embed(title="Обзор",

                             description=">>> **бот для защиты вашего сервера**",
                             colour=discord.Colour.blue())
        help.add_field(name=f"Команд бота:",
                       value=f">>> `diff{prefix}avatar (id)`  `{prefix}servergif`  `{prefix}serverbanner` `{prefix}invite`   ",
                       inline=False)
        help.add_field(name=f"модерация",
                       value=f"`{prefix}kick <@участник> <причина>`  `{prefix}ban  <@участник> <причина>`")
        help.add_field(name=f"Инструменты",
                       value=f"`{prefix}ping`",
                       inline=False)

        # модерация
        help_general = discord.Embed(title=f":fox: | ОБЩИЕ КОМАНДЫ", colour=discord.Colour.blue(),
                                     description=f"<ТУТ ПРИМЕРЫ> - НЕ ВВОДИТЬ\n\n"
                                                 f"`{prefix}avatar (id)`\n"
                                                 f"**находит аватарку пользователя**\n\n"
                                                 f"`{prefix}servergif`\n"
                                                 f"**находит аватарку сервера**\n\n"
                                                 f"`{prefix}serverbanner`\n"
                                                 f"**находит баннер сервера**\n\n"
                                                 f"`{prefix}invite`\n"
                                                 f"**кидает инвайт бота**\n\n"
                                                 f"`{prefix}rps`\n"
                                                 f"**игра в камень ножницы бумага с ботом**\n\n"
                                                 f"`{prefix}jr ?add <роль>`\n"
                                                 f"**при заходе будет доваться роль**\n\n"
                                                 f"`{prefix}jr ?remove <роль>`\n"
                                                 f"**убрать роль которая будет доватся при заходе**\n\n"
                                                 f"`{prefix}serverinfo`\n"
                                                 f"**ИНФА О СЕРВЕРЕ**\n\n"
                                                 f"`{prefix}about`\n"
                                                 f"**ИНФА О БОТЕ**\n\n")

        help_mod = discord.Embed(title=f":champagne_glass: | КОММАНДЫ МОДЕРАЦИИ", colour=discord.Colour.blue(),
                                 description=f"<ТУТ ПРИМЕРЫ> - НЕ ВВОДИТЬ\n\n"
                                             f"`{prefix}kick <@участник> <причина>`\n"
                                             f"**кикает участника**\n\n"
                                             f"`{prefix}ban  <@участник> <причина>`\n\n"
                                             f"**банит участника**\n\n"
                                             f"`{prefix}ping`\n"
                                             f"**пинг бота**\n\n"
                                             f"`{prefix}clear <каличество сообщений>`\n"
                                             f"**чистка чата**\n\n"
                                             f"`{prefix}softban`\n"
                                             f"**Банит пользователя на сервере и удаляет все его сообщения за последние 7 дней**\n\n"
                                             f"`{prefix}unban <@участник>`\n"
                                             f"**Разбанить пользователя на сервере**\n\n"
                                             f"`{prefix}mute <@участник> <причина>`\n"
                                             f"**Заглушает пользователя на сервере**\n\n"
                                             f"`{prefix}unmute <@участник>`\n"
                                             f"**РАЗГЛУШИТЬ пользователя на сервере**\n\n"
                                             f"`{prefix}slowmode <СЕКУНДЫ>`\n"
                                             f"**ЗАДЕРЖКА ЧАТА**\n\n")
      
        help_tat = discord.Embed(title=f":shield: | КОММАНДЫ ЗАЩИТЫ", colour=discord.Colour.blue(),
                                 description=f"<ТУТ ПРИМЕРЫ> - НЕ ВВОДИТЬ\n\n"
                                             f"`{prefix}punishment <kick/ban/none>`\n"
                                             f"**Устанавливает краш ботам наказание**\n\n"
                                             f"`{prefix}joinfilter off- выкл    on- вкл`\n"
                                             f"**анти рейд**\n\n"
                                             f"`{prefix}botfilter off- выкл    on- вкл`\n"
                                             f"**банит ботов без галочки**\n\n"
                                             f"`{prefix}antispam off- выкл    on- вкл`\n"
                                             f"**Включает или отключает модуль защиты от спама**.\n\n"
                                             f"`{prefix}antilink off- выкл    on- вкл`\n"
                                             f"**Включает или отключает модуль АНТИ ССЫЛКИ**\n\n"
                                             f"`{prefix}autoban off- выкл    on- вкл`\n"
                                             f"**Включает или отключает модуль автобана (БОТ БАНИТ ВСЕХ КТО ЗАХОДИТ)**\n\n"
                                             f"`{prefix}avatarfilter off- выкл    on- вкл`\n"
                                             f"**банит всех кто без аватарки**\n\n"
                                             f"`{prefix}whitelist <@участник>`\n"
                                             f"**Устанавливает участника на которого будет игнорится защита сервера**\n\n"
                                             f"`{prefix}unwhitelist <@участник>`\n"
                                             f"**убрать участника на которого будет игнорится защита сервера**\n\n"
                                             f"`{prefix}whitelisted`\n"
                                             f"**покажет всех участников на которых будет игнорится защита сервера**\n\n")
        menu.add_button(back_button)
        menu.add_button(next_button)
        menu.add_button(end_button)
        menu.add_page(help)
        menu.add_page(help_general)
        menu.add_page(help_mod)
        menu.add_page(help_tat)
        member_details = []
        for member_embed in member_details:
            menu.add_page(member_embed)
        await menu.start()



def setup(client):
    client.add_cog(Help(client))