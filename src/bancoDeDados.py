import sqlite3
from os.path import exists

caminho = "sqlScripts/"


class BancoDeDados:
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
            self.executarScript("createDb.sql")

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

    def executarComando(self, cmd, dados=None):
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
        if type(dados) is not list:
            return False

        if not self.validaTabela(nomeTabela):
            return False

        else:
            if nomeTabela == "venda":
                sql = f"insert into {nomeTabela} (cpf_cliente, cpf_funcionario, data_venda, placa_veiculo) values (?, ?, ?, ?)"
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

        caracteres = "?" * quantidade

        caracteres = caracteres.replace("??", "?, ?")
        caracteres = caracteres.replace("??", "?, ?")

        return caracteres

    def validaTabela(self, nomeTabela):
        # interagimos com essas tabelas na interface gráfica
        tabelas = ["funcionario", "cliente", "veiculo", "venda", "historico"]
        if nomeTabela not in tabelas:
            return False
        return True

    def pesquisar(self, tabela, textoPesquisa="", coluna="nome"):
        # dependendo da tabela pode precisar de mais parâmetros
        #

        if tabela == "venda":
            comando = f"select * from {tabela}"
        else:
            comando = f"select * from {tabela} where {coluna} like '%{textoPesquisa}%'"

        res = self.executarComando(comando)
        res = res.fetchall()

        return res
