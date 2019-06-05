from tkinter import *
from PIL import Image, ImageTk

global bg
bg = "#182422"

global fg
fg = "#F3E171"

global fgElo
fgElo = "#FFF399"

class InfoInvocador:
    def __init__(self, queue):
        #Renderizar imagem de titulo
        self.root = Tk()
        self.root.title("League Viwer")
        self.root.resizable(False, False)
        self.root.geometry("900x700")
        self.root["background"] = bg
        self.root.update()


        self.container = Frame(self.root, bg = bg)
                #self.container.pack()
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


        #Renderizar as informações do elo Solo Duo 5x5 
        self.frameSoloDuo = Frame(self.root, bg = bg, bd = 2, relief = SUNKEN, padx = 20)
        self.frameSoloDuo.pack(anchor = E)
        self.frameSoloDuo.place(x = 20, y = 100)
        
        elo = queue[0]["tier"] + " "+ queue[0]["rank"]

        self.labelQueue = Label(self.frameSoloDuo, text = "Ranqueada Solo/Duo", pady = 20, bg = bg, fg = fg) 
        self.labelQueue["font"] = ("Verdana",20, "bold","italic","underline")
        self.labelQueue.grid(column = 0, row = 0, columnspan = 2)

        self.labelDElo = Label(self.frameSoloDuo, text = "Divisão: ", bg = bg, fg = fg)
        self.labelDElo["font"] = ("Verdana",15)
        self.labelDElo.grid(column = 0, row = 1)

        self.labelElo = Label(self.frameSoloDuo, text = elo, bg = bg, fg = fg)
        self.labelElo["font"] = ("Verdana",15, "bold")

        self.labelDPdl = Label(self.frameSoloDuo, text = "PDL")
        self.labelElo.grid(column = 1, row = 1)








