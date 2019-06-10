from tkinter import *
from PIL import Image, ImageTk
from services import *

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
        self.root.update()

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
