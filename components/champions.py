from tkinter import *
from urllib.request import urlopen
import io
import json
from PIL import ImageTk, Image
from services import most_played_champions
from services import menu_service

# Configurações da fonte
font = ("Verdana", "14", "italic", "bold")

# Cores para tipos de campeão
colours = {"Fighter": "#933A16",
           "Assassin": "#D64142",
           "Tank": "#A4DD86",
           "Marksman": "#D6BA7B",
           "Mage": "#9CA6F7",
           "Support": "#44ACB5"}

# Respostas e cores para se ganhou baú com campeão
answer = {True: "Sim", False: "Não"}
colour = {True: "#50C878", False: "#CA3433"}

# Dados do invocador a partir do nome
player = menu_service.summonerByName("0 Fígurante", "RGAPI-0cb00a9f-31cb-4617-8b58-93e155c2f6b0")

# Arquivo dos dados dos campeões mais jogados de invocadores
with open("../src/champions_data.json", "r") as file:
    data = json.load(file)
    file.close()

# Arquivo das IDs dos campeões mais jogados de invocadores
with open("../src/champions.json", "r") as file:
    array = json.load(file)
    file.close()

# Verificar se dados do invocador estão no dicionário
if player.name not in data:
    most_played_champions.update_info(player, data, array, "RGAPI-0cb00a9f-31cb-4617-8b58-93e155c2f6b0")


class Screen:

    def __init__(self, master=None):

        # Título
        self.first = Frame(master)
        self.first.pack()
        self.title = Label(self.first, text="Campeões", fg="Seashell2", bg="Grey6", font=("Verdana", "30", "italic",
                                                                                          "bold"))
        self.title.pack()

        # Primeiro campeão
        self.second = Frame(master, bg="Grey6")
        self.second.pack()
        self.second.place(x=410, y=110)

        # Segundo campeão
        self.third = Frame(master, bg="Grey6")
        self.third.pack()
        self.third.place(x=410, y=310)

        # Terceiro campeão
        self.fourth = Frame(master, bg="Grey6")
        self.fourth.pack()
        self.fourth.place(x=410, y=510)

        # Imagens, ícones e informações
        for i in range(3):
            # Imagens e ícones
            self.render(i, 30, 80 if i == 0 else 280 if i == 1 else 480)

            # Informações
            frame = self.second if i == 0 else self.third if i == 1 else self.fourth
            self.info(frame, i)

    # Imagens e ícones
    def render(self, number, x, y):
        # Imagens
        link = urlopen(data[player.name][number]["Image"]).read()
        archive = Image.open(io.BytesIO(link))
        width, height = archive.size
        archive = archive.resize((width // 4, height // 4), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(archive)
        show = Label(image=image)
        show.image = image
        show.place(x=x, y=y)

        # Ícones
        archive = Image.open("../src/img/mastery_level_" + str(data[player.name][number]["Mastery"]) + ".png")
        width, height = archive.size
        archive = archive.resize((width // 2, height // 2), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(archive)
        show = Label(image=image, bg="Grey6")
        show.image = image
        show.place(x=x + 310, y=y + 60)

    # Informações
    def info(self, frame, i):
        Label(frame, text="Nome:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=0)
        Label(frame, text=data[player.name][i]["Name"] + ", " + data[player.name][i]["Title"],
              fg=colours[data[player.name][i]["Tags"][0]], bg="Grey6", font=font).grid(row=0, column=1)
        Label(frame, text="Maestria:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=1)
        Label(frame, text=data[player.name][i]["Mastery"], fg="DarkOrange3", bg="Grey6", font=font).grid(row=1,
                                                                                                         column=1)
        Label(frame, text="Pontos de Maestria:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=2)
        Label(frame, text=data[player.name][i]["Score"], fg="DarkOrange3", bg="Grey6", font=font).grid(row=2, column=1)
        Label(frame, text="Baú ganho:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=3)
        Label(frame, text=answer[data[player.name][i]["Chest"]], fg=colour[data[player.name][i]["Chest"]], bg="Grey6",
              font=font).grid(row=3, column=1)


# Janela
root = Tk()
root.title("League Viwer")
root.resizable(False, False)
root["background"] = "Grey6"
root.geometry("1060x690+145+0")
root.update()
Screen(root)
root.mainloop()
