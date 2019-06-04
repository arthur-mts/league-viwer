import requests
from services import menu_service

URL = "https://br1.api.riotgames.com/lol/"
image = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"
ending = "_0.jpg"
champions = menu_service.generateJsonChamps()


def most_played_champions(summoner, key):
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
