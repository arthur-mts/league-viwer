import urllib.request
from classes import userwatcher, champwatcher
from tkinter import *
from PIL import Image, ImageTk

def iconeInv(inv):
    idIcon = str(getattr(inv, "profileIconId"))
    url ="http://ddragon.leagueoflegends.com/cdn/9.11.1/img/profileicon/" + idIcon+".png"
    print("\n"+idIcon)
    print(url)
    img = urllib.request.urlopen(url)
    return Image.open(img)
