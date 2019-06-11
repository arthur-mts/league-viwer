from tkinter import *
from urllib.request import urlopen
import io
import json
from PIL import ImageTk, Image
from services import most_played_champions
from services import menu_service

back = "#182422"
front = "#F3E171"
default = ("Verdana", "15", "italic", "bold")

colours = {"Fighter": "#933A16",
           "Assassin": "#D64142",
           "Tank": "#A4DD86",
           "Marksman": "#D6BA7B",
           "Mage": "#9CA6F7",
           "Support": "#44ACB5"}

answer = {True: "Sim", False: "Não"}
colour = {True: "#50C878", False: "#CA3433"}

search = menu_service.summonerByName("Anyone", "RGAPI-92b2157f-c7f6-4a2d-a4d2-aedb3352dbf5")
dictionary = most_played_champions.most_played_champions(search.id, "RGAPI-92b2157f-c7f6-4a2d-a4d2-aedb3352dbf5")

with open("../src/champions_data.json", "r") as file:
    data = json.load(file)
    file.close()
with open("../src/champions_data.json", "w") as file:
    data[search.name] = dictionary
    json.dump(data, file, indent=3)
with open("../src/champions.json", "r") as file:
    data = json.load(file)
    file.close()
with open("../src/champions.json", "w") as file:
    data[search.name] = [dictionary[i]["ID"] for i in range(3)]
    json.dump(data, file, indent=3)


class Screen:

    def __init__(self, master=None):

        # Title
        self.first = Frame(master)
        self.first.pack()
        self.title = Label(self.first, text="Campeões Mais Jogados", fg="Snow", bg=back, font=("Verdana", "30",
                                                                                               "italic", "bold"))
        self.title.pack()

        # First champion
        self.second = Frame(master, bg=back)
        self.second.pack()
        self.second.place(x=400, y=120)

        # Second champion
        self.third = Frame(master, bg=back)
        self.third.pack()
        self.third.place(x=400, y=320)

        # Third champion
        self.fourth = Frame(master, bg=back)
        self.fourth.pack()
        self.fourth.place(x=400, y=520)

        # Render images
        for i in range(3):
            self.render(i, 50, 100 if i == 0 else 300 if i == 1 else 500, master)

        # Render info
        for j in range(3):
            number = self.second if j == 0 else self.third if j == 1 else self.fourth
            self.info(number, j)

    # Render images
    def render(self, number, x, y, master):
        link = urlopen(dictionary[number]["Image"]).read()
        archive = Image.open(io.BytesIO(link))
        width, height = archive.size
        archive = archive.resize((width // 4, height // 4), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(archive)
        image = image
        show = Label(master, image=image, bg=back)
        show.image = image
        show.place(x=x, y=y)

    # Render info
    def info(self, frame, i):
        Label(frame, text="Nome:", fg=front, bg=back, font=default).grid(row=0)
        Label(frame, text=data[search.name][i]["Name"] + ", " + data[search.name][i]["Title"],
              fg=colours[data[search.name][i]["Tags"][0]], bg=back, font=default).grid(row=0, column=1)
        Label(frame, text="Maestria:", fg=front, bg=back, font=default).grid(row=1)
        Label(frame, text=data[search.name][i]["Mastery"], fg=front, bg=back, font=default).grid(row=1, column=1)
        Label(frame, text="Pontos de Maestria:", fg=front, bg=back, font=default).grid(row=2)
        Label(frame, text=data[search.name][i]["Score"], fg=front, bg=back, font=default).grid(row=2, column=1)
        Label(frame, text="Baú ganho:", fg=front, bg=back, font=default).grid(row=3)
        Label(frame, text=answer[data[search.name][i]["Chest"]], fg=colour[data[search.name][i]["Chest"]], bg=back,
              font=default).grid(row=3, column=1)


# Creating window
root = Tk()
root.title("League Viwer")
root.resizable(False, False)
root["background"] = back
root.geometry("1100x700")
root.update()
Screen(root)
root.mainloop()
