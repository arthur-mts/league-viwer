import json
from tkinter import *
from leagueviwer.services import menu_service, api_service
from PIL import ImageTk, Image


class MenuAut:
    def __init__(self, root):
        self.root = root
        self.container = Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0)
        self.container.pack()

        # Redimensionando logo
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)

        self.painel = Label(self.container, image=self.logoImg, highlightbackground="red", highlightcolor="red",
                            highlightthickness=1, bd=0)
        self.painel.image = self.logoImg
        self.painel.pack()

        try:
            with open("../dados.json") as r:
                self.arquivo = json.load(r)
                self.validado = menu_service.validarKey(self.arquivo["senha"]);
        except:
            self.validado = False

        if self.validado:
            self.key = self.arquivo["senha"]
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
        # self.container2 = Frame(self.root, width=100, height=300)
        self.container2 = Frame(self.root, highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0,
                                pady=20, padx=20)
        self.container2.pack(expand=False, side=LEFT)

        self.labelInvocador = Frame(self.container2)
        self.labelInvocador.pack(side=LEFT)
        

        invoc = menu_service.summonerByName("0 Fígurante", self.key)

        icon = api_service.iconeInv(invoc)

        width, height = icon.size
        icon = icon.resize((width // 4, height // 4), Image.ANTIALIAS)
        self.imgIcon  = ImageTk.PhotoImage(icon)
    




        self.labelInvocador.pack(side=LEFT)


        self.labelIcon = Label(self.labelInvocador, image=self.imgIcon)
        self.labelIcon.image = self.imgIcon
        self.labelIcon.pack(side=LEFT)
        
        self.labelNomeInv = Label(self.labelInvocador, text="Invocador", font="termite 15 bold")
        self.labelNomeInv.pack(side=RIGHT)






root = Tk()
root.title("League Viwer")

root.geometry("700x500")
root.update()
MenuAut(root)
root.mainloop()
