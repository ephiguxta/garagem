import customtkinter

class Pessoa:
    def __init__(self):
        self.cpf = customtkinter.StringVar()
        self.rg = customtkinter.StringVar()
        self.nome = customtkinter.StringVar()
        self.endereco = customtkinter.StringVar()
        self.numero = customtkinter.StringVar()
        self.bairro = customtkinter.StringVar()
        self.cep = customtkinter.StringVar()
        self.telefone = customtkinter.StringVar()
        self.email = customtkinter.StringVar()
