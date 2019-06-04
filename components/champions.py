from tkinter import *
import urllib
import requests
import io
from PIL import ImageTk, Image
from services import most_played_champions
from services import menu_service


class Screen:
    def __init__(self, master=None):
        # First container
        self.first = Frame(master)
        self.first.pack()
        # Title
        self.title = Label(self.first)
        self.title["text"] = "Campeões mais jogados"
        self.title["bg"] = "#182422"
        self.title["font"] = ("Verdana", "15", "bold")
        self.title["padx"] = 100
        self.title.pack()
        # First champion
        self.first_champion = Listbox(master)
        self.first_champion.insert(1, dictionary[0]["Name"])
        self.first_champion.insert(3, dictionary[0]["Mastery"])
        self.first_champion.insert(5, dictionary[0]["Score"])
        self.first_champion.insert(7, dictionary[0]["Chest"])
        self.first_champion.pack()
        # Second champion
        self.second_champion = Listbox(master)
        self.second_champion.insert(1, dictionary[1]["Name"])
        self.second_champion.insert(3, dictionary[1]["Mastery"])
        self.second_champion.insert(5, dictionary[1]["Score"])
        self.second_champion.insert(7, dictionary[1]["Chest"])
        self.second_champion.pack()
        # Third champion
        self.third_champion = Listbox(master)
        self.third_champion.insert(1, dictionary[2]["Name"])
        self.third_champion.insert(3, dictionary[2]["Mastery"])
        self.third_champion.insert(5, dictionary[2]["Score"])
        self.third_champion.insert(7, dictionary[2]["Chest"])
        self.third_champion.pack()

    # images = []
    #
    # def champion_images(self, name, key):
    #    for j in names["data"].keys():
    #        for i in range(3):
    #            if names["data"][key]["id"] == name:
    #                data = urllib.request.urlopen(most_played_champions.get_image(names["data"][key]["id"])).read()
    #                opening = Image.open(io.BytesIO(data))
    #                image = ImageTk.PhotoImage(opening)
    #                label = Label(root, image=image)
    #                label.grid(column=i)
    #                images.append(image)

root = Tk()
root.title = "League Viwer"
root["background"] = "#182422"
Screen(root)
root.mainloop()

# ID = menu_service.summonerByName("Yoda", "RGAPI-6a76510a-6efe-43a3-9393-a834c9eb9a08")
# dictionary = menu_service.most_played_champions(ID, "RGAPI-6a76510a-6efe-43a3-9393-a834c9eb9a08")
# names = menu_service.generateJsonChamps()
