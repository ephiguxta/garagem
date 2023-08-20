import customtkinter


class Veiculo:
    def __init__(self):
        self.modelo = customtkinter.StringVar()
        self.marca = customtkinter.StringVar()
        self.ano = customtkinter.StringVar()
        self.cor = customtkinter.StringVar()
        self.preco = customtkinter.StringVar()
        self.placa = customtkinter.StringVar()
        self.kmRodados = customtkinter.StringVar()

    def setModelo(self, value):
        self.modelo = value

    def setMarca(self, value):
        self.marca = value

    def setAno(self, value):
        self.ano = value

    def setCor(self, value):
        self.cor = value

    def setPreco(self, value):
        self.preco = value

    def setPlaca(self, value):
        self.placa = value

    def setKmRodados(self, value):
        self.kmRodados = value
