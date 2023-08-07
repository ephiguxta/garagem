import sqlite3
from sqlite3 import Error

# Função para criar a tabela no banco de dados
def criar_tabela(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)  
    except Error as e:
        print(e)

# Define o caminho e nome do banco de dados
database = 'bdGaragemJython.db'

try:
    # Conecta ao banco de dados ou cria se não existir
    conn = sqlite3.connect(database)

    sql_statements = [
        """
        CREATE TABLE IF NOT EXISTS `Garagem Jython` (
            `Cnpj` VARCHAR(14) NOT NULL,
            `nomeFantasia` VARCHAR(45) NOT NULL,
            PRIMARY KEY (`Cnpj`)
        )""",
        """
        CREATE TABLE IF NOT EXISTS `Veiculo` (
            `placa` VARCHAR(7) NOT NULL,
            `marca` VARCHAR(15) NOT NULL,
            `ano` DATE NOT NULL,
            `cor` VARCHAR(15) NOT NULL,
            `preco` FLOAT NOT NULL,
            `kmRodados` INTEGER NOT NULL,
            `CnpjJython` VARCHAR(14) NOT NULL,
            PRIMARY KEY (`placa`),
            FOREIGN KEY (`CnpjJython`)
            REFERENCES `Garagem Jython` (`Cnpj`)
            ON DELETE RESTRICT
            ON UPDATE CASCADE
        )""",
        """
        CREATE TABLE IF NOT EXISTS `Pessoa` (
            `idPessoa` INTEGER NOT NULL,
            `rg` VARCHAR(45) NOT NULL,
            `nome` VARCHAR(45) NOT NULL,
            `bairro` VARCHAR(45) NOT NULL,
            `numero` INTEGER NOT NULL,
            `cep` VARCHAR(8) NOT NULL,
            `telefone` VARCHAR(11) NOT NULL,
            `email` VARCHAR(45) NULL,
            `dataNasc` VARCHAR(10) NOT NULL,
            `sexo` CHAR(1) NOT NULL,
            PRIMARY KEY (`idPessoa`)
        )""",
        """
        CREATE TABLE IF NOT EXISTS `PessoaJuridica` (
            `cnpj` VARCHAR(14) NOT NULL,
            `nomeFantasia` VARCHAR(45) NOT NULL,
            `idPessoa` INTEGER NOT NULL,
            PRIMARY KEY (`cnpj`),
            FOREIGN KEY (`idPessoa`)
            REFERENCES `Pessoa` (`idPessoa`)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        )""",
        """
        CREATE TABLE IF NOT EXISTS `Funcionario` (
            `cargo` VARCHAR(45) NOT NULL,
            `salario` FLOAT NOT NULL,
            `CnpjJython` VARCHAR(14) NOT NULL,
            `cpfFuncionario` VARCHAR(11) NOT NULL,
            `idPessoa` INTEGER NOT NULL,
            PRIMARY KEY (`cpfFuncionario`),
            FOREIGN KEY (`CnpjJython`)
            REFERENCES `Garagem Jython` (`Cnpj`)
            ON DELETE RESTRICT
            ON UPDATE CASCADE,
            FOREIGN KEY (`idPessoa`)
            REFERENCES `Pessoa` (`idPessoa`)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        )""",
        """
        CREATE TABLE IF NOT EXISTS `PessoaJuridica_compra_de_funcionario_Veiculo` (
            `cnpjPessoaJuridica` VARCHAR(14) NOT NULL,
            `cpfFuncionario` VARCHAR(11) NOT NULL,
            `CnpjJython` VARCHAR(14) NOT NULL,
            `placaVeiculo` VARCHAR(7) NOT NULL,
            PRIMARY KEY (`cnpjPessoaJuridica`, `cpfFuncionario`, `CnpjJython`, `placaVeiculo`),
            FOREIGN KEY (`cnpjPessoaJuridica`)
            REFERENCES `PessoaJuridica` (`cnpj`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
        )""",
        """
        CREATE TABLE IF NOT EXISTS `Venda` (
            `idVenda` INTEGER NOT NULL ,
            `cpfFuncionario` VARCHAR(11) NOT NULL,
            `placaVeiculo` VARCHAR(7) NOT NULL,
            `CnpjJython` VARCHAR(14) NOT NULL,
            PRIMARY KEY (`idVenda`),
            FOREIGN KEY (`cpfFuncionario`)
            REFERENCES `Funcionario` (`cpfFuncionario`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
            FOREIGN KEY (`placaVeiculo`, `CnpjJython`)
            REFERENCES `Veiculo` (`placa`, `CnpjJython`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
        )""",
        """
        CREATE TABLE IF NOT EXISTS `Compra` (
            `idVenda` INTEGER NOT NULL,
            `idPessoa` INTEGER NOT NULL,
            PRIMARY KEY (`idVenda`),
            FOREIGN KEY (`idVenda`)
            REFERENCES `Venda` (`idVenda`)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
            FOREIGN KEY (`idPessoa`)
            REFERENCES `Pessoa` (`idPessoa`)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        )""",
        """
        CREATE TABLE IF NOT EXISTS `Pessoa Fisica` (
            `idPessoa` INTEGER NOT NULL,
            `cpfPessoaFisica` VARCHAR(11) NOT NULL,
            PRIMARY KEY (`idPessoa`),
            FOREIGN KEY (`idPessoa`)
            REFERENCES `Pessoa` (`idPessoa`)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        )"""
    ]

    # Executa as instruções SQL para criar as tabelas
    for sql_statement in sql_statements:
        criar_tabela(conn, sql_statement)

    print("Tabelas criadas com sucesso!")

except Error as e:
    print(e)

finally:
    # Fecha a conexão com o banco de dados
    conn.close()
# Função para conectar ao banco de dados
def criar_conexao():
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
        return None

# Função para inserir um registro na tabela Garagem Jython
def inserir_garagem_jython(cnpj, nome_fantasia):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `Garagem Jython` (Cnpj, nomeFantasia) VALUES (?, ?)", (cnpj, nome_fantasia))
            conn.commit()
            print("Registro inserido com sucesso na tabela Garagem Jython.")
        except Error as e:
            print("Erro ao inserir o registro:", e)
        finally:
            conn.close()

# Função para remover um registro da tabela Garagem Jython
def remover_garagem_jython(cnpj):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `Garagem Jython` WHERE Cnpj=?", (cnpj,))
            conn.commit()
            print("Registro removido com sucesso da tabela Garagem Jython.")
        except Error as e:
            print("Erro ao remover o registro:", e)
        finally:
            conn.close()

# Função para alterar o nome fantasia na tabela Garagem Jython
def atualizar_garagem_jython(cnpj, novo_nome_fantasia):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE `Garagem Jython` SET nomeFantasia=? WHERE Cnpj=?", (novo_nome_fantasia, cnpj))
            conn.commit()
            print("Registro atualizado com sucesso na tabela Garagem Jython.")
        except Error as e:
            print("Erro ao atualizar o registro:", e)
        finally:
            conn.close()

# Exemplo de uso das funções:
if __name__ == '__main__':
    # Inserindo um registro na tabela Garagem Jython
    inserir_garagem_jython("33.310.386/0001-97", "Close Car")

    # Alterando o nome fantasia de um registro na tabela Garagem Jython
    atualizar_garagem_jython("33.310.386/0001-97", "Nova Razão Social")

    # Removendo um registro da tabela Garagem Jython
    remover_garagem_jython("33.310.386/0001-97")

