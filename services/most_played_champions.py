import requests

URL = "https://br1.api.riotgames.com/lol/"
image = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"
ending = "_0.jpg"
images = []
champions = requests.get("http://ddragon.leagueoflegends.com/cdn/9.10.1/data/pt_BR/champion.json").json()


def most_played_champions(summoner, key):
    # champions = requests.get("http://ddragon.leagueoflegends.com/cdn/9.11.1/data/pt_BR/champion.json").json()
    end = "champion-mastery/v4/champion-masteries/by-summoner/" + summoner + "?api_key=" + key
    result = requests.get(URL + end).json()
    dictionary = [{}, {}, {}]
    for key in (champions["data"].keys()):
        for i in range(3):
            if champions["data"][key]["key"] == str(result[i]["championId"]):
                dictionary[i]["Name"] = champions["data"][key]["name"]
                dictionary[i]["Mastery"] = result[i]["championLevel"]
                dictionary[i]["Score"] = result[i]["championPoints"]
                dictionary[i]["Chest"] = result[i]["chestGranted"]
                dictionary[i]["Image"] = get_image(champions["data"][key]["id"])
    return dictionary


def get_image(name):
    return image + name + ending
