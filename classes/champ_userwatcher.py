class Champion(object):
    #O construtor da classe Champion irá receber um dicionario com todos os atributos.
    #Esse dicionario sera fornecido pelo json obtido por uma consulta get em url.
    def __init__(self, initial_dict):
        for key in initial_dict:
            setattr(self, key, initial_dict[key])
