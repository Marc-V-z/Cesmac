import json

class Config:
    def __init__(self):
        self.Favoritos = []
        self.Tema = "Branco"
        self.InterfaceV = "beta2"

        self.cor1 = "White", "White"            # cor das entradas de texto, output
        self.cor2 = "Lightgray"        # cor dos botões
        self.cor3 = "White"            # cor dos fundos
        self.cor4 = "Gainsboro"        # cor do fundo diretorio
        self.cor5 = "Black", "White","Black"   # cor do texto e cor caso o fundo seja escuro, caso seja output
        self.cor6 = "Lightgray"        # cor do frame de comandos

        self.dados = {"Favoritos": self.Favoritos, "Tema": self.Tema, "InterfaceV": self.InterfaceV } # dicionario
        self.temas = ["Branco","Cinza", "Preto", "Dark", "Metal", "Aqua", "AquaMarine", "Darker", "Tester"]

        self.Cores_Update()

    def Adicionar_Favorito(self, caminho):
        self.Favoritos.append(caminho)

    def Remover_Favorito(self, i):
        self.Favoritos.pop(i)

    def Load_Config(self):
        try:
            with open('Config.json', 'r') as file: 
                self.dados = json.load(file)
                self.Favoritos = self.dados["Favoritos"]
                self.Tema = self.dados["Tema"]
                self.InterfaceV = self.dados["InterfaceV"]
            self.Cores_Update()
        except:
            self.Save_Config()

    def Save_Config(self):
        with open('Config.json', 'w') as file: 
            json.dump(self.dados, file,indent=4)

    def Cores_Update(self):
        match self.Tema:
            case "Branco":
                self.cor1 = "White", "White"
                self.cor2 = "Lightgray"
                self.cor3 = "White"
                self.cor4 = "Gainsboro"
                self.cor4 = "Gainsboro"
                self.cor5 = "Black", "Black", "Black"
                self.cor6 = "Lightgray"
            case "Cinza":
                self.cor1 = "White", "White"
                self.cor2 = "gray"
                self.cor3 = "Lightgray"
                self.cor4 = "Gainsboro"
                self.cor5 = "Black", "White", "Black"
                self.cor6 = "Lightgray"
            case "Preto":
                self.cor1 = "White", "White"
                self.cor2 = "gray"
                self.cor3 = "Lightgray"
                self.cor4 = "Gainsboro"
                self.cor5 = "Black", "White", "Black"
                self.cor6 = "Gray"
            case "Dark":
                self.cor1 = "Lightgray", "Lightgray"
                self.cor2 = "Gray"
                self.cor3 = "Lightgray"
                self.cor4 = "Gray"
                self.cor5 = "Black", "White", "Black"
                self.cor6 = "DimGray"
            case "Metal":
                self.cor1 = "Lightgray", "Lightgray"
                self.cor2 = "LightSlateGray"
                self.cor3 = "Lightgray"
                self.cor4 = "Gainsboro"
                self.cor5 = "Black", "White", "Black"
                self.cor6 = "Lightgray"
            case "Aqua":
                self.cor1 = "White", "White"
                self.cor2 = "SkyBlue"
                self.cor3 = "PowderBlue"
                self.cor4 = "Gainsboro"
                self.cor5 = "Black", "Black", "Black"
                self.cor6 = "LightBlue"
            case "AquaMarine":
                self.cor1 = "White", "White"
                self.cor2 = "DarkBlue"
                self.cor3 = "Blue"
                self.cor4 = "LightBlue"
                self.cor5 = "Black", "White", "Black"
                self.cor6 = "Lightblue"
            case "Darker":
                self.cor1 = "Lightgray", "Black"
                self.cor2 = "Gray"
                self.cor3 = "DarkGray"
                self.cor4 = "Dimgray"
                self.cor5 = "Black", "White", "White"
                self.cor6 = "Dimgray"
            case "Tester":
                self.cor1 = "LightSlateGray", "DarkSlateGray"
                self.cor2 = "Silver"
                self.cor3 = "SlateGray"
                self.cor4 = "SteelBlue"
                self.cor5 = "Black", "Black", "White"
                self.cor6 = "DeepSkyBlue"

