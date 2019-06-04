from tkinter import *
# import urllib
# import requests
# import io
# from PIL import ImageTk, Image
# from services import most_played_champions
# from services import menu_service

back = "#182422"
front = "#F3E171"
default = ("Verdana", "15", "italic", "bold")

# ID = menu_service.summonerByName("Yoda", "RGAPI-e02de77d-5dd2-4a65-8df1-9b8b73dfb05d")
# dictionary = most_played_champions.most_played_champions(ID.id, "RGAPI-e02de77d-5dd2-4a65-8df1-9b8b73dfb05d")
# names = menu_service.generateJsonChamps()
dictionary = [{"Name": "Anything",
               "Mastery": 5,
               "Score": 10000,
               "Chest": False}]

colours = {"Fighter": "#933A16",
           "Assassin": "#D64142",
           "Tank": "#A4DD86",
           "Marksman": "#D6BA7B",
           "Mage": "#9CA6F7",
           "Support": "#44ACB5"}


class Screen:
    def __init__(self, master=None):

        # Title
        self.first = Frame(master)
        self.first.pack()
        self.title = Label(self.first, text="Campeões Mais Jogados", fg="Snow", bg="#182422", font=("Verdana", "30", "bold"))
        self.title.pack()

        earned = dictionary[0]["Chest"]
        answer = {True: "Sim",
                  False: "Não"}
        colour = {True: "#50C878",
                  False: "#CA3433"}

        # First champion
        self.second = Frame(master, bg=back)
        self.second.pack()
        self.second.place(x=300, y=100)
        Label(self.second, text="Nome:", fg=front, bg=back, font=default).grid(row=0)
        Label(self.second, text=dictionary[0]["Name"], fg=front, bg=back, font=default).grid(row=0, column=1)
        Label(self.second, text="Masteria:", fg=front, bg=back, font=default).grid(row=1)
        Label(self.second, text=dictionary[0]["Mastery"], fg=front, bg=back, font=default).grid(row=1, column=1)
        Label(self.second, text="Pontos de Masteria:", fg=front, bg=back, font=default).grid(row=2)
        Label(self.second, text=dictionary[0]["Score"], fg=front, bg=back, font=default).grid(row=2, column=1)
        Label(self.second, text="Baú ganho:", fg=front, bg=back, font=default).grid(row=3)
        Label(self.second, text=answer[earned], fg=colour[earned], bg=back, font=default).grid(row=3, column=1)

        # Second champion
        self.third = Frame(master, bg=back)
        self.third.pack()
        self.third.place(x=300, y=300)
        Label(self.third, text="Nome:", fg=front, bg=back, font=default).grid(row=0)
        Label(self.third, text=dictionary[0]["Name"], fg=front, bg=back, font=default).grid(row=0, column=1)
        Label(self.third, text="Masteria:", fg=front, bg=back, font=default).grid(row=1)
        Label(self.third, text=dictionary[0]["Mastery"], fg=front, bg=back, font=default).grid(row=1, column=1)
        Label(self.third, text="Pontos de Masteria:", fg=front, bg=back, font=default).grid(row=2)
        Label(self.third, text=dictionary[0]["Score"], fg=front, bg=back, font=default).grid(row=2, column=1)
        Label(self.third, text="Baú ganho:", fg=front, bg=back, font=default).grid(row=3)
        Label(self.third, text=answer[earned], fg=colour[earned], bg=back, font=default).grid(row=3, column=1)

        # Third champion
        self.fourth = Frame(master, bg=back)
        self.fourth.pack()
        self.fourth.place(x=300, y=500)
        Label(self.fourth, text="Nome:", fg=front, bg=back, font=default).grid(row=0)
        Label(self.fourth, text=dictionary[0]["Name"], fg=front, bg=back, font=default).grid(row=0, column=1)
        Label(self.fourth, text="Masteria:", fg=front, bg=back, font=default).grid(row=1)
        Label(self.fourth, text=dictionary[0]["Mastery"], fg=front, bg=back, font=default).grid(row=1, column=1)
        Label(self.fourth, text="Pontos de Masteria:", fg=front, bg=back, font=default).grid(row=2)
        Label(self.fourth, text=dictionary[0]["Score"], fg=front, bg=back, font=default).grid(row=2, column=1)
        Label(self.fourth, text="Baú ganho:", fg=front, bg=back, font=default).grid(row=3)
        Label(self.fourth, text=answer[earned], fg=colour[earned], bg=back, font=default).grid(row=3, column=1)


root = Tk()
root.title = "League Viwer"
root["background"] = "#182422"
root.geometry("900x700")
Screen(root)
root.mainloop()
