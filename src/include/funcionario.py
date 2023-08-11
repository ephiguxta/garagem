class Funcionario(PessoaFisica):
    '''
    Essa classe deve ser instanciada quando houver a
    necessidade de inserir um novo funcionário ao banco
    de dados.
    '''

    def __init__(self, cpf, nome, endereco, numero, bairro, cep, telefone,
                 email, rg, dataNasc, sexo, cargo, salario):

        super().__init__(self, cpf, nome, endereco, numero, bairro, cep,
                         telefone, email, rg, dataNasc, sexo):
        self._cargo = cargo
        self._salario = salario

    def getCargo(self):
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSalario(self):
        return self._salario

    def setSalario(self, salario):
        self._salario = salario

    #FIXME: assim como na classe Pessoa, qual a funcionalidade
    # desse método?
    def vender(self, placa):
        pass

