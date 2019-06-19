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

        #renderizar logo
        self.container = Frame(self.root, bg = bg)
        self.container.pack(side = TOP)
        #self.container.place(x = 340, y = 0)
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)
        self.painel = Label(self.container, image=self.logoImg, bg = bg)
        self.painel.image = self.logoImg
        self.painel.pack(anchor=W, fill=Y, side=TOP)
        
        if(len(self.queueList) == 0):
            self.labelErro = Label(self.root, text ="Sem dados suficientes!\n Jogue partidas ranqueadas e volte mais tarde!", fg = fg, bg = bg, font = ("Verdana", 20, "bold"))

            self.labelErro.grid(column = 2, row = 1, columnspan = 2)
            self.labelElo.pack(self.root, side = TOP)
        else:
            self.renderQueue(self.queueList[0], LEFT)
            self.renderQueue(self.queueList[1], RIGHT)
        

        self.button = Frame(self.root)
        self.button.pack()
        self.button.place(x=30, y=20)
        self.back = Button(self.button, text="◄ VOLTAR", bg="Grey10", fg="Grey90", font=("Arial Black", "13", "bold",
                                                                                        "italic"),
                        bd=2, activebackground="Grey20", activeforeground="Grey90",
                        relief="solid", height=1, width=15, command=self.close)
        self.back.pack()



    def close(self):
        self.root.destroy()
        from components import menu
        self.menuG = menu.MenuAut()
        

    def renderQueue(self, queue,l):
        #Renderizar as informações das filas ranqueadas 
        self.frameQueue = Frame(self.root, bg = bg, bd = 2, relief = SUNKEN, padx = 20)
        self.frameQueue.pack(anchor = N, side = l, padx = 40, pady = 50)
        leagueId = queue["leagueId"]
        league = api_service.getFullLeague(leagueId, self.key)

        leagueName = league["name"]
        elo = queue["tier"] + " "+ queue["rank"]
        pdl = str(queue["leaguePoints"])
        numVD = str(queue["wins"])+"/"+str(queue["losses"])


        Label(self.frameQueue, text = queue["queueType"].replace("_", " "), pady = 8, bg = bg, fg = fg,font = ("Verdana",20, "bold","italic","underline")).grid(column = 0, row = 0, columnspan = 2)


        Label(self.frameQueue, text = leagueName, bg = bg, fg = fg, font = ("Verdana",20,"bold")).grid(column = 0, row = 1, columnspan = 2)
        

        self.divis = Frame(self.frameQueue, bg = bg)
        self.divis.grid(row = 2, columnspan = 2)
        #Label(self.frameQueue, text = "Divisão: ", bg = bg, fg = fg, font  = ("Verdana",15)).grid(column = 0, row = 2)
        Label(self.divis, text = "Divisão: ", bg = bg, fg = fg, font  = ("Verdana",15)).pack(anchor = CENTER, side = LEFT)

        #self.labelElo = Label(self.frameQueue, text = elo, bg = bg, fg = fg,font = ("Verdana",15, "bold"), pady = 10)
        #self.labelElo.grid(column = 1, row = 2)
        self.labelElo = Label(self.divis, text = elo, bg = bg, fg = fg,font = ("Verdana",15, "bold"), pady = 10)
        self.labelElo.pack(anchor = CENTER, side =LEFT)

        self.pdlFrame = Frame(self.frameQueue, bg = bg)
        self.pdlFrame.grid(row = 3, columnspan = 2)

        Label(self.pdlFrame, text = "Pontos de Liga: ", bg = bg, fg = fg, font = ("Verdana",15)).pack(anchor = CENTER, side = LEFT)
        Label(self.pdlFrame, text = pdl, bg = bg, fg = fg,font =("Verdana",15, "bold"), pady = 15).pack(anchor = CENTER, side = LEFT)

        self.winLoseFrame = Frame(self.frameQueue, bg = bg)
        self.winLoseFrame.grid(row = 4, columnspan = 2)
        Label(self.winLoseFrame, text = "Vitorias/Derrotas: ", bg = bg, fg = fg, font = ("Verdana", 15)).pack(anchor = CENTER, side = LEFT)
        Label(self.winLoseFrame, text = numVD, bg = bg, fg = fg, font = ("Verdana",15,"bold"), pady = 15).pack(anchor = CENTER, side = LEFT)
