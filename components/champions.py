from tkinter import *
from urllib.request import urlopen
import io
from PIL import ImageTk, Image
from services.info import *
from services.menu_service import *

# Fonte
font = ("Verdana", "14", "italic", "bold")

# Cores dos tipos de campeão
colours = {"Fighter": "#933A16",
           "Assassin": "#D64142",
           "Tank": "#A4DD86",
           "Marksman": "#D6BA7B",
           "Mage": "#9CA6F7",
           "Support": "#44ACB5"}

# Respostas e cores para se ganhou baú
answer = {True: "Sim", False: "Não"}
colour = {True: "#50C878", False: "#CA3433"}

# Chave
key = get_key()

# Nome
name = get_name()


class Screen:

    def __init__(self, master=None):

        # Info
        self.data = get_data()
        self.array = get_array()
        self.player = summonerByName(name, key)
        self.update = update_info(self.player, self.data, self.array, key)

        # Janela
        self.window = Tk()
        self.window.title("League Viwer")
        self.window.resizable(False, False)
        self.window["background"] = "Grey6"
        self.window.geometry("1060x690+145+0")

        # Título
        self.first = Frame(master)
        self.first.pack()
        self.title = Label(self.first, text="Campeões", fg="Grey90", bg="Grey6", font=("Arial Black", "30", "italic",
                                                                                       "bold"))
        self.title.pack()

        # Voltar
        self.button = Frame(master)
        self.button.pack()
        self.button.place(x=30, y=20)
        self.back = Button(self.button, text="◄ VOLTAR", bg="Grey10", fg="Grey90", font=("Arial Black", "13", "bold",
                                                                                         "italic"),
                           bd=2, activebackground="Grey20", activeforeground="Grey90", cursor="X_Cursor",
                           relief="solid", height=1, width=15, command=self.close)
        self.back.pack()

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

        # Imagens, ícones e info
        for i in range(3):
            # Imagens e ícones
            self.x = 30
            self.y = 80 if i == 0 else 280 if i == 1 else 480
            self.render(i)

            # Info
            self.frame = self.second if i == 0 else self.third if i == 1 else self.fourth
            self.info(i)
        self.window.mainloop()

    # Imagens e ícones
    def render(self, i):
        # Imagens
        link = urlopen(self.data[self.player.name][i]["Image"]).read()
        archive = Image.open(io.BytesIO(link))
        width, height = archive.size
        archive = archive.resize((width // 4, height // 4), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(archive)
        show = Label(image=photo, bg="Grey26")
        show.image = photo
        show.place(x=self.x, y=self.y)

        # Ícones
        archive = Image.open("../src/img/mastery_level_" + str(self.data[self.player.name][i]["Mastery"]) + ".png")
        width, height = archive.size
        archive = archive.resize((width // 2, height // 2), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(archive)
        show = Label(image=photo, bg="Grey6")
        show.image = photo
        show.place(x=self.x + 310, y=self.y + 60)

    # Info
    def info(self, i):
        Label(self.frame, text="Nome:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=0)
        Label(self.frame, text=self.data[self.player.name][i]["Name"] + ", " + self.data[self.player.name][i]["Title"],
              fg=colours[self.data[self.player.name][i]["Tags"][0]], bg="Grey6", font=font).grid(row=0, column=1)
        Label(self.frame, text="Maestria:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=1)
        Label(self.frame, text=self.data[self.player.name][i]["Mastery"], fg="DarkOrange3", bg="Grey6",
              font=font).grid(row=1, column=1)
        Label(self.frame, text="Pontos de Maestria:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=2)
        Label(self.frame, text=self.data[self.player.name][i]["Score"], fg="DarkOrange3", bg="Grey6",
              font=font).grid(row=2, column=1)
        Label(self.frame, text="Baú ganho:", fg="DarkOrange3", bg="Grey6", font=font).grid(row=3)
        Label(self.frame, text=answer[self.data[self.player.name][i]["Chest"]],
              fg=colour[self.data[self.player.name][i]["Chest"]], bg="Grey6", font=font).grid(row=3, column=1)

    # Voltar
    def close(self):
        self.window.destroy()
        from components.menu import MenuAut
        MenuAut()


Screen()
