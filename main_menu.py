import requests
from classes import userwatcher

def validarKey(key):
    req = requests.get("https://br1.api.riotgames.com/lol/status/v3/shard-data?api_key="+key).json()
    if("status" in req):
        print("Chave invalida, tente novamente!")
        return False
    else:
        print("Chave validada!")
        return True

def menu(op):
    if (op == 0):
        exit()
    elif(op==1):
    #Bucar invocador
        return services.summonerByName()
    elif(op==2):
    #Status do servidor
        print(services.serverStatus())
    elif(op==3)

minhaKey = "0"
print("---League-Watcher---")
print("author: Arthur Mauricio")
print("github: https://github.com/punisher077")
while True:
    apiKey = str(input("Digite a sua api key para realizar as consultas:"))
    valido = validarKey(apiKey)
    if(valido):
        minhaKey = apiKey
        break


#sumoner = userwatcher.json_to_summoner(service.urlSummonerByName("Yoda"))
#print(userwatcher.SummonertoString(sumoner))
#URL DO JSON DOS CHAMPS: http://ddragon.leagueoflegends.com/cdn/9.8.1/data/pt_BR/champion.json
