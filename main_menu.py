import requests
from classes import userwatcher
from services import menu_service
from classes import champwatcher



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
            print("\033[91mInvocador "+nome+" não encontrado!\033[0m")
        else:
            print(userwatcher.SummonerToString(summner))
            global invocador
            invocador = summner
    elif(op==2):
        #Status do servidor
        print(menu_service.serverStatus(minhaKey))
    elif(op==3):
        #Buscar champion pelo nome
        nome = str(input("Digite o nome do campeão: "))
        champ = menu_service.championByName(nome, minhaKey)
        if(champ == "ERRO"):
            print("\033[91mCampeão não encontrado! Tente novamente\033[0m")
        else:
            print(champwatcher.ChampToString(champ))
    elif(op==4):
        print(4)
        #Mostrar ultima partida do invocador buscado
    elif(op==5):
        if(not invocador):
            print("\033[91mPrimeiro salve um invocador!\033[0m")
        else:
            print(menu_service.mostPlayedChampions(invocador.id, minhaKey))
        #Campeao mais jogado do invocador buscado
    elif(op==6):
        #Detalhes do invocador
        if(not invocador):
            print("\033[91mPrimeiro salve um invocador!\033[0m")
        else:
            print(userwatcher.SummonerToStringTotal(invocador))
    else:
        print("\033[91mOpção invalida!\033[0m")
minhaKey = "0"
print("\033[1m---LEAGUE-VIWER---\nauthor: Arthur Mauricio\ngithub: https://github.com/punisher077\033[0m")
while True:
    apiKey = str(input("Digite a sua api key para realizar as consultas:"))
    valido = validarKey(apiKey)
    if(valido):
        minhaKey = apiKey
        break

invocador = None
while True:
    print("---MENU---")
    txtInv = "1- Buscar e salvar invocador"
    txtInv += (" (Invocador salvo: \033[94m"+invocador.name+"\033[0m)") if(invocador!=None)  else ""
    print("0- Sair\n"+ txtInv+"\n2- Status do Server\n3- Buscar informações de campeão\n4- Detalhes de partida\n5- Campeão mais jogado\n6- Dados do invocador")
    op = int(input("Digite uma opção: "))
    menu(op)
#print(userwatcher.SummonertoString(sumoner))
# URL DO JSON DOS CHAMPS: http://ddragon.leagueoflegends.com/cdn/9.11.1/data/pt_BR/champion.json

# URL DAS SPLASH https://ddragon.leagueoflegends.com/cdn/img/champion/splash/AurelionSol_0.jpg

# URL DOS ICONES https://ddragon.leagueoflegends.com/cdn/img/champion/tiles/AurelionSol_0.jpg
