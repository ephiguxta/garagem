class Pessoa:
    '''
    Serve de base para Pessoa Física/Jurídica,
    aqui temos os dados básicos do funcionário/comprador
    '''

    def __init__(self, nome, endereco, numero, bairro, cep, telefone, email):
        self._nome = nome
        self._endereco = endereco
        self._numero = numero
        self._bairro = bairro
        self._cep = cep
        self._telefone = telefone
        self._email = email

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEndereco(self):
        return self._endereco

    def setEndereco(self, endereco):
        self._endereco = endereco

    def getNumero(self):
        return self._numero

    def setNumero(self, numero):
        self._numero = numero

    def getBairro(self):
        return self._bairro

    def setBairro(self, bairro):
        self._bairro = bairro

    def getCep(self):
        return self._cep

    def setCep(self, cep):
        self._cep = cep

    def getTelefone(self):
        return self._telefone

    def setTelefone(self, telefone):
        self._telefone = telefone

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    # FIXME: qual a funcionalidade desse método?
    def pagar(self, preco):
        pass
