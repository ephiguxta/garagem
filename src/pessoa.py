import customtkinter


class Pessoa:
    def __init__(self):
        self._cpf = customtkinter.StringVar()
        self._rg = customtkinter.StringVar()
        self._nome = customtkinter.StringVar()
        self._endereco = customtkinter.StringVar()
        self._numero = customtkinter.StringVar()
        self._bairro = customtkinter.StringVar()
        self._cep = customtkinter.StringVar()
        self._telefone = customtkinter.StringVar()
        self._email = customtkinter.StringVar()

    def setCpf(self, value):
        self._cpf = value

    def setRg(self, value):
        self._rg = value

    def setNome(self, value):
        self._nome = value

    def setEndereco(self, value):
        self._endereco = value

    def setNumero(self, value):
        self._numero = value

    def setBairro(self, value):
        self._bairro = value

    def setCep(self, value):
        self._cep = value

    def setTelefone(self, value):
        self._telefone = value

    def setEmail(self, value):
        self._email = value
