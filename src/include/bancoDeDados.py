import sqlite3

caminho = 'sqlScripts/'

class BancoDeDados():
    """
    Cria e manipula o banco de dados
    """

    def __init__(self, database):
        """
        Define o nome do arquivo e o comando a ser feito
        """

        self.database = database
        self.conectar()

    def conectar(self):
        self.conexao = sqlite3.connect(self.database)
        self.cursor = self.conexao.cursor()
        self.conectado = True

    def fecharConexao(self):
        self.conexao.commit()
        self.conexao.close()
        self.conectado = False

    def executarScript(self, sqlScript):
        if not self.conectado:
            self.conectar()

        # lê o arquivo com o script sql e executa
        #
        script = f"{caminho}{sqlScript}"
        arquivoSql = open(script)
        stringSql = arquivoSql.read()

        self.cursor.executescript(stringSql)

        self.fecharConexao()

    def executarComando(self, cmd, dados = None):
        if not self.conectado:
            self.conectar()

        if dados is None:
            res = self.cursor.execute(cmd)

        else:
            res = self.cursor.execute(cmd, dados)

        return res

    def inserirDados(self, nomeTabela, dados):
        # os dados a serem inseridos devem estar definidos
        # em uma lista
        if type(dados) is not list:
            return None

        if not self.validaTabela(nomeTabela):
            return None

        else:
            params = self.contarParametros(nomeTabela)
            params = self.montarParametros(params)

            sql = f"insert into {nomeTabela} values ({params})"
            self.executarComando(sql, dados)

            self.fecharConexao()

    def contarParametros(self, nomeTabela):
        """
        Essa função conta a quantidade de parâmetros que uma tabela detém,
        esse número de retorno, serve para montar a string do insert futuro
        """

        infoTabela = f"pragma table_info('{nomeTabela}')"
        res = self.executarComando(infoTabela)
        info = res.fetchall()

        return len(info)

    def montarParametros(self, quantidade):
        caracteres = '?' * quantidade

        # monta um parâmetro válido para a inserção dos dados
        # em uma tabela.
        # por exemplo para a tabela A ele gera (?, ?, ?, ?),
        # como se a tabela A tivesse quatro parâmetros
        caracteres = caracteres.replace('??', '?, ?')
        caracteres = caracteres.replace('??', '?, ?')

        return caracteres

    def validaTabela(self, nomeTabela):
        # interagimos com essas tabelas na interface gráfica
        tabelas = ['funcionario', 'cliente', 'veiculo', 'historico']
        if nomeTabela not in tabelas:
            return False
        return True

# A maneira de utilizar essa classe é da seguinte forma:
#
script = 'createDb.sql'
databaseFile = 'test.db'
db = BancoDeDados(databaseFile)
db.executarScript(script)

dadosFuncionario = [ '123', '123', 'nome', 'cargo', 123, 'endereco',
                     'bairro', 123, 'cep', 'email' ]

dadosVeiculo = [ 'placa', 'marca', 'modelo', 1999-10-10, 'cor', 123, 123 ]

db.inserirDados('funcionario', dadosFuncionario)
db.inserirDados('veiculo', dadosVeiculo)
