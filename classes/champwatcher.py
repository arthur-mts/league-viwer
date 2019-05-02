class Champion(object):
    #O construtor da classe Champion irá receber um dicionario com todos os atributos.
    #Esse dicionario sera fornecido pelo json obtido por uma consulta get em url.
    def __init__(self, initial_dict):
        for key in initial_dict:
            setattr(self, key, initial_dict[key])

def ChampToString(champ):
    res = "Nome: \033[93m"+champ.name+", "+champ.title+"\033[0m.\nTipo(s):\033[96m"+str(champ.tags[0])
    res+="\033[0m and \033[96m"+ champ.tags[1]+"\033[0m.\n" if (len(champ.tags)>1) else "\033[0m.\n"
    res += "Vida base: \033[91m" + str(champ.stats["hp"])+"\033[0m HP.\nArmadura base: \033[91m"+str(champ.stats["armor"])+"\033[0m.\nDano de ataque base:\033[91m"+str(champ.stats["attackdamage"])+" AD\033[0m.\nVelocidade de atque base: \033[91m"+str(champ.stats["attackspeed"])+"\033[0m.\nResumo: "+champ.blurb
    return(res)
