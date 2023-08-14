import sqlite3
from os.path import exists

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
        self.conectado = False
        self.checarExistencia()

    def checarExistencia(self):
        # caso não exista o BD, cria um novo através do script
        # principal.
        if exists(self.database):
            self.conectar()

        else:
            self.executarScript('createDb.sql')

    def conectar(self):
        self.conexao = sqlite3.connect(self.database)
        self.cursor = self.conexao.cursor()
        self.conectado = True

    def fecharConexao(self):
        # TODO:
        # verifique se a abertura e fechamento constante implica numa
        # considerável perda de performance.
        #
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

        # TODO:
        # todos os comandos direto no BD devem ser validados,
        # desde o script sql até os dados que serão inseridos.
        #
        if dados is None:
            res = self.cursor.execute(cmd)

        else:
            res = self.cursor.execute(cmd, dados)

        return res

    def inserirDados(self, nomeTabela, dados):
        # os dados a serem inseridos devem estar definidos
        # em uma lista
        if type(dados) is not list:
            return False

        if not self.validaTabela(nomeTabela):
            return False

        else:
            nParams = self.contarParametros(nomeTabela)
            params = self.montarParametros(nParams)

            sql = f"insert into {nomeTabela} values ({params})"
            self.executarComando(sql, dados)

            self.fecharConexao()

    def contarParametros(self, nomeTabela):
        """
        Esse método conta a quantidade de parâmetros que uma tabela detém,
        esse número de retorno, serve para montar a string do insert futuro
        """

        infoTabela = f"pragma table_info('{nomeTabela}')"
        res = self.executarComando(infoTabela)
        info = res.fetchall()

        return len(info)

    def montarParametros(self, quantidade):
        """
        Monta um parâmetro válido para a inserção dos dados
        em uma tabela.
        Por exemplo para a tabela A ele gera (?, ?, ?, ?),
        pois a tabela A contém quatro campos
        """

        caracteres = '?' * quantidade

        caracteres = caracteres.replace('??', '?, ?')
        caracteres = caracteres.replace('??', '?, ?')

        return caracteres

    def validaTabela(self, nomeTabela):
        # interagimos com essas tabelas na interface gráfica
        tabelas = ['funcionario', 'cliente', 'veiculo', 'compra', 'historico']
        if nomeTabela not in tabelas:
            return False
        return True

    def pesquisar(self, tabela, nome):

        # dependendo da tabela pode precisar de mais parâmetros
        #
        params = ''
        if tabela == 'funcionario':
            params = '*'
            column = 'nome'
            comando = f"select {params} from {tabela} where {column} like '%{nome}%'"
        if tabela == 'cliente':
            params = '*'
            column = 'nome'
            comando = f"select {params} from {tabela} where {column} like '%{nome}%'"
        if tabela == 'veiculo':
            params = 'modelo, cor, ano, marca, placa, kmRodados, preco'
            column = 'modelo'
            comando = f"select {params} from {tabela} where {column} like '%{nome}%'"
        if tabela == 'compra':
            comando = f"select * from {tabela}"

        res = self.executarComando(comando)
        res = res.fetchall()

        return res
"""
# A maneira de utilizar essa classe é da seguinte forma:
#


dadosFuncionario = [ '123', '123', 'nome', 'cargo', 123, 'endereco',
                     'bairro', 123, 'cep', 'email', '2131231232' ]
db.inserirDados('funcionario', dadosFuncionario)

dadosVeiculo = [ 'placa', 'marca', 'modelo', 1999-10-10, 'cor', 123, 123 ]

db.inserirDados('veiculo', dadosVeiculo)
"""

script = 'createDb.sql'
databaseFile = 'test.db'
db = BancoDeDados(databaseFile)
db.executarScript(script)
