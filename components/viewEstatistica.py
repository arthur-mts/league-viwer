from tkinter import *
from PIL import Image, ImageTk
from services import api_service, menu_service

global bg
bg = "#182422"

global fg
fg = "#F3E171"

class EstatisticasInvo:
    def __init__(self, invocador, key):
        self.invocador = invocador
        self.key = key
        self.root = Tk()
        self.root.title("League Viwer")
        self.root.resizable(False, False)
        self.root.geometry("900x700")
        self.root["background"] = bg

        #renderizar logo
        self.container = Frame(self.root, bg = bg)
        #self.container.pack(side = TOP)
        self.container.grid(row = 0, column = 0, columnspan = 5)
        self.container.place(y = 0, x = 330)
        #self.container.place(x = 340, y = 0)
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)
        self.painel = Label(self.container, image=self.logoImg, bg = bg)
        self.painel.image = self.logoImg
        self.painel.pack(anchor=W, fill=Y, side=TOP)
        
        self.root.update()
        
        #Botão para voltar
        self.button = Frame(self.root)
        self.button.pack()
        self.button.place(x=30, y=20)
        self.back = Button(self.button, text="◄ VOLTAR", bg="Grey10", fg="Grey90", font=("Arial Black", "13", "bold",
                                                                                        "italic"),
                        bd=2, activebackground="Grey20", activeforeground="Grey90",
                        relief="solid", height=1, width=15, command=self.close)
        self.back.pack()
        
        

        #Lista de ultimas partidas jogadas pelo invocador
        self.matches = api_service.getLastMatches(self.invocador.accountId, key)
        #Id dos campeões mais jogados
        self.idsMains = menu_service.mostPlayedChampions(self.invocador.id, self.key, idC=True)
        #Ids dos campeões mais jogados ultimamente
        self.idsLast = api_service.filterMostPlayedChampions(self.key, self.matches, self.invocador)
        
        #Ultimas partidas dos campeões mais jogados pelo invocador.
        self.lastMainMatches = api_service.filterMatchesByChampions(self.key, self.matches, self.idsMains, self.invocador)
        print(self.lastMainMatches)
        #Partidas dos campeões mais jogados ultimamente pelo invocador.
        self.lastMostMatches = api_service.filterMatchesByChampions(self.key, self.matches,self.idsLast, self.invocador)
        print(self.lastMostMatches)
        #Convertendo os ids para objetos do tipo campeão
        self.champsMain  = [menu_service.champById(c) for c in self.lastMainMatches.keys()]
        self.champsMost = [menu_service.champById(c) for c in self.lastMostMatches.keys()]
        self.renderMains()
        self.renderMost()

        
        
    def renderMains(self):
        self.mainsFrame = Frame(self.root,bg = bg, bd = 2, relief = SUNKEN)
        self.mainsFrame.pack(side = LEFT,anchor = N)
        self.mainsFrame.place(x = 20, y = 150)
        
        #Titulo da janela
        self.labelMains = Label(self.mainsFrame, text = "Estatisticas com os principais",fg =fg, bg = bg,
                                    font = ("Verdana",15, "bold","italic","underline"))
        self.labelMains.grid(row = 0,column = 0, columnspan = 3, padx = 20)
        
        for i in range(len(self.champsMain)):
            row = 1 + i*3
            champ = self.champsMain[i]
            self.champFrame = Frame(self.mainsFrame,  width = 100, height = 100, bg = bg)
            self.champFrame.grid(row = row, rowspan = 3, padx = 20, pady = 20)
            #elf.champFrame.pack(side = LEFT,anchor = N)
            #self.champFrame.place(x = 20, y = y)
            
            
            
            
            #Imagem do campeão
            #champ = self.champsMain[0]
            icon= api_service.getIconByName(champ.name)
            width, height = icon.size
            icon = icon.resize((width // 2, height // 2), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(icon)
            self.licon = Label(self.champFrame, image = img)
            self.licon.image = img
            self.licon.grid(row = 1, rowspan =2, sticky = W)
            
            self.labelName = Label(self.champFrame, text = champ.name, font = ("Verdana", 15, "bold")
                                    , fg = "white", bg =bg).grid(row = 1, column = 1, rowspan = 2, sticky = N)
            
            wl = self.lastMainMatches[champ.key]
            txt = "Vitorias: "+str(wl[0])+"/Derrotas: "+str(wl[1])
            self.winsLose = Label(self.champFrame, text = txt,font = ("Verdana", 15, "bold"),
                                fg ="red", bg = bg).grid(row = 3, column = 0, columnspan = 3)
            
        
        #ssself.splashC = api_service.getSplashByName(list(self.champsMost[self.champsMost.keys()[0]].name))
        
        
        

    def renderMost(self):
        self.mostFrame = Frame(self.root,bg = bg, bd = 2, relief = SUNKEN)
        self.mostFrame.pack(side = LEFT,anchor = N)
        self.mostFrame.place(x = 450, y = 150)
        
        #Titulo da janela
        self.labelMost = Label(self.mostFrame, text = "Estatisticas com os mais jogados",fg =fg, bg = bg,
                                    font = ("Verdana",15, "bold","italic","underline"))
        self.labelMost.grid(row = 0,column = 0, columnspan = 3, padx = 20)
        
        for i in range(len(self.champsMost)):
            row = 1 + i*3
            champ = self.champsMost[i]
            self.champFrame = Frame(self.mostFrame,  width = 100, height = 100, bg = bg)
            self.champFrame.grid(row = row, rowspan = 3, padx = 20, pady = 20)
            #elf.champFrame.pack(side = LEFT,anchor = N)
            #self.champFrame.place(x = 20, y = y)
            
            
            
            
            #Imagem do campeão
            #champ = self.champsMain[0]
            icon= api_service.getIconByName(champ.name)
            width, height = icon.size
            icon = icon.resize((width // 2, height // 2), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(icon)
            self.licon = Label(self.champFrame, image = img)
            self.licon.image = img
            self.licon.grid(row = 1, rowspan =2, sticky =W)
            
            self.labelName = Label(self.champFrame, text = champ.name, font = ("Verdana", 15, "bold")
                                    , fg = "white", bg =bg).grid(row = 1, column = 1, rowspan = 2, sticky = N)
            
            wl = self.lastMostMatches[champ.key]
            txt = "Vitorias: "+str(wl[0])+"/Derrotas: "+str(wl[1])
            self.winsLose = Label(self.champFrame, text = txt,font = ("Verdana", 15, "bold"),
                                fg ="red", bg = bg).grid(row = 3, column = 0, columnspan = 3)
        
    def close(self):
        self.root.destroy()
        from components import menu
        self.menuG = menu.MenuAut()
        
        