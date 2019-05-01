class Champion(object):
    #O construtor da classe Champion irá receber um dicionario com todos os atributos.
    #Esse dicionario sera fornecido pelo json obtido por uma consulta get em url.
    def __init__(self, initial_dict):
        for key in initial_dict:
            setattr(self, key, initial_dict[key])

def ChampToString(champ):
    res = "Nome: "+champ.name+", "+champ.title+".\nTipo(s):"+str(champ.tags[0])
    res+=" and "+ champ.tags[1]+".\n" if (len(champ.tags)>1) else ".\n"
    res += "Vida base: " + str(champ.stats["hp"])+" HP.\nArmadura base: "+str(champ.stats["armor"])+".\nDano de ataque base: "+str(champ.stats["attackdamage"])+" AD.\nVelocidade de atque base: "+str(champ.stats["attackspeed"])+".\nResumo: "+champ.blurb
    return(res)
