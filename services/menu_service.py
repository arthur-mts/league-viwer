import requests
from classes import userwatcher
from classes import champwatcher
url = "https://br1.api.riotgames.com/lol/"
jsonchamps = 0
def summonerByName(name, key):
    end = "summoner/v4/summoners/by-name/"+name+"?api_key="+key
    res = requests.get(url+end).json()
    summner = userwatcher.Summoner(res)
    return summner

def serverStatus(key):
    end = "status/v3/shard-data"+"?api_key="+key
    res = requests.get(url+end).json()
    return "Game: "+ res["services"][0]["status"]+"\nSite: "+res["services"][1]["status"]

def championByName(name, key):
    global jsonchamps
    if(jsonchamps==0):
        jsonchamps = requests.get("http://ddragon.leagueoflegends.com/cdn/9.8.1/data/pt_BR/champion.json").json()
    if not name in jsonchamps["data"]:
        return "ERRO"
    else:
        champ = champwatcher.Champion(jsonchamps["data"][name])
        return champ
