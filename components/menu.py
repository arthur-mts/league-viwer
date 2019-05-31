import json
from tkinter import *
from services import menu_service, api_service
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
            with open("../src/dados/key.json") as r:
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
            with open("../src/dados/key.json", "w", encoding='utf-8') as arquivo:
                json.dump(validado, arquivo)
                arquivo.close()
            self.container2.destroy()
            self.container3.destroy()
            self.renderOpcoes()
        else:
            self.keyEnter.delete(0, END)
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
        self.container2 = Frame(self.root, highlightbackground="red", highlightcolor="red", highlightthickness=1, pady = 20)
#, pady=50, padx=20
        self.container2.pack(side = LEFT)

        self.invocador = api_service.checarInvSalvo()
        if(self.invocador):
            self.renderInvocador()
        else:
            self.renderSalvarInvocador()



            
    def renderInvocador(self):
        icon = api_service.iconeInv(self.invocador)
        width, height = icon.size
        icon = icon.resize((width // 4, height // 4), Image.ANTIALIAS)
        self.imgIcon  = ImageTk.PhotoImage(icon)

        nomeInv = getattr("name", self.invocador)
        self.labelInvocador = Label(self.container2, image=self.imgIcon, text = nomeInv)
        self.labelInvocador.pack(side=LEFT)
        

        #self.labelIcon = Label(self.labelInvocador, image=self.imgIcon)
        #self.labelIcon.image = self.imgIcon
        #self.labelIcon.pack(side=LEFT)
        
        #self.labelNomeInv = Label(self.labelInvocador, text="0 Fígurante", font="termite 15 bold")
        #self.labelNomeInv.pack(side=RIGHT)

       

        

        #invoc = menu_service.summonerByName("0 Fígurante", self.key)

        #icon = api_service.iconeInv(invoc)

        #width, height = icon.size
        #icon = icon.resize((width // 4, height // 4), Image.ANTIALIAS)
        #self.imgIcon  = ImageTk.PhotoImage(icon)
    




        #self.labelInvocador.pack(side=LEFT)


        #self.labelIcon = Label(self.labelInvocador, image=self.imgIcon)
        #self.labelIcon.image = self.imgIcon
        #self.labelIcon.pack(side=LEFT)
        
        #self.labelNomeInv = Label(self.labelInvocador, text="0 Fígurante", font="termite 15 bold")
        #self.labelNomeInv.pack(side=RIGHT)

    def renderSalvarInvocador(self):
        
        self.frameInv = Frame(self.container2)
        #self.frameInv.pack()
        self.labelTxt = Label(self.container2, text = "Digite seu nome invocador: ")
        self.labelTxt["font"] = ("Nerdfont", 10,"bold")
        #self.labelTxt.grid(column = 0, row = 1)
        self.labelTxt.pack(side = LEFT)

        self.inputNome = Entry(self.container2)
        self.inputNome.pack()
        #self.inputNome.grid(column = 2, row = 1)

        #self.frameBot = Frame(self.container2)
        #self.frameBot.grid(row = 2)
        #self.frameBot.pack()

        self.botaoSalvar = Button(self.container2, text="Buscar", anchor = CENTER)
        self.botaoSalvar["command"] = self.actionSalvarInvoc
        self.botaoSalvar.pack(anchor = CENTER)
        #self.botaoSalvar.grid(row = 2, column = 1)

        
    
    def actionSalvarInvoc(self):
        nome = self.inputNome.get()
        invoc = menu_service.summonerByName(nome, self.key) 
        if(invoc == "ERRO"):
            self.inputNome.delete(0,END)
            self.botaoSalvar["bg"] = "red"
            self.botaoSalvar["text"] = "Invocador nao encontrado"
        else:
            self.botaoSalvar["bg"] = "green"
            self.botaoSalvar["text"] = "Salvo!"
            api_service.salvarInv(invoc)
            






root = Tk()
root.title("League Viwer")

root.geometry("700x500")
root.update()
MenuAut(root)
root.mainloop()
