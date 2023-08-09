class PessoaJuridica(Pessoa):
    def __init__(self, cpf, nome, endereco, numero, bairro, cep, telefone, email,
                 nome_empresa, cnpj):

        super().__init__(self, cpf, nome, endereco, numero, bairro, cep,
                         telefone, email)
        self._nomeEmpresa= nomeEmpresa
        self._cnpj = cnpj

    def getNomeFantasia(self):
        return self._nomeFantasia

    def setNomeFantasia(self, nomeFantasia):
        self._nomeFantasia = nomeFantasia

    def getCnpj(self):
        return self._cnpj

    def setCnpj(self, cnpj):
        self._cnpj = cnpj
