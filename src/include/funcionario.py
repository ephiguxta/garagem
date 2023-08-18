import customtkinter
from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        self.cargo = customtkinter.StringVar()
        self.salario = customtkinter.StringVar()
