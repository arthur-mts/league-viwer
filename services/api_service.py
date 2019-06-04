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
        print(cinv)
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
    print(res)
    return res
