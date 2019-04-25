import requests, json
print("~~LEAGUE COACH~~\nBy: punihser077")
token = "RGAPI-7755cba1-3ad5-4ae1-9409-7815c284a46c"
regiao = "br1"
invocador = str(input("Digite o seu nickname:"))
url = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+invocador+"?api_key="+token
res = requests.get(url).json()
print(res)
