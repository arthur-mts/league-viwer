import urllib.request
import json
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
            invoc = arquivo["invocador"]
            return userwatcher.Summoner(invoc)
    except:
        return False

def salvarInv(inv):
    jinv = {"invocador": json.dumps(inv.__dict__)}
    with open("../src/dados/inv.json", "w", encoding="utf-8") as r:
        json.dump(jinv,r)
        r.close()
        
