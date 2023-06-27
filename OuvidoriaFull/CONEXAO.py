import mysql.connector

# Classe de conexao com o banco de dados
class Conexao:
        def __init__(self):
            self.connection = mysql.connector.connect(
                host='localhost',
                user='Ouvidoria',
                password='ouvidoria',
                database='ouvidoria',
            )
            self.cursor = self.connection.cursor()

        def get_ocorrencia(self):
            # Metodo que ira pegar os dados das ocorrencias registradas
            sql='SELECT * FROM OcorrenciasSQL'

            self.cursor.execute(sql)
            lista_ocorrencia= self.cursor.fetchall()

            return lista_ocorrencia

        def post_ocorrencia(self, titulo, tipo, descricao):
            # Adiciona uma nova linha no banco de dados, com os dados recebidos pela classse
            sql='INSERT INTO OcorrenciasSQL(titulo, tipo, descricao) VALUES (%s,%s,%s)'
            data=(titulo, tipo, descricao)

            self.cursor.execute(sql, data)
            self.connection.commit()

            userId = self.cursor.lastrowid
            return userId
        
        def search_ocorrencia(self, id):
             sql = 'select * from OcorrenciasSQL where id=%s'
             data = (id, )

             self.cursor.execute(sql, data)
             lista_ocorrencia = self.cursor.fetchall()

             return lista_ocorrencia

        def delete_ocorrencia(self, id):
            sql='DELETE from OcorrenciasSQL where id=%s'
            data=(id,)

            self.cursor.execute(sql, data)
            self.connection.commit()

            recordAffect = self.cursor.rowcount

            return recordAffect

        def close_conexao(self):
            self.cursor.close()
            self.connection.close()
