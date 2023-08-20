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
