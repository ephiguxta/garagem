from pessoa import Pessoa
import customtkinter

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        self._cargo = customtkinter.StringVar()
        self._salario = customtkinter.StringVar()

    def getCargo(self):
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSalario(self):
        return self._salario
    
    def setSalario(self, salario):
        self._salario = salario
