import customtkinter

class Venda:
    def __init__(self):
        self.cpfCliente = customtkinter.StringVar()
        self.cpfFuncionario = customtkinter.StringVar()
        self.dataVenda = customtkinter.StringVar()
        self.placaVeiculo = customtkinter.StringVar()
