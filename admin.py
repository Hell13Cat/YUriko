#---------------------------------------------------------------
# Исходный код бота YUriko, он создавался для сервера Campfire.
# https://discord.gg/HeAftd6
# © CC NC-BY 4.0 github.com/Hell13Cat/YUriko
#---------------------------------------------------------------
import os
import psutil
import os
import discord
import embed

def conv(num):
    return str(round((num/2.**20), 2)) + " mb"


def getproc():
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = str(round((py.memory_info()[0]/2.**30), 2)) + " mb"
    return memoryUse


def getram():
    memv = psutil.virtual_memory()
    return [str(conv(float(memv.total))), str(conv(float(memv.used))), str(conv(float(memv.free)))]


def getrom():
    disk = psutil.disk_usage('/')
    return [str(conv(float(disk.total))), str(conv(float(disk.used))), str(conv(float(disk.free)))]


def getservstat(message):
    embe=discord.Embed(title="Статистика", description="Информация о сервере", colour=0x96b2eb)
    embe.set_author(name=embed.usinf(message)[1], icon_url=embed.usinf(message)[0])
    embe.add_field(name="Всего RAM", value=str(getram()[0]), inline=False)
    embe.add_field(name="Используется RAM", value=str(getram()[1]), inline=False)
    embe.add_field(name="Свободно RAM", value=str(getram()[2]), inline=False)
    embe.add_field(name="Скрипт RAM", value=str(getproc()), inline=False)
    embe.add_field(name="Всего ROM", value=str(getrom()[0]), inline=False)
    embe.add_field(name="Используется ROM", value=str(getrom()[1]), inline=False)
    embe.add_field(name="Свободно ROM", value=str(getrom()[2]), inline=False)
    return embe


def help(message):
    embe=discord.Embed(title="Админ помощь", description="Доступ только создателю бота. Базовый префикс этих комманд `y!adm `", colour=0x96b2eb)
    embe.set_author(name=embed.usinf(message)[1], icon_url=embed.usinf(message)[0])
    embe.add_field(name="sys", value="Инфа о компьютере с ботом", inline=False)
    embe.add_field(name="ser", value="Инфа о серверах с этим ботом", inline=False)
    return embe

def ser(message, clients):
    embe=discord.Embed(title="Сервера", description="Список серверов с ботом", colour=0x96b2eb)
    embe.set_author(name=embed.usinf(message)[1], icon_url=embed.usinf(message)[0])
    for guil in clients:
        id = "ID: " + str(guil.id)
        name = str(guil.name)
        embe.add_field(name=name, value=id, inline=False)
    return embe

