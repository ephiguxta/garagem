from pessoa import Pessoa
import customtkinter


class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        self._cargo = customtkinter.StringVar()
        self._salario = customtkinter.StringVar()

    def setCargo(self, cargo):
        self._cargo = cargo

    def setSalario(self, salario):
        self._salario = salario
