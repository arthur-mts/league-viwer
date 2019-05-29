import json
from tkinter import *
from services import menu_service


class MenuAut:
    def __init__(self, root):
        self.root = root
        self.container = Frame(root)
        self.container["pady"] = 10
        self.container.pack()
        self.titulo = Label(self.container, text="League Viwer")
        self.titulo["font"] = ("Arial", "30", "bold")
        self.titulo.pack()

        try:
            with open("../dados.json") as r:
                self.arquivo = json.load(r)
                self.validado = menu_service.validarKey(self.arquivo["senha"]);
        except:
            self.validado = False

        if self.validado:
            self.renderOpcoes()
        else:
            self.renderAutenticar()

    def actionAutenticar(self):
        self.key = self.keyEnter.get()
        if menu_service.validarKey(self.key):
            self.botaoAut["text"] = "Chave validada!"
            self.botaoAut["bg"] = "green"
            validado = {'senha': self.key}
            with open("../dados.json", "w", encoding='utf-8') as arquivo:
                json.dump(validado, arquivo)
                arquivo.close()
            self.container2.destroy()
            self.container3.destroy()
            self.renderOpcoes()
        else:
            self.botaoAut["text"] = "Erro de autenticação"
            self.botaoAut["bg"] = "yellow"

    def renderAutenticar(self):
        self.container2 = Frame(self.root)
        self.container2["pady"] = 10
        self.container2.pack()
        self.textoAut = Label(self.container2, text="Digite sua chave de acesso: ")
        self.textoAut["font"] = ("20")
        self.textoAut.pack(side=LEFT)
        self.keyEnter = Entry(self.container2)
        self.keyEnter.pack(side=LEFT)
        self.container3 = Frame(self.root)
        self.container3.pack()
        self.botaoAut = Button(self.container3, text="Autenticar")
        self.botaoAut["command"] = self.actionAutenticar
        self.botaoAut.pack(side=TOP)

    def renderOpcoes(self):
        self.container2 = Frame(self.root)
        self.container2["pady"] = 10
        self.container2.pack()
        self.textoOps = Label(self.container2, text="Ver invocador etc")
        self.textoOps.pack(side=LEFT)



root = Tk()
root.title("League Viwer")
MenuAut(root)
root.mainloop()

