import mysql.connector

# Classe de conexao com o banco de dados
class Conexao:
        def __init__(self):
            # Dados para se conectar ao banco de dados
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='dbz123456789',
                database='OcorrenciaSQL'
            )
            self.cursor = self.connection.cursor()

        # aqui ele faz a operacoes no banco de dados e envia o dados,
        # sem alteracao, para a classe Ouvidoria
        def get_ocorrencia(self, tipo_lista):
            sql=''
            if tipo_lista==4:
                sql = 'SELECT * FROM ocorrenciasql'
                self.cursor.execute(sql)
            else:
                sql = 'SELECT * FROM ocorrenciasql where tipo=%s'
                data = (tipo_lista, )
                self.cursor.execute(sql, data)
            lista_ocorrencias = self.cursor.fetchall()

            return lista_ocorrencias

        # Monta o comando SQL para executar no banco de dados e retorna o ultimo id cadastrado
        # ou seja, retorna o id dos dados cadastrado
        def post_ocorrencia(self, titulo, tipo, descricao):
            sql='INSERT INTO ocorrenciasql(titulo, tipo, descricao) VALUES (%s,%s,%s)'
            data=(titulo, tipo, descricao)

            self.cursor.execute(sql, data)
            self.connection.commit()

            userId = self.cursor.lastrowid
            return userId
        
        # Monta a mensagem SQL para retorna a lista com id que o cliente quiser
        # e retorna a lista de dados da tabela no banco de dados
        def search_ocorrencia(self, id):
             sql = 'select * from ocorrenciasql where id=%s'
             data = (id, )

             self.cursor.execute(sql, data)
             lista_ocorrencia = self.cursor.fetchall()

             return lista_ocorrencia

        # Deleta a linha no banco de dados e retorna a quantidade de linhas
        # excluidas
        def delete_ocorrencia(self, id):
            sql='DELETE from ocorrenciasql where id=%s'
            data=(id,)

            self.cursor.execute(sql, data)
            self.connection.commit()

            recordAffect = self.cursor.rowcount

            return recordAffect

        def close_conexao(self):
            self.cursor.close()
            self.connection.close()
