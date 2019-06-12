import requests
import json

URL = "https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"
image = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/"
ending = "_0.jpg"
champions = requests.get("http://ddragon.leagueoflegends.com/cdn/9.11.1/data/pt_BR/champion.json").json()


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


def get_image(name):
    return image + name + ending


def update_info(player, data, array, key):
    dictionary = most_played_champions(player.id, key)

    data[player.name] = dictionary
    array[player.name] = [dictionary[i]["ID"] for i in range(3)]

    with open("../src/champions_data.json", "w") as file:
        json.dump(data, file, indent=3)

    with open("../src/champions.json", "w") as file:
        json.dump(array, file, indent=3)
