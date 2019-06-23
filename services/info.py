import requests
import json

# Constantes de links
URL = "https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"
image = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"
ending = "_0.jpg"
champions = requests.get("http://ddragon.leagueoflegends.com/cdn/9.11.1/data/pt_BR/champion.json").json()


# Pegar campeões mais jogados
def most_played_champions(summoner, key):
    end = summoner + "?api_key=" + key
    result = requests.get(URL + end).json()
    dictionary = [{}, {}, {}]
    for key in (champions["data"].keys()):
        for i in range(3):
            if champions["data"][key]["key"] == str(result[i]["championId"]):
                dictionary[i]["Name"] = champions["data"][key]["name"]
                dictionary[i]["Title"] = champions["data"][key]["title"]
                dictionary[i]["Mastery"] = result[i]["championLevel"]
                dictionary[i]["Score"] = result[i]["championPoints"]
                dictionary[i]["Chest"] = result[i]["chestGranted"]
                dictionary[i]["Tags"] = champions["data"][key]["tags"]
                dictionary[i]["ID"] = result[i]["championId"]
                dictionary[i]["Image"] = get_image(champions["data"][key]["id"])
    return dictionary


# Pegar link da imagem
def get_image(name):
    return image + name + ending


# Atualizar informações
def update_info(player, key):
    data = dict()
    array = dict()
    dictionary = most_played_champions(player.id, key)

    data[player.name] = dictionary
    array[player.name] = [dictionary[i]["ID"] for i in range(3)]

    with open("../src/dados/champions.json", "w") as file:
        json.dump(data, file, indent=3)

    with open("../src/dados/IDs.json", "w") as file:
        json.dump(array, file, indent=3)


# Pegar dados dos campeões
def get_data():
    try:
        with open("../src/dados/champions.json", "r") as file:
            data = json.load(file)
            file.close()
        return data
    except:
        with open("../src/dados/champions.json", "w") as file:
            file.write("{}")
            file.close()


# Pegar nome do invocador
def get_name():
    with open("../src/dados/inv.json") as file:
        dictionary = json.load(file)
        file.close()
    player = json.loads(dictionary["invocador"])
    return player["name"]


# Pegar IDs dos campeões mais jogados
def get_array():
    try:
        with open("../src/dados/IDs.json", "r") as file:
            array = json.load(file)
            file.close()
        return array
    except:
        with open("../src/dados/IDs.json", "w") as file:
            file.write("{}")
            file.close()


# Pegar chave de acesso
def get_key():
    with open("../src/dados/key.json") as file:
        key = json.load(file)
        file.close()
    return key["senha"]
