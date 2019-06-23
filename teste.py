from tkinter import *
from PIL import ImageTk

bg = "Grey6"  # "#182422"

fg = "#F3E171"
class Teste:
    def __init__(self):
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
        #teste


