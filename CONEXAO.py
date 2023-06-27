import mysql.connector

class Conexao:
        def __init__(self):
            self.connection = mysql.connector.connect(
                host='localhost',
                user='Ouvidoria',
                password='ouvidoria',
                database='ouvidoria',
            )
            self.cursor = self.connection.cursor()

        def registrar_usuarios(self):
            sql='SELECT * FROM ocorrencias'

            self.cursor.execute(sql)
            lista_usuario= self.cursor.fetchall()

            return lista_usuario

        def cadastrar_usuario(self, titulo, tipo, descricao):
                sql='INSERT INTO ocorrencias(titulo, tipo, descricao) VALUES (%s,%s,%s)'
                data=(titulo, tipo, descricao)

                self.cursor.execute(sql, data)
                self.connection.commit()

                userId = self.cursor.lastrowid
                return userId

        def deletar_usuario(self, id):
            sql='DELETE from ocorrencias where id=%s'
            data=(id,)

            self.cursor.execute(sql, data)
            self.connection.commit()

            recordAffect = self.cursor.rowcount

            return recordAffect

        def atualizar_usuario(self, titulo, tipo, descricao):
            sql = 'UPDATE ocorrencias set titulo=%s, tipo=%s, descricao=%s where id=%s'
            data = (nome, tipo, usuario, id)

            self.cursor.execute(sql, data)
            self.connection.commit()

            lista_afetada = self.cursor.rowcount

            return lista_afetada

        def close_conexao(self):
            self.cursor.close()
            self.connection.close()


conexao = Conexao()

lista_usuarios = conexao.listar_usuarios()
for usuario in lista_usuarios:
        print(usuario)
        print(usuario[0], usuario[1])

conexao.close_conexao()