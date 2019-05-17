import requests
from classes import userwatcher
from classes import champwatcher
url = "https://br1.api.riotgames.com/lol/"
jsonchamps = 0

def generateJsonChamps():
    global jsonchamps
    if(jsonchamps==0):
        jsonchamps = requests.get("http://ddragon.leagueoflegends.com/cdn/9.10.1/data/pt_BR/champion.json").json()

def summonerByName(name, key):
    end = "summoner/v4/summoners/by-name/"+name+"?api_key="+key
    res = requests.get(url+end).json()
    if("status" in res.keys()):
        return "ERRO"
    else:
        summner = userwatcher.Summoner(res)
        return summner

def serverStatus(key):
    end = "status/v3/shard-data"+"?api_key="+key
    res = requests.get(url+end).json()
    return "Game: "+ res["services"][0]["status"]+"\nSite: "+res["services"][1]["status"]

def championByName(name, key):
    generateJsonChamps()
    find, champ = False, 0
    for j in jsonchamps["data"].keys():
        if(name.upper() == j.upper()):
            champ = champwatcher.Champion(jsonchamps["data"][name])
            find = True
    return champ if (find) else "ERRO"



def mostPlayedChampions(sumn_id, key):
    generateJsonChamps()
    end = "champion-mastery/v4/champion-masteries/by-summoner/"+sumn_id+"?api_key="+key
    res = requests.get(url+end).json()
    txt  = ""
    for key in(jsonchamps["data"].keys()):
        for i in range(3):
            if(jsonchamps["data"][key]["key"] == str(res[i]["championId"])):
                txt += "--------------------------\n"+"\033[1m"+(jsonchamps["data"][key]["name"])+"\033[0m"+"\n\033[4mMaestria\033[0m "+str(res[i]["championLevel"])+"\n\033[4mPontos de maestria:\033[0m "+str(res[i]["championPoints"])+"\033[4m\nBaú ganho:\033[0m "+str(res[i]["chestGranted"])+"\n--------------------------\n"
    return(txt)
