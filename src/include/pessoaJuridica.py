class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, numero, bairro, cep, telefone, email):
        super().__init__(self, nomeFantasia, cnpj)
        self._nomeFantasia = nomeFantasia
        self._cnpj = cnpj

#metodos getters e setters
    def getNomeFantasia(self):
        return self._nomeFantasia

    def setNomeFantasia(self, nomeFantasia):
        self._nomeFantasia = nomeFantasia

    def getCnpj(self):
        return self._cnpj

    def setCnpj(self, cnpj):
        self._cnpj = cnpj
