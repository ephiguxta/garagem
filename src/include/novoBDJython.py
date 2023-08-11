import sqlite3
from sqlite3 import Error

bdJython = 'bdGaragemJython.db'

# Função para conectar ao banco de dados
def criarConexao():
    try:
        conexao = sqlite3.connect(bdJython)
        return conexao
    except Error as erro:
        print(erro)
        return None

# Função para criar as tabelas
def criarTabelas():
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS GaragemJython (
                    cnpjJython VARCHAR(18) NOT NULL,
                    nomeFantasia VARCHAR(45) NOT NULL,
                    endereco VARCHAR(45) NOT NULL,
                    bairro VARCHAR(45) NOT NULL,
                    numero INT NOT NULL,
                    cep VARCHAR(20) NOT NULL,
                    email VARCHAR(45) NOT NULL,
                    PRIMARY KEY (cnpjJython)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Funcionario (
                    cpfFuncionario VARCHAR(14) NOT NULL,
                    rg VARCHAR(16) NOT NULL,
                    nome VARCHAR(45) NOT NULL,
                    cargo VARCHAR(45) NOT NULL,
                    salario FLOAT NOT NULL,
                    endereco VARCHAR(45) NOT NULL,
                    bairro VARCHAR(45) NOT NULL,
                    numero INT NOT NULL,
                    cep VARCHAR(45) NOT NULL,
                    email VARCHAR(45) NOT NULL,
                    PRIMARY KEY (cpfFuncionario)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Veiculo (
                    placa VARCHAR(9) NOT NULL,
                    marca VARCHAR(45) NOT NULL,
                    modelo VARCHAR(45) NOT NULL,
                    ano DATE NOT NULL,
                    cor VARCHAR(45) NOT NULL,
                    kmRodados INT NOT NULL,
                    preco FLOAT NOT NULL,
                    PRIMARY KEY (placa)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS PessoaFisica (
                    cpfPessoaFisica VARCHAR(14) NOT NULL,
                    rg VARCHAR(16) NOT NULL,
                    nome VARCHAR(45) NOT NULL,
                    endereco VARCHAR(45) NOT NULL,
                    bairro VARCHAR(45) NOT NULL,
                    numero INT NOT NULL,
                    cep VARCHAR(45) NOT NULL,
                    email VARCHAR(45) NOT NULL,
                    dataNasc DATE NOT NULL,
                    PRIMARY KEY (cpfPessoaFisica)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS PessoaJuridica (
                    cnpjPessoaJuridica VARCHAR(18) NOT NULL,
                    nomeFantasia VARCHAR(45) NOT NULL,
                    endereco VARCHAR(45) NOT NULL,
                    bairro VARCHAR(45) NOT NULL,
                    numero INT NOT NULL,
                    cep VARCHAR(20) NOT NULL,
                    email VARCHAR(45) NOT NULL,
                    
                    PRIMARY KEY (cnpjPessoaJuridica)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Compra (
                    idVenda INTEGER PRIMARY KEY,
                    cnpjJython VARCHAR(18) NOT NULL,
                    cpfFuncionario VARCHAR(14) NOT NULL,
                    cpfPessoaFisica VARCHAR(14),
                    cnpjPessoaJuridica VARCHAR(18),
                    placaVeiculo VARCHAR(9) NOT NULL,
                    FOREIGN KEY (cnpjJython) REFERENCES GaragemJython (cnpjJython),
                    FOREIGN KEY (cpfFuncionario) REFERENCES Funcionario (cpfFuncionario),
                    FOREIGN KEY (cpfPessoaFisica) REFERENCES PessoaFisica (cpfPessoaFisica),
                    FOREIGN KEY (cnpjPessoaJuridica) REFERENCES PessoaJuridica (cnpjPessoaJuridica),
                    FOREIGN KEY (placaVeiculo) REFERENCES Veiculo (placa)
                )
            ''')
            conexao.commit()
            print("Tabelas criadas com sucesso!")
        except Error as erro:
            print("Erro ao criar tabelas:", erro)
        finally:
            conexao.close()

#----- Funções para inserção nas tabelas -----
def inserirGaragemJython(cnpjJython, nomeFantasia,endereco,bairro,numero,cep,email):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO GaragemJython VALUES (?, ?, ?, ?, ?, ?, ?)", (cnpjJython,nomeFantasia,endereco,bairro,str(numero),cep,email))
            conexao.commit()
            print("Registro inserido com sucesso na tabela GaragemJython.")
        except Error as erro:
            print("Erro ao inserir o registro na tabela GaragemJython:", erro)
        finally:
            conexao.close()

def inserirFuncionario(cpfFuncionario, rg, nome, cargo, salario, endereco, bairro, numero, cep, email):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Funcionario VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (cpfFuncionario, rg, nome, cargo, str(salario), endereco, bairro, str(numero), cep, email))
            conexao.commit()
            print("Registro inserido com sucesso na tabela Funcionario.")
        except Error as erro:
            print("Erro ao inserir o registro na tabela Funcionario:", erro)
        finally:
            conexao.close()

def inserirVeiculo(placa,marca,modelo,ano,cor,kmRodados,preco):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Veiculo VALUES (?, ?, ?, ?, ?, ?, ?)",(placa,marca,modelo,str(ano),cor,str(kmRodados),str(preco)))
            conexao.commit()
            print("Registro inserido com sucesso na tabela Veiculo.")
        except Error as erro:
            print("Erro ao inserir o registro na tabela Veiculo:", erro)
        finally:
            conexao.close()

def inserirPessoaFisica(cpfPessoaFisica,rg,nome,endereco,bairro,numero,cep,email,dataNasc):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO PessoaFisica VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)",(cpfPessoaFisica,rg,nome,endereco,bairro,str(numero),cep,email,str(dataNasc)))
            conexao.commit()
            print("Registro inserido com sucesso na tabela PessoaFisica.")
        except Error as erro:
            print("Erro ao inserir o registro na tabela PessoaFisica:", erro)
        finally:
            conexao.close()

def inserirPessoaJuridica(cnpjPessoaJuridica,nomeFantasia,endereco,bairro,numero,cep,email):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO PessoaJuridica VALUES (?, ?, ?, ?, ?, ?, ?)",(cnpjPessoaJuridica,nomeFantasia,endereco,bairro,numero,cep,email))
            conexao.commit()
            print("Registro inserido com sucesso na tabela PessoaJuridica.")
        except Error as erro:
            print("Erro ao inserir o registro na tabela PessoaJuridica:", erro)
        finally:
            conexao.close()

def inserirCompra(idVenda,cnpjJython,cpfFuncionario,cpfPessoaFisica,cnpjPessoaJuridica,placaVeiculo):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Compra VALUES (?, ?, ?, ?, ?, ?)",(idVenda,cnpjJython,cpfFuncionario,cpfPessoaFisica,cnpjPessoaJuridica,placaVeiculo))
            conexao.commit()
            print("Registro inserido com sucesso na tabela Compra.")
        except Error as erro:
            print("Erro ao inserir o registro na tabela Compra:", erro)
        finally:
            conexao.close()

#----- Funções para pesquisar -----
# Função para pesquisar funcionários por CPF
def pesquisarFuncionario(cpfFuncionario):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Funcionario WHERE cpfFuncionario=?", (cpfFuncionario,))
            funcionarios = cursor.fetchall()

            if len(funcionarios) == 0:
                print("Nenhum funcionário encontrado.")
            else:
                print("Funcionários encontrados:")
                for funcionario in funcionarios:
                    print("CPF:", funcionario[0])
                    print("RG:", funcionario[1])
                    print("Nome:", funcionario[2])
                    print("Cargo:", funcionario[3])
                    print("Salário:", funcionario[4])
                    print("Endereço:", funcionario[5])
                    print("Bairro:", funcionario[6])
                    print("Número:", funcionario[7])
                    print("CEP:", funcionario[8])
                    print("Email:", funcionario[9])
                    print("-----------------------")

        except Error as erro:
            print("Erro ao pesquisar Funcionario:", erro)
        finally:
            conexao.close()
#Função para pesquisar por placa do veículo
def pesquisarVeiculo(placa):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Veiculo WHERE placa=?", (placa,))
            veiculos = cursor.fetchall()

            if len(veiculos) == 0:
                print("Nenhum veículo encontrado.")
            else:
                print("Veículo encontrado:")
                for veiculo in veiculos:
                    print("Placa:", veiculo[0])
                    print("Marca:", veiculo[1])
                    print("Modelo:", veiculo[2])
                    print("Ano:", veiculo[3])
                    print("Cor:", veiculo[4])
                    print("kmRodados:",veiculo[5])
                    print("Preco:", veiculo[6])
                    print("-----------------------")

        except Error as erro:
            print("Erro ao pesquisar Veiculo:", erro)
        finally:
            conexao.close()

#Função para pesquisar por CPF da pesssoa física
def pesquisarPessoaFisica(cpfPessoaFisica):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM PessoaFisica WHERE cpfPessoaFisica=?", (cpfPessoaFisica,))
            pessoas = cursor.fetchall()

            if len(pessoas) == 0:
                print("Nenhuma pessoa encontrada.")
            else:
                print("Pessoa encontrada:")
                for pessoa in pessoas:
                    print("Cpf:", pessoa[0])
                    print("Rg:", pessoa[1])
                    print("Nome:", pessoa[2])
                    print("Endereco:", pessoa[3])
                    print("Bairro:", pessoa[4])
                    print("Numero:",pessoa[5])
                    print("Cep:", pessoa[6])
                    print("Email:",pessoa[7])
                    print("Data de Nascimento:", pessoa[8])
                    print("-----------------------")

        except Error as erro:
            print("Erro ao pesquisar pessoa:", erro)
        finally:
            conexao.close()

#Função para pesquisar todas as compras
def pesquisarCompra():
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM Compra")
            compras = cursor.fetchall()

            if len(compras) == 0:
                print("Nenhuma compra encontrada.")
            else:
                print("Compras encontrados:")
                for compra in compras:
                    print(compra)
                    print("-----------------------")

        except Error as erro:
            print("Erro ao pesquisar compras:", erro)
        finally:
            conexao.close()


#----- Funções para remoção -----

#Remocao da garagem Jython por CNPJ 
def removerGaragemJython(cnpj):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM GaragemJython WHERE Cnpj=?", (cnpj))
            conexao.commit()
            print("Registro removido com sucesso da tabela GaragemJython.")
        except Error as erro:
            print("Erro ao remover o registro da tabela GaragemJython:", erro)
        finally:
            conexao.close()

#Remover Funcionario por CPF
def removerFuncionario(cpfFuncionario):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM Funcionario WHERE cpfFuncionario=?", (cpfFuncionario))
            conexao.commit()
            print("Registro removido com sucesso da tabela Funcionario.")
        except Error as erro:
            print("Erro ao remover o registro da tabela Funcionario:", erro)
        finally:
            conexao.close()

#Remover Veiculo por placa
def removerVeiculo(placa):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM Veiculo WHERE placa=?", (placa))
            conexao.commit()
            print("Registro removido com sucesso da tabela Veiculo.")
        except Error as erro:
            print("Erro ao remover o registro da tabela Veiculo:", erro)
        finally:
            conexao.close()

#Remover Pessoa Fisica por CPF
def removerPessoaFisica(cpfPessoaFisica):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM PessoaFisica WHERE cpfPessoaFisica=?",(cpfPessoaFisica))
            conexao.commit()
            print("Registro removido com sucesso na tabela PessoaFisica.")
        except Error as erro:
            print("Erro ao remover o registro na tabela PessoaFisica:", erro)
        finally:
            conexao.close()

#Remover Pessoa Juridica por CPNJ
def removerPessoaJuridica(cnpjPessoaJuridica):
    conexao = criarConexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM PessoaJuridica WHERE cnpjPessoaJuridica=?",(cnpjPessoaJuridica))
            conexao.commit()
            print("Registro removido com sucesso na tabela PessoaJuridica.")
        except Error as erro:
            print("Erro ao remover o registro na tabela PessoaJuridica:", erro)
        finally:
            conexao.close()

# Exemplo de uso das funções
if __name__ == '__main__':
    criarTabelas()

    #----- INSERCAO -----   
     
    # Exemplo de inserção na tabela GaragemJython:
    inserirGaragemJython("33.310.386/0001-97", "Close Car", "Rua das Flores", "Centro", 123, "12345-678", "closecar@example.com")

    # Exemplo de inserção na tabela Funcionario:
    inserirFuncionario("111.222.333-44", "1234567", "João da Silva", "Vendedor", 3000.0, "Rua do Comércio", "Bairro Novo", 456, "87654-321", "joao@example.com")

    # Exemplo de inserção na tabela Veiculo:
    inserirVeiculo("ABC1234", "Chevrolet", "Onix", "2020-01-01", "Preto", 50000, 45000.0)

    # Exemplo de inserção na tabela PessoaFisica:
    inserirPessoaFisica("555.666.777-88", "7654321", "Maria Oliveira", "Avenida Principal", "Centro", 789, "56789-012", "maria@example.com", "1990-05-15")

    # Exemplo de inserção na tabela PessoaJuridica:
    inserirPessoaJuridica("22.444.666/0001-99", "Auto Peças Ltda", "Rua dos Carros", "Centro", 456, "98765-432", "autopecas@example.com")

    # Exemplo de inserção na tabela Compra:
    inserirCompra(1, "33.310.386/0001-97", "111.222.333-44", "555.666.777-88", "22.444.666/0001-99", "ABC1234")
    inserirCompra(2, "33.310.386/0001-97", "111.222.333-44", "555.666.777-88", "22.444.666/0001-99", "ABC1234")
    
    #----- PESQUISA ------
    pesquisarFuncionario("111.222.333-44")
    pesquisarVeiculo("ABC1234")
    pesquisarCompra()
    pesquisarPessoaFisica("555.666.777-88")
    
    #Sem exemplos de remoção bastar chamar as funções de remoção e passar os parâmetros


