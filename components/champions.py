from tkinter import *
from urllib.request import urlopen
import io
from PIL import ImageTk, Image
from services import most_played_champions
from services import menu_service

background = "#182422"
foreground = "#F3E171"
default = ("Verdana", "15", "italic", "bold")

colours = {"Fighter": "#933A16",
           "Assassin": "#D64142",
           "Tank": "#A4DD86",
           "Marksman": "#D6BA7B",
           "Mage": "#9CA6F7",
           "Support": "#44ACB5"}


class Screen:
    def __init__(self, name, key, master=None):

        search = menu_service.summonerByName(name, key)
        dictionary = most_played_champions.most_played_champions(search.id, key)

        # Title
        self.first = Frame(master)
        self.first.pack()
        self.title = Label(self.first)
        self.title["text"] = "Campeões Mais Jogados"
        self.title["fg"] = "Snow"
        self.title["bg"] = "#182422"
        self.title["font"] = ("Verdana", "30", "italic", "bold")
        self.title.pack()

        answer = {True: "Sim",
                  False: "Não"}
        colour = {True: "#50C878",
                  False: "#CA3433"}

        # First champion
        self.second = Frame(master, bg=background)
        self.second.pack()
        self.second.place(x=400, y=120)

        # First champion image
        link = urlopen(dictionary[0]["Image"]).read()
        data = Image.open(io.BytesIO(link))
        width, height = data.size
        data = data.resize((width // 4, height // 4), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(data)
        image = image
        show = Label(master, image=image, bg=background)
        show.image = image
        show.place(x=50, y=100)

        # First champion info
        Label(self.second, text="Nome:", fg=foreground, bg=background, font=default).grid(row=1)
        Label(self.second, text=dictionary[0]["Name"] + ", " + dictionary[0]["Title"],
              fg=colours[dictionary[0]["Tags"][0]], bg=background, font=default).grid(row=1, column=1)
        Label(self.second, text="Masteria:", fg=foreground, bg=background, font=default).grid(row=2)
        Label(self.second, text=dictionary[0]["Mastery"], fg=foreground, bg=background, font=default).grid(row=2,
                                                                                                           column=1)
        Label(self.second, text="Pontos de Masteria:", fg=foreground, bg=background, font=default).grid(row=3)
        Label(self.second, text=dictionary[0]["Score"], fg=foreground, bg=background, font=default).grid(row=3,
                                                                                                         column=1)
        Label(self.second, text="Baú ganho:", fg=foreground, bg=background, font=default).grid(row=4)
        Label(self.second, text=answer[dictionary[0]["Chest"]], fg=colour[dictionary[0]["Chest"]], bg=background,
              font=default).grid(row=4, column=1)

        # Second champion
        self.third = Frame(master, bg=background)
        self.third.pack()
        self.third.place(x=400, y=320)

        # Second champion image
        link = urlopen(dictionary[1]["Image"]).read()
        data = Image.open(io.BytesIO(link))
        width, height = data.size
        data = data.resize((width // 4, height // 4), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(data)
        image = image
        show = Label(master, image=image, bg=background)
        show.image = image
        show.place(x=50, y=300)

        # Second champion info
        Label(self.third, text="Nome:", fg=foreground, bg=background, font=default).grid(row=0)
        Label(self.third, text=dictionary[1]["Name"] + ", " + dictionary[1]["Title"],
              fg=colours[dictionary[1]["Tags"][0]], bg=background, font=default).grid(row=0, column=1)
        Label(self.third, text="Masteria:", fg=foreground, bg=background, font=default).grid(row=1)
        Label(self.third, text=dictionary[1]["Mastery"], fg=foreground, bg=background, font=default).grid(row=1,
                                                                                                          column=1)
        Label(self.third, text="Pontos de Masteria:", fg=foreground, bg=background, font=default).grid(row=2)
        Label(self.third, text=dictionary[1]["Score"], fg=foreground, bg=background, font=default).grid(row=2, column=1)
        Label(self.third, text="Baú ganho:", fg=foreground, bg=background, font=default).grid(row=3)
        Label(self.third, text=answer[dictionary[1]["Chest"]], fg=colour[dictionary[1]["Chest"]], bg=background,
              font=default).grid(row=3, column=1)

        # Third champion
        self.fourth = Frame(master, bg=background)
        self.fourth.pack()
        self.fourth.place(x=400, y=520)

        # Third champion image
        link = urlopen(dictionary[2]["Image"]).read()
        data = Image.open(io.BytesIO(link))
        width, height = data.size
        data = data.resize((width // 4, height // 4), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(data)
        image = image
        show = Label(master, image=image, bg=background)
        show.image = image
        show.place(x=50, y=500)

        # Third champion info
        Label(self.fourth, text="Nome:", fg=foreground, bg=background, font=default).grid(row=0)
        Label(self.fourth, text=dictionary[2]["Name"] + ", " + dictionary[2]["Title"],
              fg=colours[dictionary[2]["Tags"][0]], bg=background, font=default).grid(row=0, column=1)
        Label(self.fourth, text="Masteria:", fg=foreground, bg=background, font=default).grid(row=1)
        Label(self.fourth, text=dictionary[2]["Mastery"], fg=foreground, bg=background, font=default).grid(row=1,
                                                                                                           column=1)
        Label(self.fourth, text="Pontos de Masteria:", fg=foreground, bg=background, font=default).grid(row=2)
        Label(self.fourth, text=dictionary[2]["Score"], fg=foreground, bg=background, font=default).grid(row=2,
                                                                                                         column=1)
        Label(self.fourth, text="Baú ganho:", fg=foreground, bg=background, font=default).grid(row=3)
        Label(self.fourth, text=answer[dictionary[2]["Chest"]], fg=colour[dictionary[2]["Chest"]], bg=background,
              font=default).grid(row=3, column=1)


root = Tk()
root.title("League Viwer")
root.resizable(False, False)
root["background"] = "#182422"
root.geometry("1100x700")
root.update()
# Screen(root, name, key)
root.mainloop()
