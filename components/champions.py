from tkinter import *
# import urllib
# import requests
# import io
# from PIL import ImageTk, Image
from services import most_played_champions
from services import menu_service

back = "#182422"
front = "#F3E171"
f = ("Verdana", "15", "bold")

ID = menu_service.summonerByName("Yoda", "RGAPI-283f25a0-c771-4c65-80af-f387548385fc")
dictionary = most_played_champions.most_played_champions(ID.id, "RGAPI-283f25a0-c771-4c65-80af-f387548385fc")
names = menu_service.generateJsonChamps()
print(*dictionary, sep="\n")


class Screen:
    def __init__(self, master=None):

        # First container
        self.first = Frame(master)
        self.first.pack()

        # Second container
        self.second = Frame(master, bg=back)
        self.second.pack()

        # Third container
        self.third = Frame(master, bg=back)
        self.third.pack()

        # Fourth container
        self.fourth = Frame(master, bg=back)
        self.fourth.pack()

        # Title
        self.title = Label(self.first)
        self.title["text"] = "Campeões Mais Jogados"
        self.title["fg"] = "Snow"
        self.title["bg"] = "#182422"
        self.title["font"] = ("Verdana", "30", "bold")
        self.title.pack(side="left")

        # First champion
        earned = dictionary[0]["Chest"]
        answer = {True: "Sim",
                  False: "Não"}
        colour = {True: "Green",
                  False: "Red"}
        Label(self.second, text="Nome:", fg=front, bg=back, font=f).grid(row=0)
        Label(self.second, text=dictionary[0]["Name"], fg="Yellow", bg=back, font=f).grid(row=0, column=1)
        Label(self.second, text="Maestria:", fg=front, bg=back, font=f).grid(row=1)
        Label(self.second, text=dictionary[0]["Mastery"], fg="Yellow", bg=back, font=f).grid(row=1, column=1)
        Label(self.second, text="Pontos de maestria:", fg=front, bg=back, font=f).grid(row=2)
        Label(self.second, text=dictionary[0]["Mastery"], fg="Yellow", bg=back, font=f).grid(row=2, column=1)
        Label(self.second, text="Ganhou baú:", fg=front, bg=back, font=f).grid(row=3)
        Label(self.second, text=answer[earned], fg=colour[earned], bg=back, font=f).grid(row=3, column=1)


root = Tk()
root.title = "League Viwer"
root["background"] = "#182422"
root.geometry("900x700")
Screen(root)
root.mainloop()
