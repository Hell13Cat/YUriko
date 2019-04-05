import discord
import time
from discord.ext import commands

def usinf(message):
    urlav= "https://cdn.discordapp.com/avatars/"+str(message.author.id)+"/"+message.author.avatar+".png"
    return [urlav, str(message.author)]

def minimal(Text, message):
    embed=discord.Embed(description=Text, colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    return embed

def base(Title, Descrip, message):
    embed=discord.Embed(title=Title, description=Descrip, colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    return embed

def url(Url, Title, Descrip, message):
    embed=discord.Embed(title=Title, description=Descrip, url=Url, colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    return embed

def img(Imgurl, message):
    embed=discord.Embed(colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    embed.set_image(url=Imgurl)
    return embed

def imganim(Imgurl, message):
    embed=discord.Embed(title="Арт со стены группы <<Animart - милые аниме арты :3>>", url="https://vk.com/animart_pub", colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    embed.set_image(url=Imgurl)
    return embed

def bugpic(Imgurl, Textbug, Liketext, message):
    embed=discord.Embed(title="Бугурт со стены группы БУГУРТ-ТРЕД", url="https://vk.com/bugurt_thread", description=Textbug, colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    embed.set_footer(text=Liketext)
    embed.set_image(url=Imgurl)
    return embed

def bug(Textbug, Liketext, message):
    embed=discord.Embed(title="Бугурт со стены группы БУГУРТ-ТРЕД", url="https://vk.com/bugurt_thread", description=Textbug, colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    embed.set_footer(text=Liketext)
    return embed

def campfire(Textbug, Liketext, message):
    embed=discord.Embed(title="Последняя новость о Campfire", description=Textbug, colour=0x96b2eb)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    embed.set_footer(text=Liketext)
    return embed

def error(Text, message):
    embed=discord.Embed(title="Ошибка", description=Text, colour=0xff0000)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    return embed


def baseosu(Title, Descrip, message):
    embed=discord.Embed(title=Title, description=Descrip, colour=0xff7eb9)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    embed.set_thumbnail(url="https://i.ibb.co/N6mBFdD/Osu-Logo-2015.png")
    return embed

def help(num, message):
    if num=="0":
        embed=discord.Embed(title="Помощь 1 страница", description="Тут указаны все комманды бота YUriko. Префикс `y!`", colour=0x96b2eb)
        embed.add_field(name="gif", value="Поиск гифок ботом. После команды писать поисковый запрос.", inline=False)
        embed.add_field(name="ping", value="Проверка работы бота.", inline=False)
        embed.add_field(name="time", value="Время по МСК.", inline=False)
        embed.add_field(name="shot", value="Сокращение ссылок. После команды введите url.", inline=False)
        embed.add_field(name="8ball", value="Да или нет? После команды ведите вопрос.", inline=False)
        embed.add_field(name="osu", value="Подробнее osu help", inline=False)
        embed.add_field(name="a", value="Рандомная аниме картинка", inline=False)
        embed.add_field(name="y!help 2", value="Вторая страница->>>>>", inline=False)
    elif num=="1":
        embed=discord.Embed(title="Помощь 2 страница", description="Тут указаны все комманды бота YUriko. Префикс `y!`", colour=0x96b2eb)
        embed.add_field(name="b", value="Рандомный бугурт", inline=False)
        embed.add_field(name="campfire", value="Последняя новость о Campfire", inline=False)
        embed.add_field(name="invite", value="Пригласить бота на свой сервер", inline=False)
    embed.set_author(name=usinf(message)[1], icon_url=usinf(message)[0])
    return embed
