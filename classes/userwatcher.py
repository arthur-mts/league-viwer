class Summoner(object):
    def __init__(self, initial_dict):
        for key in initial_dict:
            setattr(self, key, initial_dict[key])


def SummonerToString(sumn):
    res = "Nome: "+sumn.name + "\nLevel: "+ str(sumn.summonerLevel)
    return res
