from tkinter import *
import json
import requests
from PIL import ImageTk, Image

class InfoInvocador:
    def __init__(self, root, inv):
        self.root = root
        idIcone = getattr(inv, "profileIconId")
        icon = requests.get()
