import json
from tkinter import *
from services import menu_service, api_service
from PIL import ImageTk, Image
global bg
bg = "#182422"


class MenuAut:
    def __init__(self, root):
        self.root = root
        self.container = Frame(root)
                #self.container.pack()
        self.container.grid(row = 0, column = 2, columnspan = 2)
        self.container.place(x = 340, y = 0)
        # Redimensionando logo
        img = Image.open('../src/img/lol_logo.png')
        width, height = img.size
        img = img.resize((width // 2, height // 2), Image.ANTIALIAS)
        self.logoImg = ImageTk.PhotoImage(img)

        self.painel = Label(self.container, image=self.logoImg, bg = bg)
        self.painel.image = self.logoImg
        self.painel.grid_columnconfigure(0, weight = 1)
        self.painel.grid_rowconfigure(0, weight = 1)
        self.painel.pack(anchor=W, fill=Y, expand=False, side=LEFT)

        try:
            with open("../src/dados/key.json") as r:
                self.arquivo = json.load(r)
                self.validado = menu_service.validarKey(self.arquivo["senha"]);
        except:
            self.validado = False

        if self.validado:
            self.key = self.arquivo["senha"]
            self.renderOpcoes()
        else:
            self.renderAutenticar()

    def actionAutenticar(self):
        self.key = self.keyEnter.get()
        if menu_service.validarKey(self.key):
            self.botaoAut["text"] = "Chave validada!"
            self.botaoAut["bg"] = "green"
            validado = {'senha': self.key}
            with open("../src/dados/key.json", "w", encoding='utf-8') as arquivo:
                json.dump(validado, arquivo)
                arquivo.close()
            self.container2.destroy()
            self.container3.destroy()
            self.renderOpcoes()
        else:
            self.keyEnter.delete(0, END)
            self.botaoAut["text"] = "Erro de autenticação"
            self.botaoAut["bg"] = "yellow"

    def renderAutenticar(self):
        self.container2 = Frame(self.root)
        self.container2["pady"] = 10
        #self.container2.pack(side = LEFT)
        self.container2.grid(column = 2, row = 0, columnspan = 2)
        self.textoAut = Label(self.container2, text="Digite sua chave de acesso: ")
        self.textoAut["font"] = ("20")
        self.textoAut.grid(sticky = E)
        self.keyEnter = Entry(self.container2)
        self.keyEnter.grid(column = 1, row = 0)
        #self.keyEnter.pack(side=LEFT)
        #self.container3 = Frame(self.root)
        #self.container3.pack()
        #self.container3.grid()
        self.botaoAut = Button(self.container2, text="Autenticar")
        self.botaoAut["command"] = self.actionAutenticar
        self.botaoAut.grid(rowspan = 2)
        #self.botaoAut.pack(side=TOP)
    

    def renderOpcoes(self):
        #self.container2 = Frame(self.root, highlightbackground="red", highlightcolor="red", highlightthickness=1, pady = 20)
#, pady=50, padx=20
        #self.container2.pack(side = LEFT)
        #self.container2.grid(co)

        self.invocador = api_service.checarInvSalvo()
        print(self.invocador)


        if(self.invocador):
            self.renderInvocador()
            self.renderSalvarInvocador()
        else:
            self.renderSalvarInvocador()



            
    def renderInvocador(self):

        if hasattr(self, "frameInvSalvo"):
            self.frameInvSalvo.destroy()
        

        self.frameInvSalvo = Frame(self.root, width=100, height=100, bg = bg)
        #self.frameInvSalvo.pack(side = LEFT)

        self.frameInvSalvo.grid(row = 0, column = 0, pady=20)
        #print(self.root.grid_location(50,0 ))        
        self.frameInvSalvo.place(x = 20, y = 20)   

        icon = api_service.iconeInv(self.invocador)
        width, height = icon.size
        icon = icon.resize((75, 75), Image.ANTIALIAS)
        self.imgIcon  = ImageTk.PhotoImage(icon)

        #self.canvasImg = Canvas(self.frameInvSalvo, width = 75, height = 75)
        #self.canvasImg.grid(column = 0, row = 0)
        #self.canvasImg.create_image((0,0),image = self.imgIcon, anchor = NW)
        #self.canvasImg.image = self.imgIcon
        self.labelImg = Label(self.frameInvSalvo, image = self.imgIcon)
        self.labelImg.grid(row = 0, column = 0, sticky = E)
        
        nomeInv = getattr(self.invocador, "name")
        self.labelInvocador = Label(self.frameInvSalvo)
        self.labelNome = Label(self.frameInvSalvo, text = nomeInv, font="termite 15 bold", bg = bg)
        self.labelNome.grid(column = 1, row = 0)


        




        

    def renderSalvarInvocador(self):
        
        self.frameInv = Frame(self.root, bg = bg)
        #self.frameInv.pack(side = BOTTOM, ensure = LEFT)
        self.frameInv.grid(row = 1, pady = 20) 
        self.frameInv.place(x = 10, y = 200)

        #self.labelTxt = Label(self.frameInv, text = "Digite seu nome invocador: ")
        #self.labelTxt["font"] = ("Nerdfont", 10,"bold")
        #self.labelTxt.grid(column = 0,row = 0, sticky = E)
        #self.labelTxt.pack(side = LEFT)

        self.inputNome = Entry(self.frameInv, width=25, font="bold", fg='#96752F')
        self.inputNome.insert(0, "Digite seu nome invocador: ")
        self.inputNome.grid(row = 0, column = 0)

        self.botaoSalvar = Button(self.frameInv, text="Buscar", anchor = CENTER)
        self.botaoSalvar["command"] = self.actionSalvarInvoc
        self.botaoSalvar.grid(row = 1, column = 0)



                #self.inputNome.pack()

        #self.frameBot = Frame(self.frameInv)
        #self.frameBot.grid(row = 1, columnspan = 2)
        #self.frameBot.pack()

                #self.botaoSalvar.grid(rowspan = 2)
        #self.botaoSalvar.grid(row = 2, column = 1)

        
    
    def actionSalvarInvoc(self):
        nome = self.inputNome.get()
        invoc = menu_service.summonerByName(nome, self.key) 
        if(invoc == "ERRO"):
            self.inputNome.delete(0,END)
            self.botaoSalvar["bg"] = "red"
            self.botaoSalvar["text"] = "Invocador nao encontrado"
        else:
            self.invocador = invoc
            self.botaoSalvar["text"] = "Salvo!"
            self.inputNome["background"] = "#4EC375"
            api_service.salvarInv(invoc)
            self.renderInvocador()
            

    



root = Tk()
root.title("League Viwer")

root.geometry("900x700")
root["background"] = "#182422"
root.update()
MenuAut(root)
root.mainloop()
