import urllib.request
import json
import requests
from services import menu_service
from classes import userwatcher
from tkinter import *
from PIL import Image, ImageTk

def iconeInv(inv):
    idIcon = str(getattr(inv, "profileIconId"))
    url ="http://ddragon.leagueoflegends.com/cdn/9.11.1/img/profileicon/" + idIcon+".png"
    print("\n"+idIcon)
    print(url)
    img = urllib.request.urlopen(url)
    return Image.open(img)


def checarInvSalvo():
    try:
        with open("../src/dados/inv.json", "r") as r:
            arquivo = json.load(r)
    except:
        return False
    if "invocador" in arquivo.keys():
        invoc = json.loads(arquivo["invocador"])
        cinv = userwatcher.Summoner(invoc)
        return cinv
    else:
        return False

def salvarInv(inv):
    jinv = {"invocador": json.dumps(inv.__dict__)}
    with open("../src/dados/inv.json", "w", encoding="utf-8") as r:
        json.dump(jinv,r)
        r.close()


def statusServidor(key):
    status = requests.get("https://br1.api.riotgames.com/lol/status/v3/shard-data?api_key="+key).json()
#    print(status)
    res = ["Game: "+ status["services"][0]["status"], "Client: "+ status["services"][3]["status"]
    ]
    return res



def getQueue(idInvocador, key):
    url = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+idInvocador+"?api_key="+key
    print(url)
    res = requests.get(url).json()
    return res

def getFullLeague(leagueId, key):
    url = "https://br1.api.riotgames.com/lol/league/v4/leagues/"+leagueId+"?api_key="+key
    res = requests.get(url).json()
    return res
