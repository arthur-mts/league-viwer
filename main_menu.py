import requests
from classes import userwatcher
from services import menu_service
from classes import champwatcher

def validarKey(key):
    req = requests.get("https://br1.api.riotgames.com/lol/status/v3/shard-data?api_key="+key).json()
    if("status" in req):
        print("Chave invalida, tente novamente!")
        return False
    else:
        print("Chave validada!")
        return True

invocador = ""
def menu(op):
    summner = 0
    if (op == 0):
        #Sair
        exit()
    elif(op==1):
        #Buscar e salvar um invocador
        nome = str(input("Digite o nome do invocador a ser buscado: "))
        summner = menu_service.summonerByName(nome, minhaKey)
        if(summner == "ERRO"):
            print("Invocador "+nome+" não encontrado!")
            summner = 0
        else:
            print(userwatcher.SummonerToString(summner))
            return summner.name
    elif(op==2):
        #Status do servidor
        print(menu_service.serverStatus(minhaKey))
    elif(op==3):
        #Buscar champion pelo nome
        print("(Digite o nome do campeão sem espaços!)")
        nome = str(input("Digite o nome do campeão: "))
        champ = menu_service.championByName(nome, minhaKey)
        print(champ)
        if(champ == "ERRO"):
            print("Campeão não encontrado! Tente novamente")
        else:
            print(champwatcher.ChampToString(champ))
    elif(op==4):
        print(4)
        #Mostrar ultima partida do invocador buscado
    elif(op==5):
        print(5)
        #Campeao mais jogado do invocador buscado


minhaKey = "0"
print("---league-viwer---")
print("author: Arthur Mauricio")
print("github: https://github.com/punisher077")
while True:
    apiKey = str(input("Digite a sua api key para realizar as consultas:"))
    valido = validarKey(apiKey)
    if(valido):
        minhaKey = apiKey
        break


while True:
    print("---MENU---")
    txtInv = "1- Buscar e salvar invocador"
    txtInv += (" (Invocador salvo: "+invocador+")") if invocador != "" else ""
    print("0- Sair\n"+ txtInv+"\n2- Status do Server\n3- Buscar informações de campeão\n4- Detalhes de partida\n5- Campeão mais jogado")
    op = int(input("Digite uma opção: "))
    invocador = menu(op)
#sumoner = userwatcher.json_to_summoner(service.urlSummonerByName("Yoda"))
#print(userwatcher.SummonertoString(sumoner))
#URL DO JSON DOS CHAMPS: http://ddragon.leagueoflegends.com/cdn/9.8.1/data/pt_BR/champion.json
