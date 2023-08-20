import customtkinter


class Venda:
    def __init__(self):
        self.cpfCliente = customtkinter.StringVar()
        self.cpfFuncionario = customtkinter.StringVar()
        self.dataVenda = customtkinter.StringVar()
        self.placaVeiculo = customtkinter.StringVar()

    def setCpfCliente(self, value):
        self.cpfCliente = value

    def setCpfFuncionario(self, value):
        self.cpfFuncionario = value

    def setDataVenda(self, value):
        self.dataVenda = value

    def setPlacaVeiculo(self, value):
        self.placaVeiculo = value
