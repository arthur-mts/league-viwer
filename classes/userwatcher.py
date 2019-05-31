class Summoner(object):
    def __init__(self, initial_dict):
        for key in initial_dict.keys():
            print(key)
            setattr(self, key, initial_dict[key])


def SummonerToString(sumn):
    res = "Nome: "+sumn.name + "\nLevel: "+ str(sumn.summonerLevel)
    return res

def SummonerToStringTotal(sumn):
    res = ""
    attr = [str(a) for a in dir(sumn) if not a.startswith('__') and not callable(getattr(sumn,a))]
    for i in attr:
        res+= i +": "+ str(getattr(sumn, i))+"\n"
    return res[:-1]
