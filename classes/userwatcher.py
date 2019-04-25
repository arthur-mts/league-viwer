import requests


class Summoner(object):
    def __init__(self, name, level, idi):
        self.name = name
        self.level = level
        self.idi = idi

def SummonertoString(sumon):
    return "Nome: "+str(sumon.name) +", Level: "+str(sumon.level)+", ID: "+str(sumon.idi)


def json_to_summoner(json_res):
    json_res = dict(json_res)
    name = json_res["name"]
    idi = json_res["id"]
    level = json_res["summonerLevel"]
    return Summoner(name, level, idi)
