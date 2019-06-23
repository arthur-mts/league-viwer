from tkinter import *
from PIL import ImageTk, Image
from services import api_service, menu_service

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
        img = Image.open('src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)
        self.painel = Label(self.container, image=self.logoImg, bg=bg)
        self.painel.image = self.logoImg
        self.painel.grid_columnconfigure(0, weight=1)
        self.painel.grid_rowconfigure(0, weight=1)
        self.painel.pack(anchor=W, fill=Y, expand=False, side=LEFT)
        self.root.update()

        # Info
        self.data = Frame(self.root, bg=bg)
        self.data.pack()
        self.data.place(x=550, y=130)

        self.canvas = Canvas(self.root, width = 512, height = 512)
        self.canvas.pack()
        self.canvas.place(x = 10, y = 125)
        map = ImageTk.PhotoImage(Image.open('src/img/map.png'))
        
        self.canvas.create_image(2,2, image = map, anchor = NW)
        
        key = "RGAPI-b6ef6146-0abb-4c08-918f-e801928516fa"
        inv = menu_service.summonerByName("Dark", key)
        print(inv)
        
        matchD = api_service.getMatchStatus(key, inv)
        kills=matchD[0]
        
        maxx, maxy = 14870,14980

        colourplayer = {100: "Turquoise",
                        200: "Dark Orange"}

        for i in range(len(kills)):
            x, y = kills[i]["x"], kills[i]["y"]
            killer = kills[i]["killerId"]
            colour = colourplayer[matchD[1]] if killer == matchD[2] else "Blue" if killer <= 5 else "Red"
            x = (512 * x) / maxx
            y = 512 - ((512 * y) / maxy)
        
            self.create_point(x, y, self.canvas, colour)

        print(kills)

        Label(self.data, text=inv.name, font=("Verdana", "15", "bold", "italic"), bg=bg,
              fg=colourplayer[matchD[1]]).grid()
        
        self.root.mainloop()
        #teste
        
    def create_point(self, x,y, canvas, colour):
        x1, y1 = (x - 5), (y - 5)
        x2, y2 = (x + 5), (y + 5)
        canvas.create_oval(x1, y1, x2, y2, fill=colour)
        
Teste()

