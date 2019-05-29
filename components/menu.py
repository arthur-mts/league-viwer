from tkinter import *
from services import menu_service


class Menu:
    def renderWidgets(self):
        self.container = Frame(root)
        self.container["pady"] = 10
        self.container.pack()
        self.titulo = Label(self.container, text="League Viwer")
        self.titulo["font"] = ("Arial", "30", "bold")
        self.titulo.pack()
        self.container2 = Frame(root)
        self.container2["pady"] = 10
        self.container2.pack()
        self.textoAut = Label(self.container2, text="Digite sua chave de acesso: ")
        self.textoAut["font"] = ("20")
        self.textoAut.pack(side=LEFT)
        self.keyEnter = Entry(self.container2)
        self.keyEnter.pack(side=LEFT)
        self.container3 = Frame(root)
        self.container3.pack()
        self.botaoAut = Button(self.container3, text="Autenticar")
        self.botaoAut["command"] = self.actionAutenticar
        self.botaoAut.pack(side=TOP)

    def __init__(self, root):
        self.renderWidgets()

    def actionAutenticar(self):
        if menu_service.validarKey(self.keyEnter.get()):
            self.botaoAut["text"] = "Chave validada!"
            self.botaoAut["bg"] = "green"
        else:
            self.botaoAut["text"] = "Erro de autenticação"
            self.botaoAut["bg"] = "yellow"


root = Tk()
Menu(root)
root.mainloop()
