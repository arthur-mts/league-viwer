import json
import os
from tkinter import *
# Não consigo abrir o arquivo da mesma pasta no linux. talvez tenha q tirar na versao final
from services import menu_service, api_service
from PIL import ImageTk, Image


bg = "Grey6"  # "#182422"

fg = "#F3E171"


class MenuAut:
    def __init__(self, loop=True):
        # Renderizar imagem de titulo
        self.root = Tk()
        self.root.title("League Viwer")
        self.root.resizable(False, False)
        self.root.geometry("900x650+220+20")
        self.root["background"] = bg
        self.container = Frame(self.root, bg=bg)
        self.container.grid(row=0, column=2, columnspan=2)
        self.container.place(x=330, y=0)
        # Redimensionando logo
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)

        self.painel = Label(self.container, image=self.logoImg, bg=bg)
        self.painel.image = self.logoImg
        self.painel.grid_columnconfigure(0, weight=1)
        self.painel.grid_rowconfigure(0, weight=1)
        self.painel.pack(anchor=W, fill=Y, expand=False, side=LEFT)
        self.root.update()

        try:
            with open("../src/dados/key.json") as r:
                self.arquivo = json.load(r)
                self.validado = menu_service.validarKey(self.arquivo["senha"])
        except:
            self.validado = False

        if self.validado:
            self.key = self.arquivo["senha"]
            self.renderOpcoes()
        else:
            self.renderAutenticar()

        if not loop:
            self.root.mainloop()

    def actionAutenticar(self):
        self.key = self.keyEnter.get()
        if menu_service.validarKey(self.key):
            self.botaoAut["text"] = "Chave validada!"
            self.botaoAut["fg"] = "OliveDrab2"
            validado = {'senha': self.key}
            with open("../src/dados/key.json", "w+", encoding='utf-8') as arquivo:
                json.dump(validado, arquivo)
                arquivo.close()
            self.container2.destroy()
            self.renderOpcoes()
        else:
            self.keyEnter.delete(0, END)
            self.botaoAut["text"] = "Erro de autenticação!"
            self.botaoAut["fg"] = "Goldenrod1"

    def renderAutenticar(self):
        self.container2 = Frame(self.root, bg=bg)
        self.container2["pady"] = 10
        self.container2.grid(column=2, row=0, columnspan=2)
        self.container2.place(x=250, y=200)
        self.textoAut = Label(self.container2, text="Digite sua chave de acesso:", bg=bg, fg="DarkOrange3",
                              font=("Verdana", "14", "bold", "italic"))
        self.textoAut.grid(column=0, row=0)
        self.keyEnter = Entry(self.container2, width=45, font=("Arial", "13", "bold"), fg="Grey60", bg="Grey10", bd=3,
                              relief="solid")
        self.keyEnter.grid(column=0, row=1, pady=20)
        self.botaoAut = Button(self.container2, text="Autenticar", fg="Grey90", bg="Grey10",
                               font=("Arial", "13", "bold"), bd=2, relief="solid", activebackground="Grey20",
                               activeforeground="Grey90", width=20, cursor="X_Cursor")
        self.botaoAut["command"] = self.actionAutenticar
        self.botaoAut.grid(row=2)

    def renderOpcoes(self):
        self.invocador = api_service.checarInvSalvo()

        self.status = api_service.statusServidor(self.key)
        self.labelStatus = Label(self.root, bg=bg, fg="MediumPurple1", text=self.status[0] + "\n" + self.status[1])
        self.labelStatus["font"] = ("Arial", 15, "italic")
        self.labelStatus.grid(row=2, column=2)
        self.labelStatus.place(x=400, y=570)

        if self.invocador:
            self.renderInvocador()
            self.renderSalvarInvocador()
            self.renderMenuLateral()
        else:
            self.renderSalvarInvocador()

    def renderInvocador(self):

        if hasattr(self, "frameInvSalvo"):
            self.frameInvSalvo.destroy()

        self.frameInvSalvo = Frame(self.root, width=100, height=100, bg=bg)
        self.frameInvSalvo.place(x=20, y=370)

        icon = api_service.iconeInv(self.invocador)
        icon = icon.resize((75, 75), Image.ANTIALIAS)
        self.imgIcon = ImageTk.PhotoImage(icon)

        self.labelImg = Label(self.frameInvSalvo, image=self.imgIcon)
        self.labelImg.grid(row=0, column=0, sticky=E)
        
        nomeInv = getattr(self.invocador, "name")
        self.labelInvocador = Label(self.frameInvSalvo)
        self.labelNome = Label(self.frameInvSalvo, text=nomeInv, font="termite 15 bold italic", bg=bg, fg="Snow")
        self.labelNome.grid(column=1, row=0, padx=20)

    def renderSalvarInvocador(self):
        
        self.frameInv = Frame(self.root, bg=bg)
        #self.frameInv.pack(side = BOTTOM, ensure = LEFT)
        self.frameInv.grid(row=1, pady=20)
        self.frameInv.place(x=20, y=200)

        self.instruction = Label(self.frameInv, text="Digite seu nome de invocador:", bg=bg, fg="DarkOrange3",
                                 font=("Verdana", "14", "bold", "italic"))
        self.instruction.grid(row=0, column=0)

        self.inputNome = Entry(self.frameInv, width=30, font=("Arial", "13", "bold"), fg="Grey60",
                               bg="Grey10", bd=3, relief="solid")
        self.inputNome.grid(row=1, column=0, pady=15)

        self.botaoSalvar = Button(self.frameInv, text="Buscar", anchor=CENTER, fg="DarkOrange3", bg="Grey10",
                                  font=("Arial", "13", "bold"), bd=2, relief="solid", activebackground="Grey20",
                                  activeforeground="Grey90", width=15, cursor="X_Cursor")
        self.botaoSalvar["command"] = self.actionSalvarInvoc
        self.botaoSalvar.grid(row=2, column=0)

    def actionSalvarInvoc(self):
        nome = self.inputNome.get()
        invoc = menu_service.summonerByName(nome, self.key) 
        if invoc == "ERRO":
            self.inputNome.delete(0, END)
            self.botaoSalvar["fg"] = "Red3"
            self.botaoSalvar["text"] = "Invocador não encontrado!"
            self.botaoSalvar["width"] = 25
        else:
            self.invocador = invoc
            self.botaoSalvar["text"] = "Salvo!"
            self.inputNome["background"] = "#4EC375"
            api_service.salvarInv(invoc)
            self.renderOpcoes()
    
    def renderMenuLateral(self):
        self.boxBotoes = Frame(self.root, bg=bg)
        self.boxBotoes.grid(row=1, column=2)
        self.boxBotoes.place(y=170, x=600)

        self.botao1 = Button(self.boxBotoes, text="Campeões mais jogados", bg="Grey10", fg="OliveDrab1", height=2,
                             width=25, font=("Arial", "13", "bold"), activebackground="Grey20",
                             activeforeground="Grey90", bd=3, relief="solid", cursor="X_Cursor")
        self.botao1["command"] = self.render_champions
        self.botao1.grid(column=0, row=0, pady=15)
        
        self.botao2 = Button(self.boxBotoes, text="Estatísticas", bg="Grey10", fg="OliveDrab1", height=2, width=25,
                             font=("Arial", "13", "bold"), activebackground="Grey20", activeforeground="Grey90", bd=3,
                             relief="solid", cursor="X_Cursor")
        self.botao2["command"] = self.renderEstatisticas
        self.botao2.grid(column=0, row=1, pady=15)

        self.botao3 = Button(self.boxBotoes, text="Última partida", bg="Grey10", fg="OliveDrab1", height=2, width=25,
                             font=("Arial", "13", "bold"), activebackground="Grey20", activeforeground="Grey90", bd=3,
                             relief="solid", cursor="X_Cursor")
        self.botao3.grid(column=0, row=2, pady=15)
        self.botao3["command"] = self.render_map

        self.botao4 = Button(self.boxBotoes, text="Ranking", bg="Grey10", fg="OliveDrab1", height=2, width=25,
                             font=("Arial", "13", "bold"), activebackground="Grey20", activeforeground="Grey90", bd=3,
                             relief="solid", cursor="X_Cursor")
        self.botao4["command"] = self.renderQueue
        self.botao4.grid(column=0, row=3, pady=15)

    def renderQueue(self):
        self.root.destroy()
        from components import viewInvocador
        viewInvocador.InfoInvocador(self.invocador, self.key)

    def renderEstatisticas(self):
        self.root.destroy()
        from components import viewEstatistica
        viewEstatistica.EstatisticasInvo(self.invocador, self.key)

    def render_champions(self):
        self.root.destroy()
        os.system("champions.py 1")

    def render_map(self):
        self.root.destroy()
        os.system("map.py 1")
        
        
MenuAut(loop=False)
