import json
import os
from tkinter import *
#Não consigo abrir o arquivo da mesma pasta no linux. talvez tenha q tirar na versao final
from components import viewInvocador, viewEstatistica
from services import menu_service, api_service
from PIL import ImageTk, Image

global bg
bg = "#182422"

global fg
fg = "#F3E171"


class MenuAut:
    def __init__(self):
        #Renderizar imagem de titulo
        self.root = Tk()
        self.root.title("League Viwer")
        self.root.resizable(False, False)
        self.root.geometry("900x700")
        self.root["background"] = bg
        self.root.update()
 
        self.container = Frame(self.root, bg = bg)
        self.container.grid(row = 0, column = 2, columnspan = 2)
        self.container.place(x = 340, y = 0)
        # Redimensionando logo
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)

        self.painel = Label(self.container, image=self.logoImg, bg = bg)
        self.painel.image = self.logoImg
        self.painel.grid_columnconfigure(0, weight = 1)
        self.painel.grid_rowconfigure(0, weight = 1)
        self.painel.pack(anchor=W, fill=Y, expand=False, side=LEFT)

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
            with open("../src/dados/key.json", "w+", encoding='utf-8') as arquivo:
                json.dump(validado, arquivo)
                arquivo.close()
            self.container2.destroy()
            self.renderOpcoes()
        else:
            self.keyEnter.delete(0, END)
            self.botaoAut["text"] = "Erro de autenticação"
            self.botaoAut["bg"] = "yellow"

    def renderAutenticar(self):
        self.container2 = Frame(self.root, bg = bg)
        self.container2["pady"] = 10
        self.container2.grid(column = 2, row = 0, columnspan = 2)
        self.container2.place(x= 250, y = 200)
        self.textoAut = Label(self.container2, text="Digite sua chave de acesso: ", bg = bg, width = 40)
        self.textoAut["font"] = ("20")
        self.textoAut.grid(column = 0, row = 0, sticky = E)
        self.keyEnter = Entry(self.container2, fg = fg, width = 40)
        self.keyEnter.grid(column = 0, row = 1, pady = 20)
        self.botaoAut = Button(self.container2, text="Autenticar")
        self.botaoAut["command"] = self.actionAutenticar
        self.botaoAut.grid(row = 2)
    

    def renderOpcoes(self):
        self.invocador = api_service.checarInvSalvo()

        self.status = api_service.statusServidor(self.key)
        self.labelStatus = Label(self.root, bg =bg , fg = fg, text = self.status[0]+"\n"+self.status[1])
        self.labelStatus["font"] = ("arial", 15,"italic","underline")
        self.labelStatus.grid(row = 2, column = 2)
        self.labelStatus.place(x = 400, y = 650)

        if(self.invocador):
            self.renderInvocador()
            self.renderSalvarInvocador()
            self.renderMenuLateral()
        else:
            self.renderSalvarInvocador()

    
            
    def renderInvocador(self):

        if hasattr(self, "frameInvSalvo"):
            self.frameInvSalvo.destroy()
        

        self.frameInvSalvo = Frame(self.root, width=100, height=100, bg = bg)
        self.frameInvSalvo.place(x = 20, y = 380)   

        icon = api_service.iconeInv(self.invocador)
        width, height = icon.size
        icon = icon.resize((75, 75), Image.ANTIALIAS)
        self.imgIcon  = ImageTk.PhotoImage(icon)

        self.labelImg = Label(self.frameInvSalvo, image = self.imgIcon)
        self.labelImg.grid(row = 0, column = 0, sticky = E)
        
        nomeInv = getattr(self.invocador, "name")
        self.labelInvocador = Label(self.frameInvSalvo)
        self.labelNome = Label(self.frameInvSalvo, text = nomeInv, font="termite 15 bold", bg = bg)
        self.labelNome.grid(column = 1, row = 0)


        




        

    def renderSalvarInvocador(self):
        
        self.frameInv = Frame(self.root, bg = bg)
        #self.frameInv.pack(side = BOTTOM, ensure = LEFT)
        self.frameInv.grid(row = 1, pady = 20) 
        self.frameInv.place(x = 10, y = 250)
        self.inputNome = Entry(self.frameInv, width=25, font="bold", fg=fg)
        self.inputNome.insert(0, "Digite seu nome invocador: ")
        self.inputNome.grid(row = 0, column = 0, pady = 15)

        self.botaoSalvar = Button(self.frameInv, text="Buscar", anchor = CENTER)
        self.botaoSalvar["command"] = self.actionSalvarInvoc
        self.botaoSalvar.grid(row = 1, column = 0)

    def actionSalvarInvoc(self):
        nome = self.inputNome.get()
        invoc = menu_service.summonerByName(nome, self.key) 
        if(invoc == "ERRO"):
            self.inputNome.delete(0,END)
            self.botaoSalvar["bg"] = "red"
            self.botaoSalvar["text"] = "Invocador nao encontrado"
        else:
            self.invocador = invoc
            self.botaoSalvar["text"] = "Salvo!"
            self.inputNome["background"] = "#4EC375"
            api_service.salvarInv(invoc)
            self.renderOpcoes()
    
    def renderMenuLateral(self):
        self.boxBotoes = Frame(self.root, bg = bg)        
        self.boxBotoes.grid(row = 1, column = 2)
        self.boxBotoes.place(y = 200, x = 630)

        self.botao1 = Button(self.boxBotoes, text = "Campeões mais jogados", bg = bg, fg = fg, height=1, width=20, font = "bold")
        self.botao1.grid(column = 0, row = 0, pady = 15)
        
        self.botao2 = Button(self.boxBotoes, text = "Estatisticas", bg = bg, fg = fg, height=1, width=20, font = "bold")
        self.botao2["command"] = self.renderEstatisticas
        self.botao2.grid(column = 0, row = 1, pady = 15)

        self.botao3 = Button(self.boxBotoes, text = "Última partida", bg = bg, fg = fg, height=1, width=20, font = "bold")
        self.botao3.grid(column = 0, row = 2, pady = 15)

        self.botao4 = Button(self.boxBotoes, text = "Ver rank", bg = bg, fg = fg, height=1, width=20, font = "bold")
        self.botao4["command"]=self.renderQueue
        self.botao4.grid(column = 0, row = 3, pady = 15)



    def renderQueue(self):
        self.root.destroy()
        viewInvocador.InfoInvocador(self.invocador, self.key)

    def renderEstatisticas(self):
        self.root.destroy()
        viewEstatistica.EstatisticasInvo(self.invocador, self.key)
        
        

menu = MenuAut()
getattr(menu, "root").mainloop()

