from tkinter import *
from PIL import ImageTk, Image
import os
from services import info, api_service, menu_service

bg = "Grey6"  # "#182422"

fg = "#F3E171"


class Map:
    def __init__(self):
        self.root = Tk()
        self.root.title("League Viwer")
        self.root.resizable(False, False)
        self.root.geometry("900x650+220+20")
        self.root["background"] = bg
        self.container = Frame(self.root, bg=bg)
        self.container.grid(row=0, column=2, columnspan=2)
        self.container.place(x=330, y=0)

        # Logo
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)
        self.painel = Label(self.container, image=self.logoImg, bg=bg)
        self.painel.image = self.logoImg
        self.painel.grid_columnconfigure(0, weight=1)
        self.painel.grid_rowconfigure(0, weight=1)
        self.painel.pack(anchor=W, fill=Y, expand=False, side=LEFT)

        # Voltar
        self.button = Frame(self.root)
        self.button.pack()
        self.button.place(x=30, y=20)
        self.back = Button(self.button, text="◄ VOLTAR", bg="Grey10", fg="Grey90", font=("Arial Black", "13", "bold",
                                                                                         "italic"),
                           bd=2, activebackground="Grey20", activeforeground="Grey90", relief="solid", height=1,
                           width=15, command=self.close, cursor="X_Cursor")
        
        self.back.pack()
        self.root.update()

        # Info
        self.data = Frame(self.root, bg=bg)
        self.data.pack()
        self.data.place(x=540, y=130)

        self.canvas = Canvas(self.root, width=512, height=512)
        self.canvas.pack()
        self.canvas.place(x=10, y=125)
        map = ImageTk.PhotoImage(Image.open('../src/img/map.png'))
        
        self.canvas.create_image(2, 2, image=map, anchor=NW)
        
        key = info.get_key()
        inv = menu_service.summonerByName(info.get_name(), key)
        print(inv)
        
        matchD = api_service.getMatchStatus(key, inv)

        if not matchD:
            self.render_erro()
        else:
            self.render_all(matchD, inv)

        self.root.mainloop()

    def render_all(self, match, summoner):
        kills = match[0]
        
        maxx, maxy = 14870, 14980
      
        
        iconChamp = api_service.getIconByName(match[9])
        
        width, height = iconChamp.size
        iconChamp = ImageTk.PhotoImage(iconChamp.resize((width // 2, height // 2), Image.ANTIALIAS))
        
        colourplayer = {100: "Blue",
                        200: "Red"}
        
        result = {True: "Vitória!",
                  False: "Derrota!"}
        
        result_colour = {True: "RoyalBlue3",
                         False: "Firebrick2"}

        for i in range(len(kills)):
            x, y = kills[i]["x"], kills[i]["y"]
            killer = kills[i]["killerId"]
            colour = "OliveDrab2" if killer == match[2] else "Blue" if killer <= 5 else "Red"
            x = (512 * x) / maxx
            y = 512 - ((512 * y) / maxy)
        
            self.create_point(x, y, self.canvas, colour)
            
      
        # Icone do campeão
        labelIcon = Label(self.data, bg = bg, image = iconChamp)
        labelIcon.image = iconChamp
        labelIcon.grid(row = 0, column = 0, pady = 10)
      
        # Nome do champ
        Label(self.data, text=match[9], font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="OliveDrab2").grid(row=0, column=1, pady = 10)
        
        # Nome do invocador
        Label(self.data, text="Nome:", font=("Arial", "14", "bold", "italic"), bg=bg, fg="PaleGreen3").grid(sticky=W, row =1, column =0)
        Label(self.data, text=summoner.name, font=("Arial", "14", "bold", "italic"), bg=bg,
              fg=colourplayer[match[1]]).grid(row=1, column=1, pady=10)

        # Eliminações, mortes e assistências
        Label(self.data, text="AMA:", font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="PaleGreen3").grid(row=2, sticky=W, pady=10)
        Label(self.data, text=match[6], font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="MediumPurple1").grid(row=2, column=1)

        # Ouro gasto
        Label(self.data, text="Ouro gasto:", font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="PaleGreen3").grid(row=3, sticky=W, pady=10)
        Label(self.data, text=match[4], font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="DarkOrange3").grid(row=3, column=1)

        # Ouro recebido
        Label(self.data, text="Ouro recebido:", font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="PaleGreen3").grid(row=4, sticky=W, pady=10)
        Label(self.data, text=match[5], font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="DarkOrange3").grid(row=4, column=1)

        # Tropas abatidas
        Label(self.data, text="Tropas abatidas:", font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="PaleGreen3").grid(row=5, sticky=W, pady=10)
        Label(self.data, text=match[7], font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="DarkOrange3").grid(row=5, column=1)

        # Monstros neutros abatidos
        Label(self.data, text="Monstros abatidos:", font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="PaleGreen3").grid(row=6, sticky=W, pady=10)
        Label(self.data, text=match[8], font=("Arial", "14", "bold", "italic"), bg=bg,
              fg="DarkOrange3").grid(row=6, column=1)


        Label(text=result[match[3]], font=("Arial", "30", "bold", "italic"), bg=bg,
              fg=result_colour[match[3]]).place(x=625, y=530)

        # teste
        
    def create_point(self, x, y, canvas, colour):
        x1, y1 = (x - 5), (y - 5)
        x2, y2 = (x + 5), (y + 5)
        canvas.create_oval(x1, y1, x2, y2, fill=colour)

    def render_erro(self):
        Label(text="Você não jogou nenhuma partida em\nSummoner's Rift recentemente!",
              font=("Arial", "14", "bold", "italic"), bg=bg, fg="Firebrick2").pack(anchor=NE, padx=10, pady=140)

    def close(self):
        self.root.destroy()
        os.system("menu.py 1")


Map()
