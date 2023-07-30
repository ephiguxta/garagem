class Funcionario(PessoaFisica):
    def __init__(self, nome, endereco, numero, bairro, cep, telefone, email):
        super().__init__(self, cargo, salario)
        self._cargo = cargo
        self._salario = salario

#metodos getters e setters
    def getCargo(self):
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSalario(self):
        return self._salario

    def setSalario(self, salario)
        self._salario = salario

    def vender(self, placa):
        pass
