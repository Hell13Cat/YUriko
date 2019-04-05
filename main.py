#---------------------------------------------------------------
# Исходный код бота YUriko, он создавался для сервера Campfire.
# https://discord.gg/HeAftd6
# © CC NC-BY 4.0 github.com/Hell13Cat/YUriko
#---------------------------------------------------------------
# Настройка на:
# main.py строки 28, 162
# api.py строки 13, 30, 57, 70
# Требуются discord.py-rw, discord.ext, requests, urllib, psutil
#---------------------------------------------------------------
import discord
import time
import random
import api
from multiprocessing import Process
from discord.ext import commands
import embed
import admin


def rtime():
 return str(time.ctime(time.time()))




print(time.ctime(time.time()))
DISCORD_BOT_TOKEN = '' #Заполнить токен бота
client = discord.Client()



@client.event
async def on_ready():
 print('Logged in as')
 print(client.user.name)
 print(client.user.id)
 print('------')

  


@client.event
async def on_message(message, *msg):
  msg = message.content.split(" ")


  if msg[0] == "y!gif":
    try:
      print(msg)
      urlrd = api.giphy(message.content)
      await message.delete()
      channel = message.channel 
      await channel.send(embed=embed.img(urlrd, message))
    except:
      await message.delete()
      channel = message.channel 
      await channel.send(embed=embed.error("Ошибка запроса", message))



  if msg[0] == "y!ping":
    print(msg)
    await message.delete()
    channel = message.channel
    await channel.send(embed=embed.minimal("PONG!!!!", message))


  if msg[0] == "y!time":
    print(msg)
    time12 = time.ctime(time.time()).split(" ")[-2]
    time13 = time12
    await message.delete()
    channel = message.channel
    await channel.send(embed=embed.base("Текущее время по МСК", time13, message))

  if msg[0] == "y!shot":
    try:
      urlrd = api.shoot(msg[1])
      await message.delete()
      channel = message.channel 
      await channel.send(embed=embed.minimal(urlrd, message))
    except:
      await message.delete()
      channel = message.channel 
      await channel.send(embed=embed.error("Ошибка запроса", message))

  if msg[0] == "y!osu":
    if msg[1] == "help":
      text = """`y!osu <Ник> <Мод числом>`
      Моды:
      0 - osu!
      1 = osu!taiko
      2 = osu!catch
      3 = osu!mania"""
      await message.delete()
      channel = message.channel 
      await channel.send(embed=embed.baseosu("Инструкция", text, message))
    else:
      try:
        await message.delete()
        channel = message.channel
        await channel.send(embed=api.osu(msg[1], msg[2], message))
      except:
        await message.delete()
        channel = message.channel 
        await channel.send(embed=embed.error("Ошибка ввода запроса", message))
  
  if msg[0] == "y!8ball":
    await message.delete()
    try:
      channel = message.channel
      text = str(message.content)[8:]
      await channel.send(embed=embed.base(random.choice(["Да","Нет","Да","Нет"]), text, message))
    except:
      channel = message.channel
      await channel.send(embed=embed.error("Ошибка ввода запроса", message))


  if msg[0] == "y!help":
    try:
      com = str(message.content)
      dicthelp = {"y!help":"0", "y!help 2":"1"}
      num = dicthelp[com]
      await message.delete()
      channel = message.channel
      await channel.send(embed=embed.help(num, message))
    except:
      await message.delete()
      channel = message.channel 
      await channel.send(embed=embed.error("Помощь не получена", message))


  if msg[0] == "y!b":
    await message.delete()
    channel = message.channel
    await channel.send(embed=api.bugurtvk(message))


  if msg[0] == "y!campfire":
    await message.delete()
    channel = message.channel
    await channel.send(embed=api.campfirevk(message))


  if msg[0] == "y!a":
    await message.delete()
    channel = message.channel
    await channel.send(embed=api.campfirevk(message))

  if msg[0] == "y!invite":
    await message.delete()
    channel = message.channel
    UrlY = "https://discordapp.com/api/oauth2/authorize?client_id="+client.user.id+"&permissions=537259072&scope=bot"
    await channel.send(embed=embed.url(UrlY, "Пригласить бота", "Щелкните по надписи чтобы пригласить бота", message))

  if (msg[0] == "y!test" and str(message.author.id) == "501228178707054592") == True :
    pass
  

  if msg[0] == "y!adm":
    if str(message.author.id) == "": #Заполнить id создателя
      try:
        if msg[1] == "sys":
          await message.delete()
          channel = message.channel
          await channel.send(embed = admin.getservstat(message))
        elif msg[1] == "help":
          await message.delete()
          channel = message.channel
          await channel.send(embed = admin.help(message))
        elif msg[1] == "ser":
          await message.delete()
          channel = message.channel
          await channel.send(embed = admin.ser(message, client.guilds))
        else:
          await message.delete()
          channel = message.channel 
          await channel.send(embed=embed.error("Ошибка! Аргументы: help, svs, sus", message))
      except:
        await message.delete()
        channel = message.channel 
        await channel.send(embed=embed.error("Ошибка! Аргументы: svs, sus", message))
    else:
      await message.delete()
      channel = message.channel 
      await channel.send(embed=embed.error("К команде имеет доступ только создатель бота", message))

client.run(DISCORD_BOT_TOKEN)