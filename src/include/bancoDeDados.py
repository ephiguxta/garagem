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

    def executar(self, sqlScript, cmds = None):
        if not self.conectado:
            self.conectar()

        # executa o arquivo de script caso for passado e
        # não exista um parâmetro com comandos sql
        #
        if cmds is None and sqlScript is not None:
            # lê o arquivo com o script sql e executa
            #
            arquivoSql = open(sqlScript)
            stringSql = arquivoSql.read()

            self.cursor.executescript(stringSql)

        elif cmds is not None and sqlScript is None:
            # TODO: implementar os comandos por parâmetro

        else:
            print("Erro!")

        self.fecharConexao()

# A maneira de utilizar essa classe é da seguinte forma:
#
# script = 'createDb.sql'
# db = BancoDeDados(arquivo = db)
# db.executar(sqlScript = script)
