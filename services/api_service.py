import urllib.request, json, os, requests, operator, collections
from services import menu_service
from classes import userwatcher
from tkinter import *
from PIL import Image, ImageTk



def iconeInv(inv):
    #Checar se icone do invocador já existe
    imgDir = os.listdir("../src/img/")
    imgFile = None
    idIcon = str(getattr(inv, "profileIconId"))
    for f in imgDir:
        if "icon" in f:
            imgFile = f
    if imgFile and idIcon in imgFile:
        img_filename = "../src/img/"+imgFile
        img = Image.open(img_filename)
        return img
    else:
        url ="http://ddragon.leagueoflegends.com/cdn/9.12.1/img/profileicon/" + idIcon+".png"
        getImg = urllib.request.urlopen(url)
        img = Image.open(getImg)
        if imgFile:
            os.remove("../src/img/"+imgFile)
        img.save(("%s/icone"+idIcon+".png") % "../src/img/")
        return img


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
    res = ["Game: " + status["services"][0]["status"].capitalize(), "Cliente: " +
           status["services"][3]["status"].capitalize()]
    return res



def getQueue(idInvocador, key):
    url = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+idInvocador+"?api_key="+key
    res = requests.get(url).json()
    return res

def getFullLeague(leagueId, key):
    url = "https://br1.api.riotgames.com/lol/league/v4/leagues/"+leagueId+"?api_key="+key
    res = requests.get(url).json()
    return res


def getLastMatches(invId, key):
    #?endIndex=25: quantidade de partidas para serem capturadas
    url = "https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+invId+"?endIndex=25&api_key="+key
    res = requests.get(url).json()
    listMat = []
    #Baixar resultados das partidas seperadamente
    for mat in res["matches"]:
        urlMat = "https://br1.api.riotgames.com/lol/match/v4/matches/"+str(mat["gameId"])+"?api_key="+key 
        resMat = requests.get(urlMat).json()
        listMat.append(resMat)
        
    return listMat





#Pegar partidas jogadas por um invocador com determinados campeoes
def filterMatchesByChampions(key, matches, idChampions, inv):
    #Vitorias e derrotas com o campeão
    winsLosesByChampion = {idChampions[0]: [0,0], idChampions[1]: [0,0], idChampions[2]: [0,0]}
    for mat in matches:
        
        idPlayerInMatch = None

        #Encontrar o ID do invocador dentro da partida
        for player in mat["participantIdentities"]:
            if player["player"]["summonerName"] == inv.name:
                idPlayerInMatch = int(player["participantId"])
                break


        #Pegar informações individuais do invocador na partida
        playerStatusInMatch = mat["participants"][idPlayerInMatch-1]
        idChampionInMatch = str(playerStatusInMatch["championId"])


        #Verificar se o campeão escolhido na partida é um dos mains do invocador
        if idChampionInMatch in idChampions:
            #Verificar se o invocador ganhou ou perdeu o jogo
            win = (mat["teams"][0]["win"] if idPlayerInMatch <= 5 else mat["teams"][1]["win"]) == "Win"
            if win:
                winsLosesByChampion[idChampionInMatch][0] += 1
            else:
                winsLosesByChampion[idChampionInMatch][1] += 1
    return winsLosesByChampion

#Capturar ids dos campeões mais jogados nas ultimas 20 partidas
def filterMostPlayedChampions(key, matches, inv):
    idChampions = []
    for mat in matches:
        idPlayerInMatch = None

        #Encontrar o ID do invocador dentro da partida
        for player in mat["participantIdentities"]:
            if player["player"]["summonerName"] == inv.name:
                
                idPlayerInMatch = int(player["participantId"])
                break


        #Pegar informações individuais do invocador na partida
        playerStatusInMatch = mat["participants"][idPlayerInMatch-1]
        idChampionInMatch = str(playerStatusInMatch["championId"])
        idChampions.append(idChampionInMatch)
        
    mostPlayedDict = dict()
    championsU = list(set(idChampions))
    mostPlayed = [idChampions.count(i) for i in championsU]
    mostPlayedChampionsId = []

    for j in range(len(championsU)):
        mostPlayedDict[championsU[j]] = mostPlayed[j]

    sortedDict = dict()
    #Colocando os items em ordem crescente de vitorias
    for it in sorted(mostPlayedDict.items(), key=operator.itemgetter(1))[::-1]:
        mostPlayedChampionsId.append(it[0])

    return mostPlayedChampionsId[:3]

def getIconByName(nameC):
    url = "https://ddragon.leagueoflegends.com/cdn/9.12.1/img/champion/"+nameC+".png"
    getImg = urllib.request.urlopen(url)
    return Image.open(getImg)

def getMatchStatus(key, inv):
    #Pegar a ultima partida em summoners rift
    match = None    
    url = "https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+inv.accountId+"?endIndex=25&api_key="+key
    res = requests.get(url).json()
    for mat in res["matches"]:
        urlMat = "https://br1.api.riotgames.com/lol/match/v4/matches/"+str(mat["gameId"])+"?api_key="+key 
        resMat = requests.get(urlMat).json()
        if resMat["mapId"] == 11:
            match = resMat
            break
    if not match:
        return False
    else:
        idPlayerInMatch = None
        for player in match["participantIdentities"]:
            if player["player"]["summonerName"] == inv.name:
                idPlayerInMatch = int(player["participantId"])
                break
        # 100 para azul 200 para vermelho

        team = match["participants"][idPlayerInMatch - 1]["teamId"]
        won = match["participants"][idPlayerInMatch - 1]["stats"]["win"]
        gold_spent = match["participants"][idPlayerInMatch - 1]["stats"]["goldSpent"]
        gold_earned = match["participants"][idPlayerInMatch - 1]["stats"]["goldEarned"]
        killed = match["participants"][idPlayerInMatch - 1]["stats"]["kills"]
        died = match["participants"][idPlayerInMatch - 1]["stats"]["deaths"]
        assisted = match["participants"][idPlayerInMatch - 1]["stats"]["assists"]
        result = "{}/{}/{}".format(killed, died, assisted)
        minions = match["participants"][idPlayerInMatch - 1]["stats"]["totalMinionsKilled"]
        neutral = match["participants"][idPlayerInMatch - 1]["stats"]["neutralMinionsKilled"]
        champion = get_champion(match["participants"][idPlayerInMatch - 1]["championId"])

        # Timeline da partida capturado
        timelines = requests.get("https://br1.api.riotgames.com/lol/match/v4/timelines/by-match/"+str(match["gameId"])+"?api_key="+key).json()

        # Criar dicionário com todas as kills do jogo {killer: idKiller, killed: idKilled
        # , teamKilled: "blue/red", teamKilled: "blue/red", x: coordenadax, y: corrdy}
        kills = []
        for frame in timelines["frames"]:
            for event in frame["events"]:
                if event["type"] == "CHAMPION_KILL":   
                    kill = {"x": event["position"]["x"], "y": event["position"]["y"]
                            , "killerId": event["killerId"], "killedId": event["victimId"]}
                    kills.append(kill)
        return [kills, team, idPlayerInMatch, won, gold_spent, gold_earned, result, minions, neutral, champion]


def get_champion(number):
    champions = requests.get("http://ddragon.leagueoflegends.com/cdn/9.11.1/data/pt_BR/champion.json").json()
    for name in champions["data"].keys():
        if str(number) == champions["data"][name]["key"]:
            return champions["data"][name]["name"]
