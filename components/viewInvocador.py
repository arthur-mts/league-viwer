from tkinter import *
from PIL import Image, ImageTk
import os
from services import api_service

bg = "Grey6"

fg = "Chocolate3"

fgElo = "#FFF399"

Translate = {"Iron": "Ferro",
             "Bronze": "Bronze",
             "Silver": "Prata",
             "Gold": "Ouro",
             "Platinum": "Platina",
             "Diamond": "Diamante",
             "Master": "Mestre",
             "Grandmaster": "Grão-Mestre",
             "Challenger": "Desafiante"}


class InfoInvocador:
    def __init__(self, invocador, key):
        # Renderizar imagem de título
        self.key = key
        self.invocador = invocador
        self.queueList = api_service.getQueue(self.invocador.id, self.key)
        self.root = Tk()
        self.root.title("League Viwer")
        self.root.resizable(False, False)
        self.root.geometry("900x650+220+20")
        self.root["background"] = bg

        # Logo
        self.container = Frame(self.root, bg=bg)
        self.container.pack(side=TOP)
        # self.container.place(x = 340, y = 0)
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)
        self.painel = Label(self.container, image=self.logoImg, bg=bg)
        self.painel.image = self.logoImg
        self.painel.pack(anchor=W, fill=Y, side=TOP)

        # Loading
        icon = Image.open("../src/img/loading.png")
        width, height = icon.size
        icon = icon.resize((width // 6, height // 6), Image.ANTIALIAS)
        self.loading = ImageTk.PhotoImage(icon)
        self.photo = Label(image=self.loading, bg="Grey6")
        self.photo.image = self.loading
        self.photo.pack(pady=150)

        # Voltar
        self.button = Frame(self.root)
        self.button.pack()
        self.button.place(x=30, y=20)
        self.back = Button(self.button, text="◄ VOLTAR", bg="Grey10", fg="Grey90", font=("Arial Black", "13", "bold",
                                                                                         "italic"), bd=2,
                           activebackground="Grey20", activeforeground="Grey90", relief="solid", height=1, width=15,
                           command=self.close, cursor="X_Cursor")
        self.back.pack()

        self.root.update()
        
        if len(self.queueList) == 0:
            self.photo.destroy()
            self.labelErro = Label(self.root,
                                   text="Sem dados suficientes!\nJogue partidas ranqueadas e volte mais tarde!",
                                   fg="Goldenrod2", bg=bg, font=("Verdana", 20, "bold"))

            # self.labelErro.grid(column = 2, row = 1, columnspan = 2)
            self.labelErro.pack(pady=50)
        elif len(self.queueList) == 1:
            self.photo.destroy()
            self.renderQueue(self.queueList[0], TOP)
            self.x = 345
            self.y = 500
            self.render_icons(self.queueList[0])
        else:
            self.photo.destroy()
            self.renderQueue(self.queueList[0], LEFT)
            self.renderQueue(self.queueList[1], RIGHT)
            self.x = 100
            self.y = 460
            self.render_icons(self.queueList[0])
            self.x = 595
            self.y = 460
            self.render_icons(self.queueList[1])

    def close(self):
        self.root.destroy()
        os.system("menu.py 1")

    def renderQueue(self, queue, l):
        # Renderizar as informações das filas ranqueadas
        self.frameQueue = Frame(self.root, bg=bg, bd=3, relief="groove", padx=20)
        self.frameQueue.pack(anchor=N, side=l, padx=40, pady=50)
        leagueId = queue["leagueId"]
        league = api_service.getFullLeague(leagueId, self.key)

        leagueName = league["name"]
        elo = Translate[queue["tier"].capitalize()] + " " + queue["rank"]
        pdl = str(queue["leaguePoints"])
        numVD = str(queue["wins"])+"/"+str(queue["losses"])

        Label(self.frameQueue, text=queue["queueType"].replace("_", " ").title().replace("X", "x"), pady=8, bg=bg,
              fg="Gainsboro", font=("Verdana", 20, "bold", "italic")).grid(column=0, row=0, columnspan=2)

        Label(self.frameQueue, text=leagueName, bg=bg, fg="DarkOliveGreen2",
              font=("Verdana", 20, "bold")).grid(column=0, row=1, columnspan=2)

        self.divis = Frame(self.frameQueue, bg=bg)
        self.divis.grid(row=2, columnspan=2)
        # Label(self.frameQueue, text = "Divisão: ", bg = bg, fg = fg, font  = ("Verdana",15)).grid(column = 0, row = 2)
        Label(self.divis, text="Divisão: ", bg=bg, fg="Light Blue", font=("Verdana", 15)).pack(anchor=CENTER, side=LEFT)

        # self.labelElo = Label(self.frameQueue, text = elo, bg = bg, fg = fg,font = ("Verdana",15, "bold"), pady = 10)
        # self.labelElo.grid(column = 1, row = 2)
        self.labelElo = Label(self.divis, text=elo, bg=bg, fg="Medium Aquamarine", font=("Verdana", 15, "bold"),
                              pady=20)
        self.labelElo.pack(anchor=CENTER, side=LEFT)

        self.pdlFrame = Frame(self.frameQueue, bg=bg)
        self.pdlFrame.grid(row=3, columnspan=2)

        Label(self.pdlFrame, text="Pontos de Liga: ", bg=bg, fg="Light Blue", font=("Verdana", 15)).pack(anchor=CENTER,
                                                                                                   side=LEFT)
        Label(self.pdlFrame, text=pdl, bg=bg, fg="Medium Aquamarine", font=("Verdana", 15, "bold"),
              pady=15).pack(anchor=CENTER, side=LEFT)

        self.winLoseFrame = Frame(self.frameQueue, bg=bg)
        self.winLoseFrame.grid(row=4, columnspan=2)
        Label(self.winLoseFrame, text="Vitórias / Derrotas: ", bg=bg, fg="Light Blue",
              font=("Verdana", 15)).pack(anchor=CENTER, side=LEFT)
        Label(self.winLoseFrame, text=numVD, bg=bg, fg="Medium Aquamarine", font=("Verdana", 15, "bold"),
              pady=15).pack(anchor=CENTER, side=LEFT)

    def render_icons(self, queue):
        # Ícones
        archive = Image.open("../src/img/tier/" + queue["tier"].capitalize() + ".png")
        width, height = archive.size
        archive = archive.resize((width // 5, height // 5), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(archive)
        show = Label(image=photo, bg="Grey6")
        show.image = photo
        show.place(x=self.x, y=self.y)
