#---------------------------------------------------------------
# Исходный код бота YUriko, он создавался для сервера Campfire.
# https://discord.gg/HeAftd6
# © CC NC-BY 4.0 github.com/Hell13Cat/YUriko
#---------------------------------------------------------------
import requests
import json
import urllib
import time
import urllib
import embed
import random
import discord
from discord.ext import commands


def giphy(text):
    giphyid = "" # Получить токен giphy и заполнить
    textr = text[5:]
    print(textr)
    urlr = "https://api.giphy.com/v1/gifs/search?api_key="+giphyid+"&q="+textr+"&limit=1&offset=0&rating=PG-13&lang=ru"
    data = requests.get(urlr)
    dataj = data.json()
    urlr = dataj["data"][0]["images"]["fixed_height"]["url"]
    return urlr


def shoot(text):
    baseurl = "https://clck.ru/--?url="+text
    fetcher = urllib.request.urlopen(baseurl)
    return str(fetcher.read())[2:-1]

def osu(user, mode, message):
    try:
        osutoken = "" # Получите токен osu и заполните
        urlbase = "https://osu.ppy.sh/api/get_user?k="+osutoken+"&u="+user+"&m="+mode
        data = requests.get(urlbase)
        dataj = data.json()
        dictmod = {"0":"osu!","1":"osu!taiko","2":"osu!catch","3":"osu!mania"}
        imgmod = {"0":"https://i.ibb.co/WtC74pD/mode-osu.png",
        "1":"https://i.ibb.co/h93cmzH/mode-taiko.png",
        "2":"https://i.ibb.co/Sw57WQ7/mode-fruits.png",
        "3":"https://i.ibb.co/b65y5rp/mode-mania.png"
        }
        strmod = dictmod[mode]
        inf = ["https://osu.ppy.sh/users/"+str(dataj[0]["user_id"]), round(float(dataj[0]["pp_raw"])), round(float(dataj[0]["accuracy"]), 2), dataj[0]["playcount"], dataj[0]["pp_rank"], dataj[0]["pp_country_rank"], round(float(dataj[0]["level"]))]
        embe=discord.Embed(title=user, url=inf[0], description=strmod, colour=0xff7eb9)
        embe.set_author(name=embed.usinf(message)[1], icon_url=embed.usinf(message)[0])
        embe.add_field(name="Уровень", value=inf[6], inline=False)
        embe.add_field(name="PP", value=inf[1], inline=False)
        embe.add_field(name="Аккуратность", value=inf[2], inline=False)
        embe.add_field(name="Всего игр", value=inf[3], inline=False)
        embe.add_field(name="Место по миру", value=inf[4], inline=False)
        embe.add_field(name="Место по стране", value=inf[5], inline=False)
        embe.set_thumbnail(url=imgmod[mode])
        return embe
    except:
        return embed.error("Произошло что-то странное. А вы всё правильно ввели?", message)

def animevk(message):
    try:
        vktoken = "" # Получить ВК токен и заполните
        ots = random.choice(range(1,3000))
        baseurl = "https://api.vk.com/method/photos.get?owner_id=-45739204&album_id=wall&rev=0&extended=0&photo_sizes=0&offset="+str(ots)+"&count=1&access_token="+vktoken+"&v=5.92"
        data = requests.get(baseurl)
        dataj = data.json()
        numsize = len(dataj["response"]["items"][0]["sizes"])-1
        Urlread = dataj["response"]["items"][0]["sizes"][numsize]["url"]
        return embed.imganim(Urlread, message)
    except:
        return embed.error("Произошло что-то странное. Возможно ошибка в поиске размера.", message)

def bugurtvk(message):
    try:
        vktoken = "" # Получить ВК токен и заполните
        ots = random.choice(range(1,3000))
        baseurl = "https://api.vk.com/method/wall.get?owner_id=-57536014&count=1&filter=owner&extended=1&offset="+str(ots)+"&access_token="+vktoken+"&v=5.92"
        data=requests.get(baseurl)
        dataj=data.json()
        try:
            numsize = len(dataj["response"]["items"][0]["attachments"][0]["photo"]["sizes"])-1
            Imgurl = dataj["response"]["items"][0]["attachments"][0]["photo"]["sizes"][numsize]["url"]
            Textread = dataj["response"]["items"][0]["text"]
            Likecount = "Колличество лайков в ВК:"+str(dataj["response"]["items"][0]["likes"]["count"])
            return embed.bugpic(Imgurl, Textread, Likecount, message)
        except:
            Textread = dataj["response"]["items"][0]["text"]
            Likecount = "Колличество лайков в ВК:"+str(dataj["response"]["items"][0]["likes"]["count"])
            return embed.bug(Textread, Likecount, message)
    except:
        return embed.error("Произошло что-то странное. Команда принята но не бугуртит.", message)

def campfirevk(message):
    try:
        vktoken = "ba8ae725ba8ae725ba8ae72595bae355e8bba8aba8ae725e62fffc14ad2998601c8a642"
        baseurl = "https://api.vk.com/method/wall.get?owner_id=-106877966&count=1&filter=owner&extended=1&offset=0&access_token="+vktoken+"&v=5.92"
        data=requests.get(baseurl)
        dataj=data.json()
        try:
            numsize = len(dataj["response"]["items"][0]["attachments"][0]["photo"]["sizes"])-1
            Imgurl = dataj["response"]["items"][0]["attachments"][0]["photo"]["sizes"][numsize]["url"]
            Textread = dataj["response"]["items"][0]["text"]
            Likecount = "Колличество лайков под новостью:"+str(dataj["response"]["items"][0]["likes"]["count"])
            return embed.campfire(Imgurl, Textread, Likecount, message)
        except:
            Textread = dataj["response"]["items"][0]["text"]
            Likecount = "Колличество лайков под новостью:"+str(dataj["response"]["items"][0]["likes"]["count"])
            return embed.campfire(Textread, Likecount, message)
    except:
        return embed.error("DEUS VULT", message)