from tkinter import *
from PIL import Image, ImageTk
from services import api_service
global bg
bg = "#182422"

global fg
fg = "#F3E171"

global fgElo
fgElo = "#FFF399"

class InfoInvocador:
    def __init__(self, invocador, key):
        #Renderizar imagem de titulo
        self.key = key
        self.invocador = invocador
        self.queueList = api_service.getQueue(self.invocador.id, self.key)
        self.root = Tk()
        self.root.title("League Viwer")
        self.root.resizable(False, False)
        self.root.geometry("900x700")
        self.root["background"] = bg
        self.root.update()

        print(self.invocador)
        print(self.queueList)



        #renderizar logo
        self.container = Frame(self.root, bg = bg)
        self.container.grid(row = 0, column = 2, columnspan = 2)
        self.container.place(x = 340, y = 0)
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)
        self.painel = Label(self.container, image=self.logoImg, bg = bg)
        self.painel.image = self.logoImg
        self.painel.grid_columnconfigure(0, weight = 1)
        self.painel.grid_rowconfigure(0, weight = 1)
        self.painel.pack(anchor=W, fill=Y, expand=False, side=LEFT)
        
        if(len(self.queueList) == 0):
            self.labelErro = Label(self.root, text ="Sem dados suficientes!\n Jogue partidas ranqueadas e volte mais tarde!", fg = fg, bg = bg, font = ("Verdana", 20, "bold"))

            self.labelErro.grid(column = 2, row = 1, columnspan = 2)
            self.labelErro.place(x = 82, y = 200)
        else:
            ex = 20
            ey = 130
            for queue in self.queueList:
                if ex < 600:
                    self.renderQueue(queue, ex, ey)
                    ex += 505
                else:
                    self.renderQueue(queue, ex, ey)
                    ey += 250
                    ex = 20







    def renderQueue(self, queue,ex,ey):
        #Renderizar as informações do elo Solo Duo 5x5 
        self.frameQueue = Frame(self.root, bg = bg, bd = 2, relief = SUNKEN, padx = 20)
        self.frameQueue.pack(anchor = E)
        self.frameQueue.place(x = ex, y = ey)
       
        leagueId = queue["leagueId"]
        league = api_service.getFullLeague(leagueId, self.key)

        leagueName = league["name"]
        elo = queue["tier"] + " "+ queue["rank"]
        pdl = str(queue["leaguePoints"])
        numVD = str(queue["wins"])+"/"+str(queue["losses"])


        Label(self.frameQueue, text = queue["queueType"], pady = 8, bg = bg, fg = fg,font = ("Verdana",20, "bold","italic","underline")).grid(column = 0, row = 0, columnspan = 2)


        Label(self.frameQueue, text = leagueName, bg = bg, fg = fg, font = ("Verdana",20,"bold")).grid(column = 0, row = 1, columnspan = 2)

        Label(self.frameQueue, text = "Divisão: ", bg = bg, fg = fg, font  = ("Verdana",15)).grid(column = 0, row = 2)

        self.labelElo = Label(self.frameQueue, text = elo, bg = bg, fg = fg,font = ("Verdana",15, "bold"), pady = 10)
        self.labelElo.grid(column = 1, row = 2)
        
        Label(self.frameQueue, text = "Pontos de Liga: ", bg = bg, fg = fg, font = ("Verdana",15)).grid(column = 0, row = 3)
        Label(self.frameQueue, text = pdl, bg = bg, fg = fg,font =("Verdana",15, "bold"), pady = 15).grid(column = 1, row = 3)

        Label(self.frameQueue, text = "Vitorias/Derrotas: ", bg = bg, fg = fg, font = ("Verdana", 15)).grid(column = 0, row = 4)
        Label(self.frameQueue, text = numVD, bg = bg, fg = fg, font = ("Verdana",15,"bold"), pady = 15).grid(column = 1, row = 4)


