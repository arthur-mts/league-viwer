import requests
from classes import userwatcher
from classes import champwatcher
url = "https://br1.api.riotgames.com/lol/"
jsonchamps = 0


def validarKey(key):
    req = requests.get("https://br1.api.riotgames.com/lol/status/v3/shard-data?api_key=" + key).json()
    return not "status" in req

def generateJsonChamps():
    global jsonchamps
    if(jsonchamps==0):
        jsonchamps = requests.get("http://ddragon.leagueoflegends.com/cdn/9.11.1/data/pt_BR/champion.json").json()

def summonerByName(name, key):
    end = "summoner/v4/summoners/by-name/"+name+"?api_key="+key
    res = requests.get(url+end).json()
    if("status" in res.keys()):
        print("aa")
        return "ERRO"
    else:
        summner = userwatcher.Summoner(res)
        print(summner)
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


#Lista de 3 campeões mais jogados. caso idC so vai retornar as chaves public void onClick(View view) {
def mostPlayedChampions(sumn_id, key, idC = False):
    generateJsonChamps()
    end = "champion-mastery/v4/champion-masteries/by-summoner/"+sumn_id+"?api_key="+key
    res = requests.get(url+end).json()
    champs = []
    print(len(res))
    for key in(jsonchamps["data"].keys()):
        for i in range(3):
            if(jsonchamps["data"][key]["key"] == str(res[i]["championId"])):
                champs.append(jsonchamps["data"][key])

    return [champ["key"] for champ in champs] if idC else champs
