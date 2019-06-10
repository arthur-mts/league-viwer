from tkinter import *
from PIL import Image, ImageTk
from services import *

global bg
bg = "#182422"

global fg
fg = "#F3E171"

class EstatisticasInvo:
    def __init__(self, invocador, key):
        self.invocador = invocador
        self.key = key
