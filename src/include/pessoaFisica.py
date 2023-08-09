class PessoaFisica(Pessoa):
    '''
    A instância desse objeto vai servir para a
    inserção dos dados no banco de dados
    '''

    def __init__(self, cpf, nome, endereco, numero, bairro, cep, telefone, email,
                 rg, dataNasc, sexo):

        super().__init__(self, cpf, nome, endereco, numero, bairro, cep, telefone, email)

        self._rg = rg
        self._dataNasc = dataNasc
        self._sexo = sexo

    def getRg(self):
        return self._rg

    def setRg(self, rg):
        self._rg = rg

    def getDataNasc(self):
        return self._dataNasc

    def setDataNasc(self, dataNasc):
        self._dataNasc = dataNasc

    def getSexo(self):
        return self._sexo

    def setSexo(self, sexo):
        self._sexo = sexo

