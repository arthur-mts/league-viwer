from tkinter import *


class Screen:
    def __init__(self, master=None):
        # First container
        self.first = Frame(master)
        self.first.pack()
        # Second container
        self.second = Frame(master)
        self.second.pack()
        # Third container
        self.third = Frame(master)
        self.third.pack()
        # Fourth container
        self.fourth = Frame(master)
        self.fourth.pack()
        # Fifth container
        self.fifth = Frame(master)
        self.fifth.pack()
        # Sixth container
        self.sixth = Frame(master)
        self.sixth.pack()
        # Title
        self.title = Label(self.first)
        self.title["text"] = "Campeões mais jogados"
        self.title["fg"] = "White"
        self.title["bg"] = "Black"
        self.title["font"] = ("Verdana", "15", "bold")
        self.title["padx"] = 100
        self.title.pack()


root = Tk()
Screen(root)
root.mainloop()
