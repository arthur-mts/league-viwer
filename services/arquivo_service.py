import json


def jsonExiste():
        try:

        with open("../dados.json") as r:
            arquivo = json.load(r)
