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

    def getCpf(self):
        return self._cpf.get()

    def setCpf(self, value):
        self._cpf = value

    def getRg(self):
        return self._rg.get()

    def setRg(self, value):
        self._rg = value

    def getNome(self):
        return self._nome.get()

    def setNome(self, value):
        self._nome = value

    def getEndereco(self):
        return self._endereco.get()

    def setEndereco(self, value):
        self._endereco = value

    def getNumero(self):
        return self._numero.get()

    def setNumero(self, value):
        self._numero = value

    def getBairro(self):
        return self._bairro.get()

    def setBairro(self, value):
        self._bairro = value

    def getCep(self):
        return self._cep.get()

    def setCep(self, value):
        self._cep = value

    def getTelefone(self):
        return self._telefone.get()

    def setTelefone(self, value):
        self._telefone = value

    def getEmail(self):
        return self._email.get()

    def setEmail(self, value):
        self._email = value
